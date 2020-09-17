class Planet:
    # class level attributes
    shape = 'round'

    def __init__(self, name, radius, gravity, system):
        # instance attributes
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):
        return f"{self.name} is orbiting in the {self.system}"

    # These class methods are available to the instances and the class itself

    @classmethod
    def commons(cls):
        return f"All planets are {cls.shape} because of gravity"
    # These static methods need to be passed an argument and are available on the instance and the class

    @staticmethod
    def spin(speed='2000 miles per hour'):
        return f'The planet spins and spins a {speed}'
