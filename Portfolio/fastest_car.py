"""
This program includes the definition of the Car class, with a constructor
that includes the make and top speed of a given car.

Outside of the class definition, the function fastest_car finds the make of
the fastest car in a list of Car objects.
"""

# Car class definition
class Car:
    def __init__(self, make: str, top_speed: int):
        self.make = make
        self.top_speed = top_speed

    def __str__(self):
        return f"Car (make: {self.make}, top speed: {self.top_speed})"


def fastest_car(cars: list):
    # Initialize the first car in the list as the 'fastest'
    fastest = cars[0]

    # Store the whole Car object
    for car in cars:
        if car.top_speed > fastest.top_speed:
            fastest = car

    # Return the make of the fastest car after the loop
    return fastest.make


if __name__ == "__main__":
    car1 = Car("Saab", 195)
    car2 = Car("Lada", 110)
    car3 = Car("Ferrari", 280)
    car4 = Car("Trabant", 85)

    cars = [car1, car2, car3, car4]
    print(fastest_car(cars))