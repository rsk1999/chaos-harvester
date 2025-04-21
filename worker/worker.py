from celery import Celery
from app.chaos_interpreter import analyze_chaos

# ✅ Use localhost because you're running Redis locally
app = Celery("tasks", broker="redis://localhost:6379/0")

@app.task
def process_chaos(raw_input):
    result = analyze_chaos(raw_input)
    print(f"Harvested: {result}")
    return result
