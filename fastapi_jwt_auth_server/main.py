from fastapi import FastAPI
from fastapi_jwt_auth_server.endpoint.auth_router import auth_router

app = FastAPI(title="Authorization Server")
app.include_router(auth_router, prefix="/auth", tags=["auth"])


if __name__ == "__main__":
    import uvicorn
    from fastapi_jwt_auth_server.schemas import APIServerConfig
    from fastapi_jwt_auth_server.config.config import env_setting

    api_config = env_setting(APIServerConfig)
    uvicorn.run(
        "fastapi_jwt_auth_server.main:app",
        host=api_config.server_host,
        port=api_config.server_port,
        reload=True,
    )
