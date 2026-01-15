from abc import ABC, abstractmethod
from typing import List


# Component: Basis interface voor alle werknemers
class Employee(ABC):
    def __init__(self, name: str, position: str, salary: float):
        self.name = name
        self.position = position
        self.salary = salary

    @abstractmethod
    def show_details(self, indent: int = 0) -> None:
        """Toon informatie over de werknemer"""
        pass

    @abstractmethod
    def get_total_salary(self) -> float:
        """Bereken totale salaris (inclusief ondergeschikten)"""
        pass

    @abstractmethod
    def count_employees(self) -> int:
        """Tel aantal werknemers"""
        pass


# Leaf: Een individuele werknemer zonder ondergeschikten
class IndividualEmployee(Employee):
    def show_details(self, indent: int = 0) -> None:
        prefix = "  " * indent
        print(f"{prefix}👤 {self.name} - {self.position} (€{self.salary:,.2f})")

    def get_total_salary(self) -> float:
        return self.salary

    def count_employees(self) -> int:
        return 1


# Composite: Een manager met ondergeschikten
class Manager(Employee):
    def __init__(self, name: str, position: str, salary: float):
        super().__init__(name, position, salary)
        self.subordinates: List[Employee] = []

    def add_subordinate(self, employee: Employee) -> None:
        """Voeg een ondergeschikte toe"""
        self.subordinates.append(employee)

    def remove_subordinate(self, employee: Employee) -> None:
        """Verwijder een ondergeschikte"""
        self.subordinates.remove(employee)

    def show_details(self, indent: int = 0) -> None:
        prefix = "  " * indent
        print(f"{prefix}👔 {self.name} - {self.position} (€{self.salary:,.2f})")

        if self.subordinates:
            print(f"{prefix}   ├─ Team:")
            for subordinate in self.subordinates:
                subordinate.show_details(indent + 2)

    def get_total_salary(self) -> float:
        """Bereken totale salaris inclusief alle ondergeschikten"""
        total = self.salary
        for subordinate in self.subordinates:
            total += subordinate.get_total_salary()
        return total

    def count_employees(self) -> int:
        """Tel deze manager plus alle ondergeschikten"""
        count = 1  # Tel deze manager
        for subordinate in self.subordinates:
            count += subordinate.count_employees()
        return count


# Voorbeeld gebruik
if __name__ == "__main__":
    # Maak individuele werknemers
    dev1 = IndividualEmployee("Anna de Vries", "Senior Developer", 65000)
    dev2 = IndividualEmployee("Pieter Jansen", "Junior Developer", 45000)
    dev3 = IndividualEmployee("Lisa van Dam", "Developer", 55000)

    designer1 = IndividualEmployee("Tom Bakker", "UI Designer", 50000)
    designer2 = IndividualEmployee("Emma Visser", "UX Designer", 52000)

    tester1 = IndividualEmployee("Jan Smit", "QA Tester", 48000)

    hr1 = IndividualEmployee("Sophie Peters", "HR Specialist", 46000)
    hr2 = IndividualEmployee("Mark de Jong", "Recruiter", 44000)

    # Maak managers
    dev_manager = Manager("Klaas Mulder", "Development Manager", 80000)
    design_manager = Manager("Sarah Groot", "Design Manager", 75000)
    hr_manager = Manager("Hans Vos", "HR Manager", 70000)

    cto = Manager("Robert Hendriks", "CTO", 120000)
    ceo = Manager("Maria van Dijk", "CEO", 150000)

    # Bouw de organisatiestructuur
    # Development team
    dev_manager.add_subordinate(dev1)
    dev_manager.add_subordinate(dev2)
    dev_manager.add_subordinate(dev3)
    dev_manager.add_subordinate(tester1)

    # Design team
    design_manager.add_subordinate(designer1)
    design_manager.add_subordinate(designer2)

    # HR team
    hr_manager.add_subordinate(hr1)
    hr_manager.add_subordinate(hr2)

    # CTO overziet development en design
    cto.add_subordinate(dev_manager)
    cto.add_subordinate(design_manager)

    # CEO is de top
    ceo.add_subordinate(cto)
    ceo.add_subordinate(hr_manager)

    # Toon organisatiestructuur
    print("=== ORGANISATIESTRUCTUUR ===\n")
    ceo.show_details()

    # Statistieken
    print("\n=== STATISTIEKEN ===")
    print(f"Totaal aantal werknemers: {ceo.count_employees()}")
    print(f"Totale salariskosten: €{ceo.get_total_salary():,.2f}")

    print(f"\nDevelopment afdeling:")
    print(f"  Werknemers: {dev_manager.count_employees()}")
    print(f"  Salariskosten: €{dev_manager.get_total_salary():,.2f}")

    print(f"\nTechnologie divisie (CTO):")
    print(f"  Werknemers: {cto.count_employees()}")
    print(f"  Salariskosten: €{cto.get_total_salary():,.2f}")

    # Demonstreer uniforme behandeling
    print("\n=== UNIFORME BEHANDELING ===")
    employees = [dev1, dev_manager, cto]
    for emp in employees:
        print(
            f"{emp.name}: verantwoordelijk voor {emp.count_employees()} personen, "
            f"salariskosten: €{emp.get_total_salary():,.2f}"
        )
