# SINGLETON IMPLEMENTATION
# /creational_patterns/singleton.py

# Singleton class for centralized network monitoring
class NetworkMonitor:
    _instance = None

    def __new__(cls):
        # Ensure only one instance ever exists
        if cls._instance is None:
            cls._instance = super(NetworkMonitor, cls).__new__(cls)
            cls._instance.status = "Initialized"
        return cls._instance

# Usage:
# monitor1 = NetworkMonitor()
# monitor2 = NetworkMonitor()
# assert monitor1 is monitor2  # True
