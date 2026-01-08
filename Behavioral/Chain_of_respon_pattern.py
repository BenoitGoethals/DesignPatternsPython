from abc import ABC, abstractmethod


# Abstract Handler
class SupportHandler(ABC):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        """Stelt de volgende handler in de keten in"""
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        """Verwerkt het verzoek of geeft het door aan de volgende handler"""
        pass


# Concrete Handlers
class BasicSupportHandler(SupportHandler):
    def handle(self, request):
        if request["priority"] == "laag":
            return f"Basic Support: Probleem '{request['issue']}' is opgelost via FAQ"
        elif self._next_handler:
            return self._next_handler.handle(request)
        return None


class TechnicalSupportHandler(SupportHandler):
    def handle(self, request):
        if request["priority"] == "gemiddeld":
            return f"Technical Support: Probleem '{request['issue']}' wordt opgelost door technisch team"
        elif self._next_handler:
            return self._next_handler.handle(request)
        return None


class ManagerSupportHandler(SupportHandler):
    def handle(self, request):
        if request["priority"] == "hoog":
            return f"Manager Support: Kritiek probleem '{request['issue']}' wordt direct door manager behandeld"
        elif self._next_handler:
            return self._next_handler.handle(request)
        return "Geen geschikte handler gevonden voor dit verzoek"


# Client code
def main():
    # Maak de handlers aan
    basic = BasicSupportHandler()
    technical = TechnicalSupportHandler()
    manager = ManagerSupportHandler()

    # Bouw de keten: basic -> technical -> manager
    basic.set_next(technical).set_next(manager)

    # Test verschillende verzoeken
    requests = [
        {"issue": "Wachtwoord vergeten", "priority": "laag"},
        {"issue": "Software crash", "priority": "gemiddeld"},
        {"issue": "Server down", "priority": "hoog"},
        {"issue": "Vraag over factuur", "priority": "laag"},
    ]

    print("=== Support Ticket Systeem ===\n")
    for req in requests:
        print(f"Verzoek: {req['issue']} (Prioriteit: {req['priority']})")
        result = basic.handle(req)
        print(f"Resultaat: {result}\n")


if __name__ == "__main__":
    main()
