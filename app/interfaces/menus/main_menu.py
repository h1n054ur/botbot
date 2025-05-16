from typing import Dict, Callable
from app.interfaces.menus.base_menu import BaseMenu

# Import stubs for sub-menus
class PurchaseMenu(BaseMenu):
    def display(self): pass
    def handle_choice(self) -> bool: return True

class ManageMenu(BaseMenu):
    def display(self): pass
    def handle_choice(self) -> bool: return True

class SettingsMenu(BaseMenu):
    def display(self): pass
    def handle_choice(self) -> bool: return True

class MainMenu(BaseMenu):
    def __init__(self):
        super().__init__(parent=None)  # Main menu has no parent
        self.purchase_menu = PurchaseMenu(parent=self)
        self.manage_menu = ManageMenu(parent=self)
        self.settings_menu = SettingsMenu(parent=self)

    def display(self):
        """Display the main menu options."""
        self.render_header("🏠 Main Menu")
        self.console.print("1. 📞 Purchase Numbers")
        self.console.print("2. 📟 Manage Numbers")
        self.console.print("3. 🧾 Settings & Admin")
        self.console.print("q. ❌ Quit")

    def handle_choice(self) -> bool:
        """Handle main menu choices."""
        options: Dict[str, Callable] = {
            '1': lambda: self.purchase_menu.show(),
            '2': lambda: self.manage_menu.show(),
            '3': lambda: self.settings_menu.show(),
            'q': lambda: False
        }
        
        return self.prompt_choice(options, show_back=False)
