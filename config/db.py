# config.py
import os

class Config:
    MONGO_URI = os.environ.get('MONGO_URI')  # Puedes establecer esto como variable de entorno
