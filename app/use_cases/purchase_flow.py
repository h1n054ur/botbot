import logging
from app.interfaces.menus.purchase.purchase_menu import PurchaseMenu

class PurchaseFlow:
    """
    Orchestrates the purchase numbers nested flow.
    """
    def __init__(self, number_service):
        self.logger = logging.getLogger(__name__)
        self.menu = PurchaseMenu()
        self.number_service = number_service

    def start(self):
        self.logger.info("Starting Purchase Numbers flow")
        self.menu.display()
        choice = self.menu.get_choice()
        # TODO: proceed with purchase flow
