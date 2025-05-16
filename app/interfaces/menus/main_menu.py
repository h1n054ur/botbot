from app.interfaces.menus.base_menu import BaseMenu

class MainMenu(BaseMenu):
    def display(self):
        self.header("Main Menu")
        print("1. 📞 Purchase Numbers")
        print("2. 📟 Manage Numbers")
        print("3. 🧾 Settings & Admin")

    def get_choice(self):
        return input("Select an option: ")
