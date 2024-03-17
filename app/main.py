import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.v1 import router as router_wazuh
from config import host
from config import port
from config import origins


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=router_wazuh, prefix="/v1")

if __name__ == "__main__":
    uvicorn.run("main:app", host=host, port=port)
