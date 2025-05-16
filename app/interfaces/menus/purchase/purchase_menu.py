from app.interfaces.menus.base_menu import BaseMenu
from app.models.country_data import COUNTRY_DATA

class PurchaseMenu(BaseMenu):
    def display(self):
        self.header("Purchase Numbers - Select Country")
        for idx, (code, info) in enumerate(COUNTRY_DATA.items(), start=1):
            print(f"{idx}. {info['name']} ({code})")
        print(f"{len(COUNTRY_DATA) + 1}. Other (manual)")

    def get_choice(self):
        return input("Select country option: ")
