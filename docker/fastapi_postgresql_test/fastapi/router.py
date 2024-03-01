from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from sqlmodel import Session, select

from database import User, engine

router = APIRouter()

class UserRequest(BaseModel):
    id: str
    name: str
    password: str
    
    
class UserResponse(BaseModel):
    id: str
    name: str


    
@router.post("/users")
def add_users(user_info: UserRequest) -> UserResponse:
    with Session(engine) as session:
        session.add(User(username=user_info.name, password=user_info.password))
        session.commit()
        session.refresh(user_info)
        
    return UserResponse(id=user_info.id, name=user_info.name)


@router.get("/users/")
def get_users() -> list[UserResponse]:
    with Session(engine) as session:
        statement = select(User)
        users = session.exec(statement).all()
        
        return [UserResponse(id=user.id, name=user.name) 
            for user in users
        ]


@router.get("/users/{id}")
def check_user(id: str) -> UserResponse:
    with Session(engine) as session:
        statement = session.get(User, id)
        if not statement:
            raise HTTPException(
                detail="User not found",
                status_code=status.HTTP_404_NOT_FOUND
            )   
        return UserResponse(status=True)