# CHAOS HARVESTER 🔥

Backend system that listens to chaos, processes it with GPT, and harvests value.

## Stack

- FastAPI (API layer)
- Celery + Redis (Async processing)
- PostgreSQL (Data storage)
- OpenAI GPT-4 (Chaos interpreter)
- Docker (Dev & deploy)

## Usage

```bash
docker-compose up --build
