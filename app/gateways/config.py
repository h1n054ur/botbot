import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        self.account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        self.auth_token = os.getenv("TWILIO_AUTH_TOKEN")
