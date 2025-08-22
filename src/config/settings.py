from loguru import logger
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MYSQL_USER: str
    MYSQL_ROOT_PASSWORD: str
    MYSQL_DATABASE: str
    MYSQL_HOST: str
    OPENAI_API_KEY: str

    @property
    def DATABASE_URL(self) -> str:
        return f"mysql+mysqlconnector://{self.MYSQL_USER}:{self.MYSQL_ROOT_PASSWORD}@{self.MYSQL_HOST}:3306/{self.MYSQL_DATABASE}"

    class Config:
        env_file = ".env"


settings = Settings()

logger.add("file.log", rotation="500 MB", level="INFO")
logger.add(lambda msg: print(msg), level="DEBUG")
