import os
from abc import ABC, abstractmethod
from typing import Callable, Dict, Optional
from rich.console import Console
from rich.panel import Panel
from rich.style import Style

# Centralize console and styles
console = Console()
HEADER_STYLE = Style(color="blue", bold=True)
PROMPT_STYLE = Style(color="green")
ERROR_STYLE = Style(color="red")

class BaseMenu(ABC):
    def __init__(self, parent: Optional['BaseMenu'] = None):
        self.parent = parent
        self.console = console

    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def render_header(self, title: str):
        """Render a stylized header using Rich panel."""
        self.clear_screen()
        self.console.print(Panel(title, style=HEADER_STYLE))

    def prompt_choice(self, options: Dict[str, Callable], show_back: bool = True) -> bool:
        """
        Display options and prompt for choice until valid input received.
        Returns False if user chose to go back, True otherwise.
        """
        if show_back and self.parent is not None:
            options['b'] = lambda: False

        while True:
            choice = self.console.input("[green]Select an option: [/green]").strip().lower()
            
            if choice in options:
                result = options[choice]()
                return True if result is None else result
            
            self.console.print("Invalid choice. Please try again.", style=ERROR_STYLE)

    def prompt_input(self, label: str, validator: Optional[Callable[[str], bool]] = None) -> str:
        """
        Prompt for input with optional validation.
        Returns the validated input string.
        """
        while True:
            value = self.console.input(f"[green]{label}: [/green]").strip()
            
            if validator is None or validator(value):
                return value
            
            self.console.print("Invalid input. Please try again.", style=ERROR_STYLE)

    def show(self) -> bool:
        """
        Display the menu and handle user interaction.
        Returns False if user wants to go back, True otherwise.
        """
        while True:
            self.display()
            if not self.handle_choice():
                return False
            
    @abstractmethod
    def display(self):
        """Display the menu options."""
        pass

    @abstractmethod
    def handle_choice(self) -> bool:
        """
        Handle user choice.
        Returns False if user wants to go back, True otherwise.
        """
        pass
