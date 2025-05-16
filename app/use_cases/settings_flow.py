from app.interfaces.menus.settings.settings_menu import SettingsMenu

class SettingsFlow:
    def __init__(self):
        self.menu = SettingsMenu()

    def start(self):
        self.menu.display()
        choice = self.menu.get_choice()
        # TODO: implement settings flow
