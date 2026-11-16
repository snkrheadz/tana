---
name: system-map
description: Draw a service or a cloud environment as a Mermaid flowchart from its Terraform files and app config, with every box and arrow checked against a file and a line. Use for /tana:system-map, or "draw the architecture", "diagram this environment".
disable-model-invocation: true
---

# System map

The chart shows what runs, what it talks to, and where data rests, in the words of the person who reads it. A script reads the Terraform files, so the chart cannot hold a box that the config does not declare. You choose what to show and what to call it. For why the check comes before the drawing, see `../mode/pillars/sounding.md`.

## Tools

- Python 3.8 or later, standard library only. The script needs no Terraform binary, no state, and no cloud login.
- `python3 -I <skill dir>/system_map.py scan DIR...` lists each Terraform folder under `DIR` with a count per resource type.
- `python3 -I <skill dir>/system_map.py show PATTERN DIR...` prints a resource: its file and line, its plain values (name, image, command, env names, schedule), what it uses, and what uses it. `PATTERN` is a glob over `type.name`, such as `'google_cloud_run_v2_service.*'`. More than three matches print as a list.
- `python3 -I <skill dir>/system_map.py draw map.json DIR... > chart.mmd` checks the map and prints the chart. The report goes to stderr. On an error it exits 1 and prints no chart.
- Run every command from one folder that is a parent of each repo you cite, because evidence paths resolve from there. Keep `map.json` and `chart.mmd` in a scratch folder unless the user wants them committed.

## Steps

1. Pick one question per chart: "how does a request reach the API", "what runs on a schedule and what does it write", "how does a commit reach production". If the user named none, start with the request path. A second question is a second chart.
2. Run `scan` on the Terraform folders. The counts show what the environment is made of and which folders have their own state.
3. Run `show` on the entry point for the question (a load balancer, a scheduler, a queue) and follow `uses` and `used by` from there. Note the plain values that point into the app repo: the image, the command, the env names.
4. Read the app repo for what Terraform cannot know. The Dockerfile and the CI workflows say how an image is built and deployed. Client code says which outside services the app calls. Take a file and a line for each fact.
5. Write `map.json` in the format below. Aim for 15 boxes or fewer. Fold resources that act as one thing into one box: a forwarding rule, a proxy, a URL map, and a backend are "the load balancer". Leave out access grants, alerts, and API switches unless the question is about them.
6. Run `draw`. To fix an error, correct the map. Never cite a line that does not show the fact.
7. Read the report. "Tied in the files but not drawn" lists links that the config has and the chart lacks. Draw each one, or decide that it is off the question and say so in the hand-off.

## Map format

```json
{
  "title": "How an order reaches the shop API",
  "direction": "LR",
  "nodes": {
    "buyer":    {"label": "Buyer", "group": "Outside", "evidence": "shop-app/README.md:12"},
    "lb":       {"label": "Load balancer", "group": "Edge", "is": ["google_compute_url_map.front", "google_compute_backend_service.api"]},
    "api":      {"label": "Shop API", "group": "Run", "is": "google_cloud_run_v2_service.api"},
    "receipts": {"label": "Receipts", "shape": "store", "is": "google_storage_bucket.receipts"},
    "pay":      {"label": "Payment API", "group": "Outside", "evidence": "shop-app/src/server.ts:3"}
  },
  "edges": [
    {"from": "buyer", "to": "lb", "label": "HTTPS", "evidence": "shop-infra/main.tf:60"},
    {"from": "lb", "to": "api", "label": "forwards"},
    {"from": "api", "to": "receipts", "label": "writes", "evidence": "shop-infra/main.tf:74"},
    {"from": "api", "to": "pay", "label": "charges the card", "evidence": "shop-app/src/server.ts:3"}
  ]
}
```

- `is` takes one glob or a list. It names the Terraform resources that the box stands for. A resource can sit in one box only. With several folders, write `folder:type.name` to pick one.
- A box with no `is` is outside the Terraform files: a person, a hosted service, another cloud, another repo. It needs `evidence`, and the chart draws it with a dashed border.
- An arrow with no `evidence` passes when the Terraform files tie its two boxes. Two boxes are tied when one uses the other, directly or through resources that sit in no box. They are also tied when one resource outside every box uses those two boxes and no third, as an access grant does.
- Any other arrow needs `evidence`, written as `path:line` from the folder where you run the command.
- Terraform says that two things are tied. It does not say which way the traffic goes. Point each arrow the way the request or the data moves, and label it with the verb the reader would use.
- `"shape": "store"` marks a place where data rests. `group` puts boxes in one frame. `direction` is `LR` or `TB`.

## What the check cannot see

- A link written as a plain name, such as `service = "shop-api"`. Terraform folders with separate state link this way. `show` prints the plain values, so find the line and cite it as evidence.
- What the code does when it runs. An access grant shows that an account may read a bucket. It does not show that the code reads it. For that, cite the code.
- Whether the files match what is deployed. The chart shows the config at one commit.
- A variable set with `-var`, `-var-file`, or the environment. `show` takes variable values from `terraform.tfvars` and `*.auto.tfvars` only, as a plain `terraform apply` does.
- What an evidence line says. The script checks that the line exists and is not blank. Open each line before you cite it.
- Config that is not Terraform, such as Kubernetes manifests or Compose files. Each box from those files needs evidence.

## Hand off

Show `chart.mmd` as a `mermaid` code block. Under it, give the question the chart answers, the counts from the report, what the chart leaves out, and the ties you chose not to draw. Say that the chart shows the config and not the deployed state. Give the commit of each repo you read and the exact `draw` command, so that the next person can redraw the chart after a change.
