from fastapi import APIRouter
from pydantic import BaseModel

from services.dependencies import rag_service
from utils.redis_client import save_message, get_history
from services.dependencies import llm_service
from db.metadata_store import save_booking


router = APIRouter()

class ChatRequest(BaseModel):
    query: str
    user_id: str
    
#for the /chat api endpoints, here we have query and the user_id
@router.post("/chat")
def chat(req: ChatRequest):

    booking_data = llm_service.extract_booking(req.query)
    # print("Booking Data:", booking_data)

    if booking_data and booking_data.get("date"):
        save_booking(booking_data)
        return {
            "message": "Booking confirmed",
            "data": booking_data
        }

    history = get_history(req.user_id)

    full_query = "\n".join(history + [req.query])

    save_message(req.user_id, req.query)

    answer = rag_service.query(full_query)

    save_message(req.user_id, answer)

    return {"answer": answer}
