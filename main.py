import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.v1 import router_wazuh
from config import Config


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[Config.Cors.dashboard_host],
    allow_credentials=Config.Cors.allow_credentials,
    allow_methods=Config.Cors.methods,
    allow_headers=Config.Cors.headers,
)

app.include_router(router=router_wazuh, prefix="/v1")

if __name__ == "__main__":
    uvicorn.run("main:app", host=Config.host, port=Config.port)
