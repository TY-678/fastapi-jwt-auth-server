from typing import Optional, Protocol
from fastapi_jwt_auth_server.core import create_access_token
from fastapi_jwt_auth_server.schemas import LoginRequest


class AbstractUserStore(Protocol):
    async def get_user(self, username: str) -> Optional[dict]:
        """
        Query user information. If usernema exists, return the user information.
        The returned dict contains at least username: str and password: str
        """
        pass


class AuthServer:
    def __init__(self, user_store):
        self.user_store = user_store

    async def authenticate_user(self, request: LoginRequest) -> Optional[dict]:
        if user := await self.user_store.get_user(self, username=request.username):
            if self._verify_password(user, request.password):
                return user
        raise ValueError("Invalid username or password")

    @staticmethod
    def generate_access_token(user: dict) -> str:
        return create_access_token(data={"sub": user["username"], "role": user["role"]})

    @staticmethod
    def _verify_password(user: dict | None, password: str) -> bool:
        if not user:
            return False
        return user.get("password") == password


def create_auth_server(user_store) -> AuthServer:
    return AuthServer(user_store)
