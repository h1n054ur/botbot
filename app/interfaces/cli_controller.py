import logging
from app.interfaces.menus.main_menu import MainMenu
from app.use_cases.purchase_flow import PurchaseFlow
from app.use_cases.manage_flow import ManageFlow
from app.use_cases.settings_flow import SettingsFlow
from app.services.number_service import NumberService
from app.services.voice_service import VoiceService
from app.services.messaging_service import MessagingService
from app.services.account_service import AccountService

class CLIController:
    """
    Orchestrates the main CLI loop and dependency wiring.
    """
    def __init__(self, number_service: NumberService, voice_service: VoiceService,
                 messaging_service: MessagingService, account_service: AccountService):
        self.logger = logging.getLogger(__name__)
        self.number_service = number_service
        self.voice_service = voice_service
        self.messaging_service = messaging_service
        self.account_service = account_service

    def run(self):
        self.logger.info("Starting Twilio Manager CLI")
        while True:
            menu = MainMenu()
            menu.display()
            choice = menu.get_choice()
            if choice == '1':
                PurchaseFlow(self.number_service).start()
            elif choice == '2':
                ManageFlow(self.number_service, self.voice_service, self.messaging_service).start()
            elif choice == '3':
                SettingsFlow(self.account_service).start()
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
