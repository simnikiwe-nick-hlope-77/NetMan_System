# BUILDER IMPLEMENTATION
# /creational_patterns/builder.py

# Product class that holds the final configuration
class NetworkConfiguration:
    def __init__(self):
        self.config = []

    def __str__(self):
        return "\n".join(self.config)

# Builder class to construct network configurations step by step
class NetworkConfigBuilder:
    def __init__(self):
        self.configuration = NetworkConfiguration()

    def add_ip(self, ip):
        self.configuration.config.append(f"IP: {ip}")
        return self  # allows chaining

    def add_dns(self, dns):
        self.configuration.config.append(f"DNS: {dns}")
        return self

    def add_firewall_rule(self, rule):
        self.configuration.config.append(f"Rule: {rule}")
        return self

    def build(self):
        """
        Final step – returns the fully built configuration.
        """
        return self.configuration
