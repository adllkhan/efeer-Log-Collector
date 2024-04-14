import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.v1 import router_wazuh, Cors, Collector


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=Cors().HOST,
    allow_credentials=Cors().CREDENTIALS,
    allow_methods=list(Cors().METHODS),
    allow_headers=list(Cors().HEADERS),
)

app.include_router(
    router=router_wazuh,
    prefix="/api/v1",
    tags=["Wazuh Events"]
)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=Collector().HOST,
        port=Collector().PORT,
        reload=True
    )
