# PROTOTYPE IMPLEMENTATION
# /creational_patterns/prototype.py
import copy

# Prototype class for network templates
class NetworkTemplate:
    def __init__(self, name, settings):
        self.name = name
        self.settings = settings  # dictionary

    def clone(self):
        """
        Returns a deep copy of this template.
        """
        return copy.deepcopy(self)

# Example usage:
# default_template = NetworkTemplate("Base", {"ip": "192.168.1.1"})
# copy1 = default_template.clone()