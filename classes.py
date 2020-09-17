class Planet:

    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):
        return f"{self.name} is orbiting in the {self.system}"

    def desc(self):
        return f"The planet {self.name} has a radius of {self.radius} and is from the systems {self.system} and has a gravity of {self.gravity}."


hoth = Planet('Hoth', 200000, 5.5, 'Hoth System')
print(f"Name is : {hoth.name}")
print(f"Radius is: {hoth.radius}")
print(f"The gravity is: {hoth.gravity}")
print(hoth.orbit())

planetX = Planet('PlanetX', 100000, 5.0, 'X System')

print(planetX.name)
print(planetX.desc())

naboo = Planet('Naboo', 300000, 8.0, 'Naboo System')

print(f"""
Name: {naboo.name}
Radius: {naboo.radius}
Gravity: {naboo.gravity}
{naboo.desc()}
""")
