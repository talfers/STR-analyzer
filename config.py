import os
from dotenv import load_dotenv

load_dotenv('./secrets.env')

class Config:
    def __init__(self):
        self.mashvisor_api_base_url = os.environ.get('MASHVISOR_API_BASE_URL', "NOT PROVIDED")
        self.mashvisor_api_host = os.environ.get('MASHVISOR_API_HOST', "NOT PROVIDED")
        self.mashvisor_api_key = os.environ.get('MASHVISOR_API_KEY', "NOT PROVIDED")

    def __str__(self):
        return f"api host: {self.mashvisor_api_host}"