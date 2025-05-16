from shared.settings import Settings

class Config:
    """
    Configuration loader that exposes environment-based settings.
    """
    def __init__(self):
        settings = Settings()
        self.account_sid = settings.TWILIO_ACCOUNT_SID
        self.auth_token = settings.TWILIO_AUTH_TOKEN
