from app.interfaces.menus.purchase.purchase_menu import PurchaseMenu

class PurchaseFlow:
    def __init__(self):
        self.menu = PurchaseMenu()

    def start(self):
        self.menu.display()
        choice = self.menu.get_choice()
        # TODO: proceed with purchase flow
