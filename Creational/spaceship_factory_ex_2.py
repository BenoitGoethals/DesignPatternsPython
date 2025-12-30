from dataclasses import dataclass, field
from typing import Type, Any


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
    name: str = "Falcon9"
    manufacturer: str = "SpaceX"
    max_speed: int = 28000
    max_fuel_capacity: int = 228000
    max_passengers: int = 228
    boms: int = 100


@dataclass
class Starship(SpaceShip):
    name: str = "Starship"
    manufacturer: str = "SpaceX"
    max_speed: int = 25000
    max_fuel_capacity: int = 150000
    max_passengers: int = 100
    crew: int = 100


@dataclass
class Enterprise(SpaceShip):
    name: str = "Enterprise"
    manufacturer: str = "Starfleet"
    max_speed: int = 100000
    max_fuel_capacity: int = 500000
    max_passengers: int = 10000
    drones: int = 100
    flight_control: int = 100


class SpaceshipFactory:
    """A Pythonic factory that supports unique per-instance data."""

    _registry: dict[str, Type[SpaceShip]] = {
        "Falcon9": Falcon9,
        "Starship": Starship,
        "Enterprise": Enterprise
    }

    @classmethod
    def create(cls, spaceship_type: str, **kwargs) -> SpaceShip:
        """
        Creates a spaceship instance.
        Pass keyword arguments to override defaults.
        """
        ship_class = cls._registry.get(spaceship_type)
        if not ship_class:
            raise ValueError(f"Unknown spaceship type: {spaceship_type}")

        # We pass kwargs directly to the class constructor
        return ship_class(**kwargs)


if __name__ == "__main__":
    # Create a default Falcon9
    default_falcon = SpaceshipFactory.create("Falcon9")

    # Create a unique Starship with custom data
    unique_starship = SpaceshipFactory.create(
        "Starship",
        name="Mars Explorer I",
        crew=500,
        max_speed=30000
    )

    print(f"Default: {default_falcon}")
    print(f"Unique:  {unique_starship}")