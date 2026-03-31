from datetime import date

from fastapi import APIRouter
router = APIRouter()

from models import student



@router.get("/", tags=["status"])
async def check_health():
    return {
    "status": "ok",

    }

@router.get("/users/{role}/{user_id}", tags=["status"])
async def get_user(user_id: int, role: str):
    return {"user_id": user_id, "role": role}



router.get("/meals/{date}/{hall_id}/{meal}", tags=["status"])
async def get_meal(date: date,hall_id: int, meal: str):
    return {"hall_id": hall_id, "meal": meal, "total_meal_numbers":[], "recipients":[]}









