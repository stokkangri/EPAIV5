'''
Create a class named SmartDevice that mimics the behavior of a smart device with the following functionalities:

Initialization:
The class should have an initializer (__init__) that accepts:
device_name (string)
model_number (string)
is_online (boolean, default is False)
The class should also have a class attribute device_count which keeps track of the total number of devices created
Attributes:
SmartDevice should have the following attributes:
device_name: The name of the device
model_number: The model number of the device
is_online: A boolean indicating if the device is currently online
status: A dictionary that stores the current status of various device features (e.g., battery level, temperature)
Methods:
update_status(attribute, value): Adds or updates a status attribute in the status dictionary
get_status(attribute): Returns the value of a specific status attribute. If the attribute does not exist, it should return 'Attribute not found'. 
toggle_online(): Changes the device's online status (is_online) to its opposite value
reset():L Resets all status attributes to their default values (i.e. clears the status dictionary)
Callable Class:
Make the SmartDevice class callable, such that calling an instance returns its device_name and model_number in a formatting string
Function Attributes:
Add a callable function attribute to the class named device_info which returns the current state of the device as a dictionary
Submission Requirements: 

Create a Python file smart_device.py Download smart_device.pythat contains the implementation of the SmartDevice class. 
Use the provided test_smart_device.py file to validate your code
Use GitHub actions to automatically run tests whenever you push your code. The GitHub Actions workflow file is also provided Download provided. 
Once you've passed all the tests, please share your GitHub Actions Link with us along with a screenshot (especially if you are clearing the tests on your desktop, then screenshot and GitHub code link)!


'''

class SmartDevice:
    device_count = 0

    def __init__(self, device_name, model_number, is_online=False):
        self.device_name = device_name
        self.model_number = model_number
        self.is_online = is_online
        self.status = {}
        SmartDevice.device_count += 1

    def update_status(self, attribute, value):
        self.status[attribute] = value

    def get_status(self, attribute):
        return self.status.get(attribute, 'Attribute not found')

    def toggle_online(self):
        self.is_online = not self.is_online

    def reset(self):
        self.status = {}

    def __call__(self):
        return f'{self.device_name} {self.model_number}'

    @property
    def device_info(self):
        return {
            'device_name': self.device_name,
            'model_number': self.model_number,
            'is_online': self.is_online,
            'status': self.status
        }