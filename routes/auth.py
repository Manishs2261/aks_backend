from fastapi import APIRouter, HTTPException, status
from datetime import datetime
from models.auth import LoginRequest, RegisterRequest
from database import users_collection

router = APIRouter(prefix="/api", tags=["Auth"])


@router.post("/login")
async def login(request: LoginRequest):
    user = await users_collection.find_one({"email": request.email})

    if not user or user["password"] != request.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    return {
        "success": True,
        "message": "Login successful"
    }


@router.post("/register")
async def register(request: RegisterRequest):
    existing_user = await users_collection.find_one({"email": request.email})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"
        )

    new_user = {
        "email": request.email,
        "password": request.password,  
        "name": request.name,
        "created_at": datetime.utcnow()
    }

    try:
        await users_collection.insert_one(new_user)
        return {
            "success": True,
            "message": "User registered successfully"
        }
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Registration failed"
        )
