from dataclasses import dataclass
from typing import Callable, Any


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
    """A factory using a registry of Callables to produce unique instances."""
    
    # Registry maps strings to the Class (which is a Callable)
    _registry: dict[str, Callable[..., SpaceShip]] = {
        "Falcon9": Falcon9,
        "Starship": Starship,
        "Enterprise": Enterprise
    }

    @classmethod
    def create(cls, spaceship_type: str, **kwargs: Any) -> SpaceShip:
        """Finds the callable in the registry and invokes it with unique data."""
        creator = cls._registry.get(spaceship_type)
        if not creator:
            raise ValueError(f"Unknown spaceship type: {spaceship_type}")
        
        # Calling the class/callable creates a brand new unique instance
        return creator(**kwargs)


if __name__ == "__main__":
    # Create a unique Starship instance with custom data
    my_starship = SpaceshipFactory.create(
        "Starship", 
        name="Starship SN15", 
        crew=12, 
        max_speed=26000
    )
    
    # Create another Starship with different data
    another_starship = SpaceshipFactory.create(
        "Starship", 
        name="Mars Colony Transporter", 
        crew=100
    )

    print(my_starship)
    print(another_starship)
    print(f"Are they the same instance? {my_starship is another_starship}")
