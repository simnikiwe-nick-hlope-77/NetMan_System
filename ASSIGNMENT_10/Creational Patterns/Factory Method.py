# FACTORY METHOD IMPLEMENTATION
# /creational_patterns/factory_method.py

from abc import ABC, abstractmethod

# Abstract class for alert processors
class AlertProcessor(ABC):
    @abstractmethod
    def send_alert(self, message: str) -> str:
        pass

# Email-based alert
class EmailAlertProcessor(AlertProcessor):
    def send_alert(self, message: str) -> str:
        return f"Email sent: {message}"

# SMS-based alert
class SMSAlertProcessor(AlertProcessor):
    def send_alert(self, message: str) -> str:
        return f"SMS sent: {message}"

# Factory to get the right alert processor
class AlertFactory:
    @staticmethod
    def get_processor(method: str) -> AlertProcessor:
        """
        Factory method that returns an alert processor based on the given method.
        """
        if method == "email":
            return EmailAlertProcessor()
        elif method == "sms":
            return SMSAlertProcessor()
        raise ValueError("Unsupported alert method")