from pydantic import BaseSettings

class Settings(BaseSettings):
    USER: str
    PASSWORD: str
    HOST: str
    DATABASE: str
    PORT: str



    class Config:
        orm_mode = True
        case_sensitive = True
        env_file = '.env'


settings = Settings()