from app.interfaces.menus.base_menu import BaseMenu

class SettingsMenu(BaseMenu):
    def display(self):
        self.header("Settings & Admin")
        print("1. Usage & Billing")
        print("2. Security & Compliance")
        print("3. Subaccount Management")
        print("4. Developer Tools")
        print("5. Account Logs")
        print("6. Advanced Search")
        print("7. Configuration Management")
        print("8. Logs & Diagnostics")
        print("9. Back")

    def get_choice(self):
        return input("Select an option: ")
