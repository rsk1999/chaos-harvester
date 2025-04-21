async def ingest_data(data):
    from worker.worker import process_chaos
    process_chaos.delay(data["payload"])
    return {"status": "queued"}
