from dataclasses import dataclass
from typing import Any, Callable, Dict, Protocol


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
    def __init__(self, **kwargs):
        defaults = {
            "name": "Falcon9",
            "manufacturer": "SpaceX",
            "max_speed": 28000,
            "max_fuel_capacity": 228000,
            "max_passengers": 228,
        }
        super().__init__(**(defaults | kwargs))

    boms: int = 100


@dataclass
class Starship(SpaceShip):
    def __init__(self, **kwargs):
        defaults = {
            "name": "Starship",
            "manufacturer": "SpaceX",
            "max_speed": 25000,
            "max_fuel_capacity": 150000,
            "max_passengers": 100,
        }
        super().__init__(**(defaults | kwargs))

    crew: int = 100


@dataclass
class Enterprise(SpaceShip):
    def __init__(self, **kwargs):
        defaults = {
            "name": "Enterprise",
            "manufacturer": "Starfleet",
            "max_speed": 100000,
            "max_fuel_capacity": 500000,
            "max_passengers": 10000,
        }
        super().__init__(**(defaults | kwargs))

    drones: int = 100


class ISpaceshipFactory(Protocol):
    def create_spaceship(self, **kwargs) -> SpaceShip: ...


class Falcon9Factory:
    def create_spaceship(self, **kwargs) -> SpaceShip:
        return Falcon9(**kwargs)


class StarshipFactory:
    def create_spaceship(self, **kwargs) -> SpaceShip:
        return Starship(**kwargs)


class EnterpriseFactory:
    def create_spaceship(self, **kwargs) -> SpaceShip:
        return Enterprise(**kwargs)


class SpaceshipFactory:
    """
    Refactored Factory that uses a registry of callables.
    The 'callables' here are the create_spaceship methods of the individual factories.
    """

    # We store the bound methods (callables) in the registry
    _creators: Dict[str, Callable[..., SpaceShip]] = {
        "Falcon9": Falcon9Factory().create_spaceship,
        "Starship": StarshipFactory().create_spaceship,
        "Enterprise": EnterpriseFactory().create_spaceship,
    }

    @classmethod
    def create(cls, spaceship_type: str, **kwargs: Any) -> SpaceShip:
        """Finds the registered callable and executes it."""
        creator = cls._creators.get(spaceship_type)
        if not creator:
            raise ValueError(f"Unknown spaceship type: {spaceship_type}")

        return creator(**kwargs)


if __name__ == "__main__":
    # The client uses the main factory, which delegates to the specific registered callables
    ship1 = SpaceshipFactory.create("Falcon9", boms=200)
    ship2 = SpaceshipFactory.create("Starship", crew=50)

    print(ship1)
    print(ship2)
