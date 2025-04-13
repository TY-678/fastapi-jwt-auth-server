from datetime import datetime, timedelta
from fastapi import HTTPException
from jose import jwt, JWTError
from fastapi_jwt_auth_server.config import env_setting
from fastapi_jwt_auth_server.schemas import SecretConfig


config: SecretConfig = env_setting(SecretConfig)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (timedelta(minutes=config.access_token_expire_minutes))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, config.secret_key, algorithm=config.algorithm)


def decode_token(token: str) -> None:
    try:
        return jwt.decode(token, config.secret_key, algorithms=[config.algorithm])
    except JWTError as e:
        raise HTTPException(status_code=403, detail=f"Token decode error: {str(e)}")
