from pydantic import BaseModel


class SecretConfig(BaseModel):
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int


class APIServerConfig(BaseModel):
    server_host: str
    server_port: int
    debug: bool
