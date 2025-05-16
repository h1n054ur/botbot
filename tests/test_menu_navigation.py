"""Basic smoke tests for menu navigation."""
import pytest
from app.interfaces.menus.main_menu import MainMenu, PurchaseMenu, ManageMenu, SettingsMenu

def test_main_menu_creation():
    """Test that MainMenu creates with proper sub-menus."""
    menu = MainMenu()
    assert isinstance(menu.purchase_menu, PurchaseMenu)
    assert isinstance(menu.manage_menu, ManageMenu)
    assert isinstance(menu.settings_menu, SettingsMenu)
    assert menu.parent is None

def test_submenu_parent_links():
    """Test that sub-menus are properly linked to parent."""
    menu = MainMenu()
    assert menu.purchase_menu.parent == menu
    assert menu.manage_menu.parent == menu
    assert menu.settings_menu.parent == menu

def test_purchase_menu_country_validation():
    """Test country code validation in purchase menu."""
    menu = PurchaseMenu(None)
    # Mock user input for testing
    def mock_input(prompt: str) -> str:
        return "FR"
    menu.console.input = mock_input
    assert menu._select_country_manual() is True