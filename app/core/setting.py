from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "FastAPI"
    SQL_SERVER: str = 'tcp:myserver.database.windows.net' 
    DB_NAME: str = 'mydb' 
    USER_NAME: str = 'myusername' 
    USER_PASSWORD: str = 'mypassword'
    SECRET='SECRET_KEY'
    ALGORITHM='HS256'  

    class Config:
        env_file = ".env"


settings = Settings()