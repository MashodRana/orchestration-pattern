from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from src.tasks import run_pipeline

app = FastAPI(title="Orchestration Service")

class StreamPayload(BaseModel):
    file_url: str
    live_stream_id: str

@app.post("/live-stream-done")
async def live_stream_done(payload: StreamPayload):
    """
    Trigger orchestration pipeline after live stream is done
    """
    task_id = run_pipeline(payload.dict())
    return {"message": "Pipeline started", "task_id": task_id}
