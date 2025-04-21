from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import psycopg2
from app.silent_listener import ingest_data

app = FastAPI()

# ✅ Input validation using Pydantic
class IngestRequest(BaseModel):
    payload: str

# ✅ Ingest endpoint
@app.post("/ingest")
async def ingest(request: IngestRequest):
    return await ingest_data(request.dict())

# ✅ Simple health check (useful for Docker/monitoring)
@app.get("/")
def health():
    return {"status": "chaos harvester online"}

# ✅ Dashboard to show latest GPT results
@app.get("/dashboard", response_class=HTMLResponse)
def dashboard():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="secret",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT insights, created_at FROM extracted_value ORDER BY created_at DESC LIMIT 10")
    rows = cur.fetchall()
    conn.close()

    html = "<h2>🧠 Chaos Insights</h2><ul>"
    for insight, created in rows:
        html += f"<li><strong>{created}</strong><br>{insight}</li>"
    html += "</ul>"
    return html
