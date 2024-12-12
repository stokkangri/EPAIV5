import math

class Circle:
    def __init__(self, radius):
        self._radius = None  # Initialize to None for initial validation
        self._cached_area = None  # Cache for area calculation
        self.radius = radius  # Use the setter for validation
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
        self._cached_area = None  # Invalidate cached area
    
    def set_radius(self, value):
        """Alternative method to set radius"""
        self.radius = value  # Uses the property setter
    
    @property
    def diameter(self):
        return 2 * self._radius
    
    @property
    def area(self):
        # Calculate area only if not cached or radius has changed
        if self._cached_area is None:
            self._cached_area = math.pi * self._radius ** 2
        return self._cached_area 