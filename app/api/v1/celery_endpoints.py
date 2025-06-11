from fastapi import APIRouter
from pydantic import BaseModel
from app.worker.tasks import print_message

router = APIRouter()

class MessageRequest(BaseModel):
    message: str

@router.post("/send-message/")
def send_message(request: MessageRequest):
    task = print_message.delay(request.message)
    return {"task_id": task.id, "status": "Message sent to worker"}
