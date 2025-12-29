from abc import ABC, abstractmethod
from typing import List, Protocol, runtime_checkable


@runtime_checkable
class Aircraft(Protocol):
    callsign: str

    def receive_message(self, message: str) -> None:
        ...

    def request_landing(self) -> None:
        ...

    def request_takeoff(self) -> None:
        ...


# Mediator Interface
class AirTrafficControl(Protocol):

    def register_aircraft(self, aircraft: Aircraft):
        pass


    def request_landing(self, aircraft):
        pass


    def request_takeoff(self, aircraft):
        pass


    def send_emergency_alert(self, aircraft, message):
        pass


    def request_runway_status(self, aircraft):
        pass

    def runway_cleared(self, self1):
        pass


# Concrete Mediator
class ControlTower(AirTrafficControl):
    def __init__(self, name: str):
        self.name = name
        self.aircraft: List['Aircraft'] = []
        self.runway_occupied = False
        self.runway_occupied_by = None

    def register_aircraft(self, aircraft):
        self.aircraft.append(aircraft)
        print(f"[{self.name}] ✈️  {aircraft.callsign} geregistreerd bij verkeerstoren")

    def request_landing(self, aircraft):
        print(f"\n[{self.name}] 📻 {aircraft.callsign} vraagt toestemming om te landen")

        if self.runway_occupied:
            print(f"[{self.name}] 🚫 {aircraft.callsign}, landingsbaan bezet door {self.runway_occupied_by.callsign}")
            print(f"[{self.name}] 🔄 {aircraft.callsign}, blijf in wachtpatroon")
            aircraft.receive_message(f"Wacht in de lucht, landingsbaan bezet")
        else:
            self.runway_occupied = True
            self.runway_occupied_by = aircraft
            print(f"[{self.name}] ✅ {aircraft.callsign}, toestemming verleend om te landen op baan 24R")
            aircraft.receive_message(f"Toestemming verleend voor landing")

            # Notificeer andere vliegtuigen
            for other_aircraft in self.aircraft:
                if other_aircraft != aircraft:
                    other_aircraft.receive_message(f"{aircraft.callsign} is aan het landen")

    def request_takeoff(self, aircraft):
        print(f"\n[{self.name}] 📻 {aircraft.callsign} vraagt toestemming om op te stijgen")

        if self.runway_occupied:
            print(
                f"[{self.name}] 🚫 {aircraft.callsign}, wacht. Landingsbaan bezet door {self.runway_occupied_by.callsign}")
            aircraft.receive_message(f"Wacht op taxibaan, landingsbaan bezet")
        else:
            self.runway_occupied = True
            self.runway_occupied_by = aircraft
            print(f"[{self.name}] ✅ {aircraft.callsign}, toestemming verleend om op te stijgen, baan 24R")
            aircraft.receive_message(f"Toestemming verleend voor opstijgen")

            # Notificeer andere vliegtuigen
            for other_aircraft in self.aircraft:
                if other_aircraft != aircraft:
                    other_aircraft.receive_message(f"{aircraft.callsign} is aan het opstijgen")

    def runway_cleared(self, aircraft):
        if self.runway_occupied_by == aircraft:
            self.runway_occupied = False
            self.runway_occupied_by = None
            print(f"[{self.name}] ✓ Landingsbaan vrijgegeven door {aircraft.callsign}")

    def send_emergency_alert(self, aircraft, message):
        print(f"\n[{self.name}] 🚨 NOODMELDING van {aircraft.callsign}: {message}")
        print(f"[{self.name}] 🚨 Alle verkeer wijken! Prioriteit aan {aircraft.callsign}")

        # Bevrijdt de landingsbaan onmiddellijk
        self.runway_occupied = False
        self.runway_occupied_by = aircraft

        # Waarschuw alle andere vliegtuigen
        for other_aircraft in self.aircraft:
            if other_aircraft != aircraft:
                other_aircraft.receive_message(
                    f"NOODMELDING: {aircraft.callsign} - {message}. Blijf weg van landingsbaan!")

        aircraft.receive_message("Prioriteit verleend, direct toestemming voor noodlanding")

    def request_runway_status(self, aircraft):
        status = "bezet" if self.runway_occupied else "vrij"
        occupied_by = f" door {self.runway_occupied_by.callsign}" if self.runway_occupied else ""
        print(f"[{self.name}] 📊 {aircraft.callsign}, landingsbaan is {status}{occupied_by}")
        aircraft.receive_message(f"Landingsbaan status: {status}{occupied_by}")


# Colleague (Abstract)
class Aircraft(ABC):
    def __init__(self, callsign: str, control_tower: AirTrafficControl):
        self.callsign = callsign
        self.control_tower = control_tower
        self.control_tower.register_aircraft(self)

    def receive_message(self, message: str):
        print(f"  [{self.callsign}] 📩 Ontvangen: {message}")

    @abstractmethod
    def request_landing(self):
        pass

    @abstractmethod
    def request_takeoff(self):
        pass


# Concrete Colleagues
class PassengerAircraft(Aircraft):
    def __init__(self, callsign: str, control_tower: AirTrafficControl, passengers: int):
        super().__init__(callsign, control_tower)
        self.passengers = passengers

    def request_landing(self):
        print(f"\n[{self.callsign}] Passagiersvliegtuig met {self.passengers} passagiers vraagt landing aan")
        self.control_tower.request_landing(self)

    def request_takeoff(self):
        print(f"\n[{self.callsign}] Passagiersvliegtuig met {self.passengers} passagiers vraagt opstijgen aan")
        self.control_tower.request_takeoff(self)

    def landing_completed(self):
        print(f"[{self.callsign}] ✓ Landing voltooid, verlaat landingsbaan")
        self.control_tower.runway_cleared(self)

    def takeoff_completed(self):
        print(f"[{self.callsign}] ✓ Opstijgen voltooid, verlaat luchtruim")
        self.control_tower.runway_cleared(self)


class CargoAircraft(Aircraft):
    def __init__(self, callsign: str, control_tower: AirTrafficControl, cargo_weight: float):
        super().__init__(callsign, control_tower)
        self.cargo_weight = cargo_weight

    def request_landing(self):
        print(f"\n[{self.callsign}] Vrachtvliegtuig ({self.cargo_weight} ton) vraagt landing aan")
        self.control_tower.request_landing(self)

    def request_takeoff(self):
        print(f"\n[{self.callsign}] Vrachtvliegtuig ({self.cargo_weight} ton) vraagt opstijgen aan")
        self.control_tower.request_takeoff(self)

    def landing_completed(self):
        print(f"[{self.callsign}] ✓ Landing voltooid, verlaat landingsbaan")
        self.control_tower.runway_cleared(self)

    def declare_emergency(self, message: str):
        print(f"[{self.callsign}] 🚨 NOODGEVAL: {message}")
        self.control_tower.send_emergency_alert(self, message)

    def takeoff_completed(self):
        pass


# Client code
def main():
    print("=" * 60)
    print("🏢 SCHIPHOL VERKEERSTOREN SIMULATOR")
    print("=" * 60)

    # Creëer de mediator (verkeerstoren)
    tower = ControlTower("Schiphol Tower")

    # Creëer vliegtuigen (colleagues)
    kl1234 = PassengerAircraft("KL1234", tower, passengers=180)
    ba567 = PassengerAircraft("BA567", tower, passengers=220)
    cargo1 = CargoAircraft("CX8901", tower, cargo_weight=45.5)

    # Scenario 1: Normale operaties
    print("\n" + "=" * 60)
    print("SCENARIO 1: Normale operaties")
    print("=" * 60)

    kl1234.request_landing()
    ba567.request_landing()  # Moet wachten
    kl1234.landing_completed()

    ba567.request_landing()  # Nu toegestaan
    ba567.landing_completed()

    # Scenario 2: Opstijgen
    print("\n" + "=" * 60)
    print("SCENARIO 2: Opstijgen")
    print("=" * 60)

    cargo1.request_takeoff()
    kl1234.request_takeoff()  # Moet wachten
    cargo1.takeoff_completed()

    kl1234.request_takeoff()
    kl1234.takeoff_completed()

    # Scenario 3: Noodsituatie
    print("\n" + "=" * 60)
    print("SCENARIO 3: Noodsituatie")
    print("=" * 60)

    ba567.request_takeoff()
    cargo1.declare_emergency("Motorstoring, verzoek noodlanding")


if __name__ == "__main__":
    main()