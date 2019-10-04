Question author's solution:
class Car:
    """A class that represents a car with a model, a year
       and a speed, plus accelerate and brake methods to
       alter the speed, plus a honk_horn method.
    """
    def __init__(self, model, year, speed=0):
        """Initialiser"""
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        """Speed goes up by 5."""
        self.speed += 5

    def brake(self):
        """Speed goes down by 5"""
        self.speed = max(0, self.speed - 5)

    def honk_horn(self):
        """Print a beep-beep message"""
        print("{} goes 'beep beep'".format(self.model))