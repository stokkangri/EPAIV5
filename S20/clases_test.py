import pytest
from person import Person
from circle import Circle
from vehicle import Vehicle, ElectricVehicle
from dynamic_class import DynamicClass, ValidatedAttribute

def test_person():
    person = Person('John', 'Doe', 1990)
    assert person.age == 34  # Assuming the current year is 2024
    person.set_birth_year(1985)
    assert person.age == 39
    person.full_name = "Jane Smith"
    assert person.first_name == "Jane"
    assert person.last_name == "Smith"
    person.base_salary = 50000
    person.bonus = 10
    assert person.salary == 55000  # base_salary = 50000, bonus = 10%
    person.base_salary = 60000
    assert person.salary == 66000  # Updated salary

def test_circle():
    circle = Circle(10)
    assert circle.radius == 10
    assert circle.diameter == 20
    assert circle.area == pytest.approx(314.159, 0.001)
    circle.radius = 5
    assert circle.diameter == 10
    assert circle.area == pytest.approx(78.539, 0.001)
    with pytest.raises(ValueError):
        circle.radius = -1  # Should raise an error for negative radius

def test_vehicle():
    vehicle = Vehicle('Toyota', 'Corolla', 2020)
    assert Vehicle.get_vehicle_count() == 1
    assert Vehicle.classify_vehicle("car") == "This is a car"
    ev = ElectricVehicle('Tesla', 'Model S', 2023)
    assert ElectricVehicle.classify_vehicle("car") == "This is an electric car"

def test_dynamic_class():
    dynamic_obj = DynamicClass()
    dynamic_obj.dynamic_attr('name', 'Dynamic Object')
    assert dynamic_obj.name == 'Dynamic Object'

def test_validated_attribute():
    class TestClass:
        value = ValidatedAttribute('value')

    validated_attr = TestClass()
    validated_attr.value = 100
    assert validated_attr.value == 100
    with pytest.raises(ValueError):
           validated_attr.value = -10  # Should raise error for negative value
