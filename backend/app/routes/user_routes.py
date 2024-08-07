from fastapi import APIRouter, HTTPException
from app.services.user_service import UserService
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    user_id: str
    name: str
    email: str
    connected_services: list

@router.post("/connect")
async def connect_user(user: User):
    result = UserService.connect_user(user)
    if not result:
        raise HTTPException(status_code=400, detail="Error connecting user")
    return {"message": f"User {user.name} connected successfully"}
