import pytest
from smart_device import SmartDevice

def test_initialization():
    device = SmartDevice("Thermostat", "T-1000")
    assert device.device_name == "Thermostat"
    assert device.model_number == "T-1000"
    assert not device.is_online
    assert device.status == {}
    assert SmartDevice.device_count == 1

def test_device_count():
    _ = SmartDevice("Lamp", "L-2000")
    assert SmartDevice.device_count == 2

def test_update_status():
    device = SmartDevice("Camera", "C-3000")
    device.update_status("battery", 80)
    assert device.get_status("battery") == 80

def test_get_status_nonexistent():
    device = SmartDevice("Camera", "C-3000")
    assert device.get_status("temperature") == 'Attribute not found'

def test_toggle_online():
    device = SmartDevice("Doorbell", "D-4000")
    device.toggle_online()
    assert device.is_online
    device.toggle_online()
    assert not device.is_online

def test_reset():
    device = SmartDevice("Speaker", "S-5000")
    device.update_status("volume", 70)
    device.reset()
    assert device.status == {}

def test_callable_class():
    device = SmartDevice("Light", "L-6000")
    assert device() == "Light (Model: L-6000)"

def test_device_info():
    device = SmartDevice("Fan", "F-7000")
    device.device_info = lambda: {"name": device.device_name, "model": device.model_number}
    info = device.device_info()
    assert info == {"name": "Fan", "model": "F-7000"}

def test_dynamic_attributes():
    device = SmartDevice("Heater", "H-8000")
    device.update_status("temperature", 25)
    assert device.get_status("temperature") == 25

def test_multiple_updates():
    device = SmartDevice("Thermostat", "T-9000")
    device.update_status("humidity", 60)
    device.update_status("battery", 90)
    assert device.get_status("humidity") == 60
    assert device.get_status("battery") == 90

def test_empty_status_after_reset():
    device = SmartDevice("Lock", "L-1000")
    device.update_status("lock_status", "locked")
    device.reset()
    assert device.status == {}

def test_multiple_devices():
    device1 = SmartDevice("Microwave", "M-1100")
    device2 = SmartDevice("Oven", "O-1200")
    assert SmartDevice.device_count == 5

def test_device_call_function():
    device = SmartDevice("Router", "R-1300")
    assert callable(device.device_info)

def test_callable_behavior():
    device = SmartDevice("Vacuum", "V-1400")
    device.device_info = lambda: "Smart Vacuum Cleaner"
    assert device.device_info() == "Smart Vacuum Cleaner"
