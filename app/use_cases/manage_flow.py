import logging
from app.interfaces.menus.manage.manage_menu import ManageMenu

class ManageFlow:
    """
    Orchestrates the manage numbers nested flow.
    """
    def __init__(self, number_service, voice_service, messaging_service):
        self.logger = logging.getLogger(__name__)
        self.menu = ManageMenu()
        self.number_service = number_service
        self.voice_service = voice_service
        self.messaging_service = messaging_service

    def start(self):
        self.logger.info("Starting Manage Numbers flow")
        self.menu.display()
        choice = self.menu.get_choice()
        # TODO: implement manage flow
