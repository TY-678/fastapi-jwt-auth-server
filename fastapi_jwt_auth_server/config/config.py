from pydantic import BaseModel
from pydantic_settings import BaseSettings


class EnvironmentSettings(BaseSettings):
    class Config:
        env_file = "config.env"
        extra = "ignore"

    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    server_host: str
    server_port: int
    debug: bool


def env_setting(model: BaseModel):
    settings = EnvironmentSettings()
    return model(**settings.model_dump())
