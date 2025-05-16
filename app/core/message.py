class Message:
    def send_sms(self, from_number: str, to_number: str, body: str):
        """Send an SMS message."""
        raise NotImplementedError
