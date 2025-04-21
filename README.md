# ⚡ Chaos Harvester

**Extract value from noise using AI.**  
An autonomous backend system that ingests unstructured data (emails, feeds, webhooks), interprets the chaos using GPT, and stores insights in a dashboard-ready database.

---

## 🔧 Stack

- **FastAPI** – API layer  
- **Celery + Redis** – Async task queue  
- **PostgreSQL** – Persistent storage  
- **OpenAI GPT-4** – Chaos interpreter  
- **Docker / Docker Compose** – Dev & deploy  
- **IMAP** – Email fetching & ingestion  

---

## 🚀 Features

- Pulls raw content from emails
- Sends data to GPT for signal extraction
- Asynchronously queues tasks with Celery
- Stores results in PostgreSQL
- Renders insights in a lightweight dashboard
- Dockerized for easy spin-up

---

## 🛠️ Setup

```bash
git clone https://github.com/rsk1999/chaos-harvester.git
cd chaos-harvester
cp .env.example .env
