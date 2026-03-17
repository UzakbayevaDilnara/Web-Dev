class Vehicle:
    def __init__(self, brand, year, speed):
        self.brand = brand
        self.year = year
        self.speed = speed

    def move(self):
        return f"{self.brand} is moving at {self.speed} km/h"

    def stop(self):
        return f"{self.brand} has stopped"

    def __str__(self):
        return f"Vehicle: {self.brand}, Year: {self.year}, Speed: {self.speed}"


class Car(Vehicle):
    def __init__(self, brand, year, speed, doors):
        super().__init__(brand, year, speed)
        self.doors = doors

    def move(self):  # override
        return f"Car {self.brand} is driving smoothly at {self.speed} km/h"

    def open_trunk(self):
        return f"{self.brand} trunk is open"


class Bike(Vehicle):
    def __init__(self, brand, year, speed, type_bike):
        super().__init__(brand, year, speed)
        self.type_bike = type_bike

    def move(self):  # override
        return f"Bike {self.brand} is riding at {self.speed} km/h"

    def do_trick(self):
        return f"{self.brand} is doing a trick!"
