import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev")
    # Configuración de conexión para tu MariaDB local en XAMPP
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://ecommerce_user:123456@localhost/ecommerce_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

