from typing import List
from fastapi import HTTPException

from schemas.user import UserCreate

# in-memory storage
user_db: List[dict] = []

def create_user(user: UserCreate) -> dict:
    
    if any(u["email"] == user.email for u in user_db):
        raise HTTPException(status_code=400, detail="User already exists")
    
    user_data = user.model_dump()

    user_data["user_id"] = len(user_db) + 1
    
    user_db.append(user_data)

    return user_data

def get_user(min_age: int = None):
    if not user_db:
        return []
    
    if min_age is not None:
        return [u for u in user_db if u["age"] >= min_age]
    
    return user_db