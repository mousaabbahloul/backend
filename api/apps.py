from django.apps import AppConfig
from .prediction import load_model

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'