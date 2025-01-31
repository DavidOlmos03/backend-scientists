from dotenv import load_dotenv
import os

load_dotenv()  

class Config:
    """
        Configurations for the application
    """
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = (
    #     f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    #     f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    # )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
