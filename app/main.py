import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.v1 import router_wazuh
from config import Base as BaseConfig


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=BaseConfig.origins,
    allow_credentials=BaseConfig.allow_credentials,
    allow_methods=BaseConfig.methods,
    allow_headers=BaseConfig.headers,
)

app.include_router(router=router_wazuh, prefix="/v1")

if __name__ == "__main__":
    uvicorn.run("main:app", host=BaseConfig.host, port=BaseConfig.port)
