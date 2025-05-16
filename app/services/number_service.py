from app.core.phone_number import PhoneNumberSearch
from app.gateways.twilio_gateway import TwilioGateway

class NumberService:
    def __init__(self):
        self.search = PhoneNumberSearch()
        self.gateway = TwilioGateway()

    def search_numbers(self, *args, **kwargs):
        return self.search.search(*args, **kwargs)

    def purchase_numbers(self, numbers: list):
        client = self.gateway.get_client()
        return self.search.purchase(numbers, client)
