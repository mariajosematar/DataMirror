from fastapi import APIRouter
from app.services.mirror_service import MirrorService

router = APIRouter()

@router.get("/mirror_interface")
async def get_mirror_interface():
    return MirrorService.get_mirror_interface()

@router.post("/create_digital_twin")
async def create_digital_twin(user_id: dict):
    return MirrorService.create_digital_twin(user_id)

@router.post("/interact")
async def user_interaction(gesture: dict):
    return MirrorService.user_interaction(gesture)

@router.post("/ask_assistant")
async def ask_assistant(query: dict):
    return MirrorService.ask_assistant(query)

@router.get("/future_prediction")
async def get_future_prediction():
    return MirrorService.get_future_prediction()
