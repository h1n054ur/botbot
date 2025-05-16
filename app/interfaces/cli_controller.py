from app.interfaces.menus.main_menu import MainMenu
from app.use_cases.purchase_flow import PurchaseFlow
from app.use_cases.manage_flow import ManageFlow
from app.use_cases.settings_flow import SettingsFlow

class CLIController:
    def run(self):
        while True:
            menu = MainMenu()
            menu.display()
            choice = menu.get_choice()
            if choice == '1':
                PurchaseFlow().start()
            elif choice == '2':
                ManageFlow().start()
            elif choice == '3':
                SettingsFlow().start()
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
