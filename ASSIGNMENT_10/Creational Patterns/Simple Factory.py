# SIMPLE FACTORY IMPLEMENTATION
# /creational_patterns/simple_factory.py

class NetworkDevice:
    def operate(self):
        pass

class Router(NetworkDevice):
    def operate(self):
        return "Routing traffic"

class Switch(NetworkDevice):
    def operate(self):
        return "Switching packets"

class Firewall(NetworkDevice):
    def operate(self):
        return "Filtering traffic"

class NetworkDeviceFactory:
    @staticmethod
    def create_device(device_type: str) -> NetworkDevice:
        devices = {
            "router": Router(),
            "switch": Switch(),
            "firewall": Firewall()
        }
        return devices.get(device_type.lower(), None)