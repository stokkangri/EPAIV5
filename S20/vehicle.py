class Vehicle:
    # Class-level variable to track vehicle count
    vehicle_count = 0
    
    def __init__(self, vehicle_make, vehicle_model, vehicle_year):
        self._vehicle_make = vehicle_make
        self._vehicle_model = vehicle_model
        self._vehicle_year = vehicle_year
        Vehicle.vehicle_count += 1
    
    @classmethod
    def get_vehicle_count(cls):
        return cls.vehicle_count
    
    @staticmethod
    def classify_vehicle(vehicle_type):
        valid_types = {"car", "truck", "motorcycle"}
        if vehicle_type.lower() not in valid_types:
            raise ValueError(f"Invalid vehicle type. Must be one of: {valid_types}")
        return f"This is a {vehicle_type.lower()}"


class ElectricVehicle(Vehicle):
    def __init__(self, vehicle_make, vehicle_model, vehicle_year):
        super().__init__(vehicle_make, vehicle_model, vehicle_year)
    
    @staticmethod
    def classify_vehicle(vehicle_type):
        valid_types = {"car", "truck", "motorcycle"}
        if vehicle_type.lower() not in valid_types:
            raise ValueError(f"Invalid vehicle type. Must be one of: {valid_types}")
        return f"This is an electric {vehicle_type.lower()}" 