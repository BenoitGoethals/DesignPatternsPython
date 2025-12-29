from abc import ABC, abstractmethod
from typing import Dict, List


# Data object dat door de keten gaat
class UserData:
    def __init__(self, data: Dict):
        self.data = data
        self.errors = []
        self.is_valid = True

    def add_error(self, error: str):
        self.errors.append(error)
        self.is_valid = False

    def __str__(self):
        return f"Data: {self.data}, Valid: {self.is_valid}, Errors: {self.errors}"


# Abstract Handler
class DataHandler(ABC):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        """Stelt de volgende handler in de keten in"""
        self._next_handler = handler
        return handler

    def handle(self, user_data: UserData) -> UserData:
        """Voert de verwerking uit en geeft door aan volgende handler"""
        # Voer eigen verwerking uit
        self.process(user_data)

        # Geef door aan volgende handler indien aanwezig
        if self._next_handler:
            return self._next_handler.handle(user_data)

        return user_data

    @abstractmethod
    def process(self, user_data: UserData):
        """Voert de specifieke verwerking uit"""
        pass


# Validatie Handlers
class EmailValidationHandler(DataHandler):
    def process(self, user_data: UserData):
        email = user_data.data.get('email', '')
        if '@' not in email or '.' not in email:
            user_data.add_error("Ongeldig email adres")
        print(f"✓ Email validatie uitgevoerd")


class AgeValidationHandler(DataHandler):
    def process(self, user_data: UserData):
        age = user_data.data.get('age', 0)
        if age < 18:
            user_data.add_error("Gebruiker moet minimaal 18 jaar zijn")
        elif age > 120:
            user_data.add_error("Leeftijd is niet realistisch")
        print(f"✓ Leeftijd validatie uitgevoerd")


# Transformatie Handlers
class NameNormalizationHandler(DataHandler):
    def process(self, user_data: UserData):
        if 'name' in user_data.data:
            # Transformeer naam naar Title Case
            user_data.data['name'] = user_data.data['name'].strip().title()
            print(f"✓ Naam genormaliseerd naar: {user_data.data['name']}")


class EmailNormalizationHandler(DataHandler):
    def process(self, user_data: UserData):
        if 'email' in user_data.data:
            # Transformeer email naar lowercase
            user_data.data['email'] = user_data.data['email'].strip().lower()
            print(f"✓ Email genormaliseerd naar: {user_data.data['email']}")


class DataEnrichmentHandler(DataHandler):
    def process(self, user_data: UserData):
        # Voeg extra informatie toe
        age = user_data.data.get('age', 0)
        if age >= 18:
            user_data.data['category'] = 'volwassene'
        else:
            user_data.data['category'] = 'minderjarige'

        user_data.data['processed'] = True
        print(f"✓ Data verrijkt met category: {user_data.data['category']}")


# Client code
def main():
    # Bouw de verwerkingsketen
    chain = EmailValidationHandler()
    chain.set_next(AgeValidationHandler()) \
        .set_next(NameNormalizationHandler()) \
        .set_next(EmailNormalizationHandler()) \
        .set_next(DataEnrichmentHandler())

    # Test verschillende gebruikers
    test_users = [
        {'name': 'jan de vries', 'email': 'JAN@EXAMPLE.COM', 'age': 25},
        {'name': 'MARIA JANSEN', 'email': 'maria.example.com', 'age': 30},
        {'name': 'piet bakker', 'email': 'piet@test.nl', 'age': 15}
    ]

    print("=== Data Verwerkingsketen ===\n")

    for i, user_dict in enumerate(test_users, 1):
        print(f"--- Gebruiker {i} ---")
        print(f"Originele data: {user_dict}")

        user_data = UserData(user_dict.copy())
        result = chain.handle(user_data)

        print(f"\nResultaat:")
        print(f"  Getransformeerde data: {result.data}")
        print(f"  Status: {'✓ Geldig' if result.is_valid else '✗ Ongeldig'}")
        if result.errors:
            print(f"  Fouten: {', '.join(result.errors)}")
        print()


if __name__ == "__main__":
    main()