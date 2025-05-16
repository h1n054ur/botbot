import os
from abc import ABC, abstractmethod

class BaseMenu(ABC):
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def header(self, title: str):
        self.clear()
        print(f"=== {title} ===")

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def get_choice(self):
        pass
