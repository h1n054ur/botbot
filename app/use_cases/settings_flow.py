import logging
from app.interfaces.menus.settings.settings_menu import SettingsMenu

class SettingsFlow:
    """
    Orchestrates the settings & admin standard menu.
    """
    def __init__(self, account_service):
        self.logger = logging.getLogger(__name__)
        self.menu = SettingsMenu()
        self.account_service = account_service

    def start(self):
        self.logger.info("Starting Settings & Admin flow")
        self.menu.display()
        choice = self.menu.get_choice()
        # TODO: implement settings flow
