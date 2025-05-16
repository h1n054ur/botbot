from app.core.message import Message

class MessagingService:
    def __init__(self):
        self.message = Message()

    def send_sms(self, from_number: str, to_number: str, body: str):
        return self.message.send_sms(from_number, to_number, body)
