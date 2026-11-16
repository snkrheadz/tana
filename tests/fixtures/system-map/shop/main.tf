# A made-up shop. The comment below names a resource and must not count as a use:
# google_storage_bucket.receipts
locals {
  region = "asia-northeast1"
  runner = google_service_account.api.email
  note   = "a } brace and google_storage_bucket.receipts inside a string"
}

variable "api_image" {
  type    = string
  default = "registry.example/shop/api:1"
}

resource "google_service_account" "api" {
  account_id = "shop-api"
}

resource "google_cloud_run_v2_service" "api" {
  name     = "shop-api"
  location = local.region

  template {
    service_account = local.runner

    containers {
      image   = var.api_image
      command = ["bun", "run", "src/server.ts"]

      env {
        name  = "ORDERS_TOPIC"
        value = google_pubsub_topic.orders.name
      }
      dynamic "env" {
        for_each = var.api_image == "" ? [] : [1]
        content {
          name  = "PAYMENT_KEY"
          value = "unused"
        }
      }
    }
  }
}

resource "google_compute_region_network_endpoint_group" "api" {
  name = "shop-api-neg"
  cloud_run {
    service = google_cloud_run_v2_service.api.name
  }
}

resource "google_compute_backend_service" "api" {
  name = "shop-api-backend"
  backend {
    group = google_compute_region_network_endpoint_group.api.id
  }
}

resource "google_compute_url_map" "front" {
  name            = "shop-front"
  default_service = google_compute_backend_service.api.id
}

resource "google_pubsub_topic" "orders" {
  name = "orders"
}

resource "google_storage_bucket" "receipts" {
  name = "shop-receipts"
}

resource "google_storage_bucket_iam_member" "api_writes_receipts" {
  bucket = google_storage_bucket.receipts.name
  role   = "roles/storage.objectUser"
  member = "serviceAccount:${google_service_account.api.email}"
}

resource "google_cloud_run_v2_job" "mailer" {
  # Reads google_storage_bucket.receipts some day.
  // Not google_pubsub_topic.orders either.
  /* Nor google_compute_url_map.front
     on a second line. */
  name = "shop-mailer" # nor google_compute_backend_service.api
  template {
    template {
      service_account = google_service_account.api.email
      containers {
        image = var.api_image
      }
    }
  }
}

resource "google_monitoring_alert_policy" "errors" {
  display_name = "shop errors"
  documentation {
    content = <<-EOT
      Open google_cloud_run_v2_job.mailer and look at } the logs.
      Project: ${data.google_project.this.number}
    EOT
  }
}

data "google_project" "this" {}

resource "google_monitoring_dashboard" "overview" {
  dashboard_json = jsonencode({
    topic  = google_pubsub_topic.orders.name
    bucket = google_storage_bucket.receipts.name
    front  = google_compute_url_map.front.name
  })
}
