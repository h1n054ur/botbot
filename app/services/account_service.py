from app.core.account import Account

class AccountService:
    def __init__(self):
        self.account = Account()

    def get_usage(self):
        return self.account.get_usage()
