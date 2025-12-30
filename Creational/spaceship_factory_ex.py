from dataclasses import dataclass
from typing import Protocol


@dataclass
class SpaceShip:
    """Base class for spaceships."""
    name: str
    manufacturer: str
    max_speed: int
    max_fuel_capacity: int
    max_passengers: int
    position: tuple[int, int] = (0, 0)


@dataclass
class Falcon9(SpaceShip):
    def __init__(self):
        super().__init__(name="Falcon9", manufacturer="SpaceX", max_speed=28000, max_fuel_capacity=228000, max_passengers=228)

    boms: int = 100


class Starship(SpaceShip):
    def __init__(self):
        super().__init__(name="Starship", manufacturer="SpaceX", max_speed=25000, max_fuel_capacity=150000, max_passengers=100)

    crew: int = 100


class Enterprise(SpaceShip):
    def __init__(self):
        super().__init__(name="Enterprise", manufacturer="Starfleet", max_speed=100000, max_fuel_capacity=500000, max_passengers=10000)

    drones: int = 100
    flight_control: int = 100




class ISpaceshipFactory(Protocol):
    def create_spaceship(self)->SpaceShip:
        ...

class Falcon9Factory(ISpaceshipFactory):
    """Factory class for creating Falcon9 spaceships."""
    def create_spaceship(self):
        return Falcon9()

class StarshipFactory(ISpaceshipFactory):
    """Factory class for creating Starship spaceships."""
    def create_spaceship(self):
        return Starship()


class EnterpriseFactory(ISpaceshipFactory):
    """Factory class for creating Enterprise spaceships."""
    def create_spaceship(self):
        return Enterprise()


class SpaceshipFactory:
    _factories = {
        "Falcon9": Falcon9Factory(),
        "Starship": StarshipFactory(),
        "Enterprise": EnterpriseFactory()
    }

    def __new__(cls, spaceship_type: str):
        return cls._factories[spaceship_type].create_spaceship()


if __name__ == "__main__":
    spaceship = SpaceshipFactory("Falcon9")
    print(spaceship)