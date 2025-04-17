# CLASS IMPLEMENTATIONS
# File: /tests/test_patterns.py

import pytest
from creational_patterns.simple_factory import NetworkDeviceFactory
from creational_patterns.factory_method import AlertFactory
from creational_patterns.abstract_factory import WindowsUIFactory, LinuxUIFactory
from creational_patterns.builder import NetworkConfigBuilder
from creational_patterns.prototype import NetworkTemplate
from creational_patterns.singleton import NetworkMonitor


def test_simple_factory():
    router = NetworkDeviceFactory.create_device("router")
    assert router.operate() == "Routing traffic"
    assert NetworkDeviceFactory.create_device("invalid") is None


def test_factory_method():
    email_processor = AlertFactory.get_processor("email")
    assert email_processor.send_alert("Test") == "Email sent: Test"

    sms_processor = AlertFactory.get_processor("sms")
    assert sms_processor.send_alert("Test") == "SMS sent: Test"

    with pytest.raises(ValueError):
        AlertFactory.get_processor("fax")


def test_abstract_factory():
    win_factory = WindowsUIFactory()
    linux_factory = LinuxUIFactory()

    assert win_factory.create_button().render() == "Windows-style button"
    assert linux_factory.create_button().render() == "Linux-style button"


def test_builder():
    builder = NetworkConfigBuilder()
    config = builder.add_ip("192.168.0.1").add_dns("8.8.8.8").add_firewall_rule("ALLOW ALL").build()

    assert "IP: 192.168.0.1" in str(config)
    assert "DNS: 8.8.8.8" in str(config)
    assert "Rule: ALLOW ALL" in str(config)


def test_prototype():
    template = NetworkTemplate("Base", {"ip": "10.0.0.1"})
    clone = template.clone()

    assert clone is not template
    assert clone.name == "Base"
    assert clone.settings == {"ip": "10.0.0.1"}

    clone.settings["ip"] = "10.0.0.2"
    assert template.settings["ip"] == "10.0.0.1"  # Ensures deep copy


def test_singleton():
    monitor1 = NetworkMonitor()
    monitor2 = NetworkMonitor()

    assert monitor1 is monitor2
    monitor1.status = "Updated"
    assert monitor2.status == "Updated"  # Both point to same instance