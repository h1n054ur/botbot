from twilio.rest import Client
from app.gateways.config import Config

class TwilioGateway:
    def __init__(self):
        config = Config()
        self._client = Client(config.account_sid, config.auth_token)

    def get_client(self):
        return self._client
