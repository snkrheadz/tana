"""Tests for plugins/tana/skills/system-map/system_map.py.

Usage: python3 -I tests/system_map_test.py
"""
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = os.path.join(HERE, "..", "plugins", "tana", "skills", "system-map", "system_map.py")
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location("system_map", SCRIPT)
system_map = importlib.util.module_from_spec(spec)
spec.loader.exec_module(system_map)

API = "shop:google_cloud_run_v2_service.api"
LB = ["google_compute_url_map.front", "google_compute_backend_service.api", "google_compute_region_network_endpoint_group.api"]


def good_map():
    return {
        "title": 'Shop "order" path',
        "nodes": {
            "buyer": {"label": "Buyer", "evidence": "app/server.ts:4"},
            "lb": {"label": "Load balancer", "group": "Edge", "is": LB},
            "api": {"label": "Shop API", "group": "Run", "is": ["google_cloud_run_v2_service.api", "google_service_account.api"]},
            "orders": {"label": "Orders topic", "is": "google_pubsub_topic.orders"},
            "receipts": {"label": "Receipts", "shape": "store", "is": "google_storage_bucket.receipts"},
            "pay": {"label": "Payment API", "evidence": "app/server.ts:3"},
        },
        "edges": [
            {"from": "buyer", "to": "lb", "label": "HTTPS", "evidence": "shop/main.tf:60"},
            {"from": "lb", "to": "api", "label": "forwards"},
            {"from": "api", "to": "orders", "label": "publishes"},
            {"from": "api", "to": "receipts", "label": "writes"},
            {"from": "api", "to": "pay", "label": "charges", "evidence": "app/server.ts:3"},
        ],
    }


class SystemMapTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        os.chdir(os.path.join(HERE, "fixtures", "system-map"))
        cls.inv = system_map.scan(["shop"])

    def test_scan_lists_every_declared_block(self):
        self.assertEqual(len(self.inv), 12)
        self.assertEqual(self.inv[API]["file"], os.path.join("shop", "main.tf"))
        self.assertEqual(self.inv[API]["line"], 18)

    def test_uses_follow_locals_and_ignore_comments_and_strings(self):
        self.assertEqual(
            sorted(self.inv[API]["uses"]),
            ["shop:google_pubsub_topic.orders", "shop:google_service_account.api"],
        )
        self.assertEqual(self.inv[API]["uses"]["shop:google_service_account.api"], 23)

    def test_comments_inside_a_block_are_not_uses(self):
        mailer = self.inv["shop:google_cloud_run_v2_job.mailer"]
        self.assertEqual(list(mailer["uses"]), ["shop:google_service_account.api"])
        self.assertEqual(mailer["values"]["name"], ["shop-mailer"])

    def test_heredoc_text_is_not_a_use_but_its_interpolation_is(self):
        alert = self.inv["shop:google_monitoring_alert_policy.errors"]
        self.assertEqual(list(alert["uses"]), ["shop:data.google_project.this"])

    def test_string_interpolation_is_a_use(self):
        grant = self.inv["shop:google_storage_bucket_iam_member.api_writes_receipts"]
        self.assertEqual(
            sorted(grant["uses"]), ["shop:google_service_account.api", "shop:google_storage_bucket.receipts"]
        )

    def test_plain_values_keep_their_block_path(self):
        values = self.inv[API]["values"]
        self.assertEqual(values["name"], ["shop-api"])
        self.assertEqual(values["template.containers.command"], ["bun", "run", "src/server.ts"])
        self.assertEqual(values["template.containers.env.name"], ["ORDERS_TOPIC", "PAYMENT_KEY"])

    def test_tfvars_value_wins_over_the_variable_default(self):
        self.assertEqual(self.inv[API]["vars"], {"api_image": "registry.example/shop/api:42"})

    def test_show_prints_uses_and_used_by(self):
        text = "\n".join(system_map.cmd_show(self.inv, "google_service_account.api"))
        self.assertIn("used by  google_cloud_run_v2_job.mailer", text)
        self.assertIn('account_id = "shop-api"', text)

    def test_good_map_draws(self):
        chart, errors, report = system_map.draw(self.inv, good_map())
        self.assertEqual(errors, [])
        self.assertIn("OK 6 boxes, 5 arrows (3 backed by a Terraform reference, 2 by evidence)", report)
        self.assertIn("flowchart LR", chart)
        self.assertIn('title: "Shop \\"order\\" path"', chart)
        self.assertIn('subgraph g1["Edge"]', chart)
        self.assertIn('n_receipts[("Receipts")]', chart)
        self.assertIn('n_buyer(["Buyer"])', chart)
        self.assertIn('n_lb -->|"forwards"| n_api', chart)
        self.assertIn("class n_buyer,n_pay outside", chart)

    def test_report_names_what_the_chart_leaves_out(self):
        spec = good_map()
        spec["edges"] = [e for e in spec["edges"] if e["to"] != "orders"]
        _, errors, report = system_map.draw(self.inv, spec)
        self.assertEqual(errors, [])
        text = "\n".join(report)
        self.assertIn("Tied in the files but not drawn (1):", text)
        self.assertIn("api -- orders  (google_cloud_run_v2_service.api at shop/main.tf:31)", text)
        self.assertIn("Left out: 5 of 12 declared", text)

    def test_a_chain_through_undrawn_resources_ties_two_boxes(self):
        spec = good_map()
        spec["nodes"]["lb"]["is"] = "google_compute_url_map.front"
        _, errors, report = system_map.draw(self.inv, spec)
        self.assertEqual(errors, [])
        self.assertIn("OK 6 boxes, 5 arrows (3 backed by a Terraform reference, 2 by evidence)", report)

    def test_two_users_of_one_account_are_not_tied(self):
        spec = good_map()
        spec["nodes"]["api"]["is"] = "google_cloud_run_v2_service.api"
        spec["nodes"]["mailer"] = {"label": "Mailer", "is": "google_cloud_run_v2_job.mailer"}
        spec["edges"] = [{"from": "api", "to": "mailer", "label": "starts"}]
        chart, errors, _ = system_map.draw(self.inv, spec)
        self.assertIsNone(chart)
        self.assertEqual(len(errors), 1)
        self.assertIn("arrow api -> mailer: no reference in the Terraform files ties these boxes", errors[0])

    def test_invented_box_fails(self):
        spec = good_map()
        spec["nodes"]["cache"] = {"label": "Cache", "is": "google_redis_instance.cache"}
        spec["nodes"]["queue"] = {"label": "Queue"}
        _, errors, _ = system_map.draw(self.inv, spec)
        self.assertEqual(len(errors), 2)
        self.assertIn("nothing in the Terraform files matches 'google_redis_instance.cache'", errors[0])
        self.assertIn("box 'queue' names nothing in the Terraform files, so it needs evidence", errors[1])

    def test_bad_evidence_fails(self):
        for evidence, message in [
            ("app/server.ts:99", "evidence line is missing or blank"),
            ("app/server.ts:2", "evidence line is missing or blank"),
            ("app/gone.ts:1", "evidence file not found"),
            ("app/server.ts", "evidence must be path:line"),
        ]:
            spec = good_map()
            spec["edges"][4]["evidence"] = evidence
            _, errors, _ = system_map.draw(self.inv, spec)
            self.assertEqual(len(errors), 1, evidence)
            self.assertIn(message, errors[0])

    def test_one_resource_in_two_boxes_fails(self):
        spec = good_map()
        spec["nodes"]["orders"]["is"] = ["google_pubsub_topic.orders", "google_service_account.api"]
        _, errors, _ = system_map.draw(self.inv, spec)
        self.assertEqual(len(errors), 1)
        self.assertIn("shop:google_service_account.api is in two boxes", errors[0])

    def test_command_line_exits_1_and_prints_no_chart_on_a_bad_map(self):
        # The dashboard uses the topic, the bucket, and the url map. A resource that uses
        # three boxes says nothing about any two of them.
        spec = good_map()
        spec["edges"] += [{"from": "orders", "to": "receipts"}, {"from": "lb", "to": "orders"}]
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
            json.dump(spec, f)
        try:
            run = subprocess.run([sys.executable, "-I", SCRIPT, "draw", f.name, "shop"], capture_output=True, text=True)
        finally:
            os.unlink(f.name)
        self.assertEqual(run.returncode, 1)
        self.assertEqual(run.stdout, "")
        self.assertIn("arrow orders -> receipts", run.stderr)
        self.assertIn("arrow lb -> orders", run.stderr)

    def test_command_line_scan(self):
        run = subprocess.run([sys.executable, "-I", SCRIPT, "scan", "."], capture_output=True, text=True)
        self.assertEqual(run.returncode, 0)
        self.assertIn("shop  (12 declared)", run.stdout)
        self.assertIn("     1  google_storage_bucket_iam_member", run.stdout)


if __name__ == "__main__":
    unittest.main()
