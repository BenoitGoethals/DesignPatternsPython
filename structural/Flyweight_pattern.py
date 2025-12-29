class CharacterFlyweight:
    def __init__(self, char, font, size):
        self.char = char      # intrinsic
        self.font = font      # intrinsic
        self.size = size      # intrinsic

    def render(self, position):
        print(f"{self.char} op {position}")


class CharacterFactory:
    _cache = {}

    @classmethod
    def get_character(cls, char, font, size):
        key = (char, font, size)
        if key not in cls._cache:
            cls._cache[key] = CharacterFlyweight(char, font, size)
        return cls._cache[key]


text = "HELLO"

for i, letter in enumerate(text):
    char = CharacterFactory.get_character(letter, "Arial", 12)
    char.render(position=i)


class VehicleType:
    def __init__(self, name, icon_path, max_payload):
        self.name = name
        self.icon_path = icon_path
        self.max_payload = max_payload


class VehicleFactory:
    _types = {}

    @classmethod
    def get_vehicle_type(cls, name):
        if name not in cls._types:
            cls._types[name] = VehicleType(
                name=name,
                icon_path=f"{name}.png",
                max_payload=5000
            )
        return cls._types[name]
class Vehicle:
    def __init__(self, vehicle_type, position, fuel):
        self.vehicle_type = vehicle_type
        self.position = position
        self.fuel = fuel

    def display(self):
        print(f"{self.vehicle_type.name} @ {self.position} | fuel={self.fuel}")


vehicles = []
vehicles.append(Vehicle(VehicleFactory.get_vehicle_type("Truck"), "A1", 80))
vehicles.append(Vehicle(VehicleFactory.get_vehicle_type("Truck"), "B2", 60))
vehicles.append(Vehicle(VehicleFactory.get_vehicle_type("Tank"), "C3", 40))

for v in vehicles:
    v.display()
