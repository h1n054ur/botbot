from app.core.call import Call

class VoiceService:
    def __init__(self):
        self.call = Call()

    def make_call(self, from_number: str, to_number: str):
        return self.call.make_call(from_number, to_number)
