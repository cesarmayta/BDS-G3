from dotenv import load_dotenv
load_dotenv()
import os

class Config:
    SQLALCHEMY_DATABASE_URI= os.getenv('DB_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS=False