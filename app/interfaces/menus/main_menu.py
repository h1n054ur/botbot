from typing import Dict, Callable
from app.interfaces.menus.base_menu import BaseMenu

# Import stubs for sub-menus
class PurchaseMenu(BaseMenu):
    def display(self):
        """Display the purchase menu."""
        self.render_header("📞 Purchase Numbers")
        self.console.print("Select country:")
        self.console.print("1. 🇺🇸 United States")
        self.console.print("2. 🇨🇦 Canada")
        self.console.print("3. 🇬🇧 United Kingdom")
        self.console.print("4. 🇦🇺 Australia")
        self.console.print("5. ✨ Other")

    def handle_choice(self) -> bool:
        """Handle purchase menu choices."""
        options = {
            '1': lambda: self._select_country('US'),
            '2': lambda: self._select_country('CA'),
            '3': lambda: self._select_country('GB'),
            '4': lambda: self._select_country('AU'),
            '5': lambda: self._select_country_manual()
        }
        return self.prompt_choice(options)
        
    def _select_country(self, country_code: str) -> bool:
        # Stub for now - will implement in Phase 3
        self.console.print(f"Selected country: {country_code}")
        return True
        
    def _select_country_manual(self) -> bool:
        # Stub for now - will implement in Phase 3
        country = self.prompt_input("Enter country code (e.g. FR):", 
                                  lambda x: len(x) == 2 and x.isalpha())
        return self._select_country(country.upper())

class ManageMenu(BaseMenu):
    def display(self):
        """Display the manage numbers menu."""
        self.render_header("📟 Manage Numbers")
        self.console.print("Loading active numbers...")  # Stub for now
        self.console.print("\nActive Numbers:")
        self.console.print("1. +1234567890 (Example Number)")
        
    def handle_choice(self) -> bool:
        """Handle manage menu choices."""
        options = {
            '1': lambda: self._manage_number("+1234567890")
        }
        return self.prompt_choice(options)
        
    def _manage_number(self, number: str) -> bool:
        # Stub for now - will implement in Phase 3
        self.console.print(f"\nManaging number: {number}")
        self.console.print("1. 📤 Make a Call")
        self.console.print("2. 💬 Send an SMS")
        self.console.print("3. 📄 View Logs")
        self.console.print("4. ⚙️ Configure Number")
        self.console.print("5. 🗑 Release Number")
        return True  # Stub return

class SettingsMenu(BaseMenu):
    def display(self):
        """Display the settings menu."""
        self.render_header("🧾 Settings & Admin")
        self.console.print("1. 📊 Usage & Billing")
        self.console.print("2. 🔒 Security & Compliance")
        self.console.print("3. 👥 Subaccount Management")
        self.console.print("4. 🛠 Developer Tools")
        self.console.print("5. 📝 Account Logs")
        self.console.print("6. 🔍 Advanced Search")
        self.console.print("7. ⚙️ Configuration Management")
        self.console.print("8. 🔧 Logs & Diagnostics")

    def handle_choice(self) -> bool:
        """Handle settings menu choices."""
        options = {
            '1': lambda: self._show_usage(),
            '2': lambda: self._show_security(),
            '3': lambda: self._show_subaccounts(),
            '4': lambda: self._show_devtools(),
            '5': lambda: self._show_logs(),
            '6': lambda: self._show_search(),
            '7': lambda: self._show_config(),
            '8': lambda: self._show_diagnostics()
        }
        return self.prompt_choice(options)

    def _show_usage(self) -> bool:
        self.console.print("Usage & Billing - Coming in Phase 3")
        return True

    def _show_security(self) -> bool:
        self.console.print("Security & Compliance - Coming in Phase 3")
        return True

    def _show_subaccounts(self) -> bool:
        self.console.print("Subaccount Management - Coming in Phase 3")
        return True

    def _show_devtools(self) -> bool:
        self.console.print("Developer Tools - Coming in Phase 3")
        return True

    def _show_logs(self) -> bool:
        self.console.print("Account Logs - Coming in Phase 3")
        return True

    def _show_search(self) -> bool:
        self.console.print("Advanced Search - Coming in Phase 3")
        return True

    def _show_config(self) -> bool:
        self.console.print("Configuration Management - Coming in Phase 3")
        return True

    def _show_diagnostics(self) -> bool:
        self.console.print("Logs & Diagnostics - Coming in Phase 3")
        return True

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
