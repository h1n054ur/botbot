from app.interfaces.menus.manage.manage_menu import ManageMenu

class ManageFlow:
    def __init__(self):
        self.menu = ManageMenu()

    def start(self):
        self.menu.display()
        choice = self.menu.get_choice()
        # TODO: implement manage flow
