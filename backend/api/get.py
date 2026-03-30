from fastapi import APIRouter
router = APIRouter()

@router.get("/", tags=["status"])
async def check_health():
    return {
    "status": "ok",

    }

@router.get("/users/{role}/{user_id}", tags=["status"])
async def get_user(user_id: int, role: str):
    return {"user_id": user_id, "role": role}


