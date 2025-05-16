class PhoneNumberSearch:
    def __init__(self):
        self.found_numbers = set()

    def search(self, country_code: str, area_code: int = None, pattern: str = None, limit: int = 500):
        """Perform raw HTTP number search with dedupe and stop criteria."""
        raise NotImplementedError

    def purchase(self, numbers: list, twilio_client):
        """Purchase selected phone numbers via Twilio SDK."""
        raise NotImplementedError
