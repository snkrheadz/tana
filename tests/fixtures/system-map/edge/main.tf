locals {
  region = "x" # a trailing comment, long enough to shift every later offset in this block
  labels = {
    owner = google_service_account.api.email
  }
  policy = jsonencode({
    reader = google_service_account.reader.email
  })
  topic = google_pubsub_topic.events.name # another trailing comment
  last  = "y"
}

variable "image" {
  type = string
}

variable "flavor" {
  type = string
}

resource "google_service_account" "api" {
  account_id = "api"
}

resource "google_service_account" "reader" {
  account_id = "reader"
}

resource "google_pubsub_topic" "events" {
  name = "events"
}

resource "google_storage_bucket" "by_region" {
  name     = "by-region"
  location = local.region
}

resource "google_storage_bucket" "by_labels" {
  name   = "by-labels"
  labels = local.labels
}

resource "google_storage_bucket" "by_policy" {
  name = "by-policy"
  note = local.policy
}

resource "google_storage_bucket" "by_topic" {
  name = "by-topic"
  note = local.topic
}

resource "google_storage_bucket" "escaped" {
  name = "escaped"
  note = "a literal $${google_pubsub_topic.events.name} stays text"
  hint = "%{if google_service_account.api.email != ""}on%{endif}"
}

resource "google_cloud_run_v2_job" "worker" {
  name = "worker"
  mode = 0644

  template {
    containers {
      image = var.image
      args = [
        "run", # the entry point
        "src/worker.ts",
      ]
      flavor = var.flavor
      limits = { cpu = "2" }
    }
  }

  payload = jsonencode({
    name = "inner"
  })

  cloud_run { service = "shop-api" }
}
