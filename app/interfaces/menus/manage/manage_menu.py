from app.interfaces.menus.base_menu import BaseMenu

class ManageMenu(BaseMenu):
    def display(self):
        self.header("Manage Numbers")
        # TODO: list active numbers

    def get_choice(self):
        return input("Select a number by index: ")
