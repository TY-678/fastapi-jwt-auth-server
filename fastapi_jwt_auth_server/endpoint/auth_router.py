from fastapi import APIRouter, HTTPException
from fastapi.security import HTTPBearer
from fastapi_jwt_auth_server.bo import AbstractUserStore, create_auth_server
from fastapi_jwt_auth_server.schemas import Token, LoginRequest

auth_router = APIRouter()
security = HTTPBearer()

user_store = AbstractUserStore
auth_server = create_auth_server(user_store=user_store)


@auth_router.post("/login", response_model=Token)
async def login(request: LoginRequest) -> Token:
    try:
        user = await auth_server.authenticate_user(request)
        return Token(access_token=auth_server.generate_access_token(user))
    except ValueError as e:
        raise HTTPException(status_code=403, detail=str(e))
