# ABSTRACT FACTORY IMPLEMENTATION
# /creational_patterns/abstract_factory.py

from abc import ABC, abstractmethod

# Abstract Button interface
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

# Windows-style button
class WindowsButton(Button):
    def render(self):
        return "Windows-style button"

# Linux-style button
class LinuxButton(Button):
    def render(self):
        return "Linux-style button"

# Abstract UI Factory
class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

# Factory for Windows UI
class WindowsUIFactory(UIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

# Factory for Linux UI
class LinuxUIFactory(UIFactory):
    def create_button(self) -> Button:
        return LinuxButton()