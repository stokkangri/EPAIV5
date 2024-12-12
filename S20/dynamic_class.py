class ValidatedAttribute:
    def __init__(self,name):
        self.name = f"_{name}"  # Private name to store the value
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self.name, None)
    
    def __set__(self, instance, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Value must be a positive integer")
        setattr(instance, self.name, value)


class DynamicClass:
    # Class-level variable
    static_value = 100
    
    # Using the descriptor for validation
    validated_number = ValidatedAttribute('validated_number')
    
    def __init__(self, **kwargs):
        # Dynamically set initial attributes from kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def dynamic_attr(self, key, value):
        """
        Dynamically add or update attributes at runtime
        """
        setattr(self, key, value)
        return self
    
    def __str__(self):
        # Custom string representation showing all instance attributes
        attrs = ', '.join(f"{k}={v}" for k, v in self.__dict__.items())
        return f"DynamicClass({attrs})" 