from datetime import datetime

class Person:
    def __init__(self, first_name, last_name, birth_year, base_salary=0, bonus=0):
        self._first_name = first_name
        self._last_name = last_name
        self._birth_year = birth_year
        self._base_salary = base_salary
        self._bonus = self._validate_bonus(bonus)

    @property
    def current_year(self):
        return datetime.now().year

    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._last_name
    
    @property
    def age(self):
        return self.current_year - self._birth_year

    def set_birth_year(self, year):
        self._birth_year = year

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    @full_name.setter
    def full_name(self, name):
        parts = name.split()
        if len(parts) < 2:
            raise ValueError("Full name must include both first and last name")
        self._first_name = parts[0]
        self._last_name = " ".join(parts[1:])

    def _validate_bonus(self, bonus):
        if not 0 <= bonus <= 100:
            raise ValueError("Bonus percentage must be between 0 and 100")
        return bonus

    @property
    def bonus(self):
        return self._bonus

    @bonus.setter
    def bonus(self, value):
        self._bonus = self._validate_bonus(value)

    @property
    def base_salary(self):
        return self._base_salary

    @base_salary.setter
    def base_salary(self, value):
        if value < 0:
            raise ValueError("Base salary cannot be negative")
        self._base_salary = value

    @property
    def salary(self):
        bonus_amount = self._base_salary * (self._bonus / 100)
        return self._base_salary + bonus_amount 