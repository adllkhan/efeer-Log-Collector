from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings


load_dotenv()


class Collector(BaseSettings):
    HOST: str
    PORT: int


class Cors(BaseSettings):
    HOST: str = Field(alias="CORS_HOST")
    CREDENTIALS: bool = Field(alias="CORS_CREDENTIALS")
    METHODS: str = Field(alias="CORS_METHODS")
    HEADERS: str = Field(alias="CORS_HEADERS")


class Wazuh(BaseSettings):
    EVENTS_DIR: str = Field(alias="WAZUH_EVENTS_DIR")
