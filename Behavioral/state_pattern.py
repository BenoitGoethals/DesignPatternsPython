from typing import Protocol


# State Protocol
class VendingMachineState(Protocol):
    def insert_money(self, machine: 'VendingMachine', amount: int) -> None:
        ...

    def select_product(self, machine: 'VendingMachine', product: str) -> None:
        ...

    def dispense(self, machine: 'VendingMachine') -> None:
        ...

    def cancel(self, machine: 'VendingMachine') -> None:
        ...


# Context - de Frisdrankenautomaat
class VendingMachine:
    def __init__(self):
        self.balance = 0
        self.selected_product = None
        self.inventory = {
            "Cola": {"price": 250, "stock": 5},
            "Water": {"price": 150, "stock": 3},
            "Sap": {"price": 200, "stock": 0}  # Uitverkocht
        }
        # Start in NoMoney state
        self._state: VendingMachineState = NoMoneyState()
        print("🤖 Frisdrankenautomaat gestart")
        self._show_inventory()

    def set_state(self, state: VendingMachineState) -> None:
        """Wijzig de huidige state"""
        self._state = state

    def insert_money(self, amount: int) -> None:
        """Geld invoeren"""
        print(f"\n💰 {amount} cent ingevoerd")
        self._state.insert_money(self, amount)

    def select_product(self, product: str) -> None:
        """Product selecteren"""
        print(f"\n🥤 Product geselecteerd: {product}")
        self._state.select_product(self, product)

    def dispense(self) -> None:
        """Product uitgeven"""
        print(f"\n📦 Dispense knop ingedrukt")
        self._state.dispense(self)

    def cancel(self) -> None:
        """Transactie annuleren"""
        print(f"\n❌ Cancel knop ingedrukt")
        self._state.cancel(self)

    def return_money(self) -> None:
        """Geef geld terug"""
        if self.balance > 0:
            print(f"💵 {self.balance} cent teruggestort")
            self.balance = 0

    def _show_inventory(self) -> None:
        """Toon beschikbare producten"""
        print("\n📋 Beschikbare producten:")
        for product, info in self.inventory.items():
            status = f"{info['stock']} stuks" if info['stock'] > 0 else "UITVERKOCHT"
            print(f"   • {product}: {info['price']} cent ({status})")


# Concrete State 1: Geen geld ingevoerd
class NoMoneyState:
    def insert_money(self, machine: VendingMachine, amount: int) -> None:
        machine.balance += amount
        print(f"✓ Saldo: {machine.balance} cent")
        machine.set_state(HasMoneyState())

    def select_product(self, machine: VendingMachine, product: str) -> None:
        print("✗ Voer eerst geld in!")

    def dispense(self, machine: VendingMachine) -> None:
        print("✗ Voer eerst geld in!")

    def cancel(self, machine: VendingMachine) -> None:
        print("✗ Geen actieve transactie om te annuleren")


# Concrete State 2: Geld ingevoerd
class HasMoneyState:
    def insert_money(self, machine: VendingMachine, amount: int) -> None:
        machine.balance += amount
        print(f"✓ Saldo verhoogd naar: {machine.balance} cent")

    def select_product(self, machine: VendingMachine, product: str) -> None:
        if product not in machine.inventory:
            print(f"✗ Product '{product}' bestaat niet")
            return

        product_info = machine.inventory[product]

        if product_info["stock"] == 0:
            print(f"✗ {product} is uitverkocht")
            machine.set_state(OutOfStockState())
            return

        if machine.balance < product_info["price"]:
            shortage = product_info["price"] - machine.balance
            print(f"✗ Onvoldoende saldo. Nog {shortage} cent nodig")
            return

        machine.selected_product = product
        print(f"✓ {product} geselecteerd (prijs: {product_info['price']} cent)")
        machine.set_state(ProductSelectedState())

    def dispense(self, machine: VendingMachine) -> None:
        print("✗ Selecteer eerst een product")

    def cancel(self, machine: VendingMachine) -> None:
        print("✓ Transactie geannuleerd")
        machine.return_money()
        machine.set_state(NoMoneyState())


# Concrete State 3: Product geselecteerd
class ProductSelectedState:
    def insert_money(self, machine: VendingMachine, amount: int) -> None:
        machine.balance += amount
        print(f"✓ Extra geld toegevoegd. Nieuw saldo: {machine.balance} cent")

    def select_product(self, machine: VendingMachine, product: str) -> None:
        print(f"✗ Product al geselecteerd: {machine.selected_product}")
        print("   Druk op dispense of cancel")

    def dispense(self, machine: VendingMachine) -> None:
        product = machine.selected_product
        product_info = machine.inventory[product]

        print(f"🎁 {product} wordt uitgegeven...")

        # Verminder voorraad
        machine.inventory[product]["stock"] -= 1

        # Bereken wisselgeld
        change = machine.balance - product_info["price"]
        machine.balance = 0

        if change > 0:
            print(f"💵 Wisselgeld: {change} cent")

        print(f"✓ Geniet van je {product}!")

        machine.selected_product = None
        machine.set_state(NoMoneyState())

    def cancel(self, machine: VendingMachine) -> None:
        print(f"✓ Selectie geannuleerd: {machine.selected_product}")
        machine.selected_product = None
        machine.set_state(HasMoneyState())


# Concrete State 4: Uitverkocht
class OutOfStockState:
    def insert_money(self, machine: VendingMachine, amount: int) -> None:
        machine.balance += amount
        print(f"✓ Geld toegevoegd, maar geselecteerd product is uitverkocht")
        print("   Selecteer een ander product of annuleer")

    def select_product(self, machine: VendingMachine, product: str) -> None:
        if product not in machine.inventory:
            print(f"✗ Product '{product}' bestaat niet")
            return

        product_info = machine.inventory[product]

        if product_info["stock"] == 0:
            print(f"✗ {product} is ook uitverkocht")
            return

        if machine.balance < product_info["price"]:
            shortage = product_info["price"] - machine.balance
            print(f"✗ Onvoldoende saldo. Nog {shortage} cent nodig")
            machine.set_state(HasMoneyState())
            return

        machine.selected_product = product
        print(f"✓ {product} geselecteerd")
        machine.set_state(ProductSelectedState())

    def dispense(self, machine: VendingMachine) -> None:
        print("✗ Geselecteerd product is uitverkocht")

    def cancel(self, machine: VendingMachine) -> None:
        print("✓ Transactie geannuleerd")
        machine.return_money()
        machine.set_state(NoMoneyState())


# Gebruik
if __name__ == "__main__":
    machine = VendingMachine()

    print("\n" + "=" * 50)
    print("SCENARIO 1: Normale aankoop")
    print("=" * 50)
    machine.insert_money(300)
    machine.select_product("Cola")
    machine.dispense()

    print("\n" + "=" * 50)
    print("SCENARIO 2: Onvoldoende geld")
    print("=" * 50)
    machine.insert_money(100)
    machine.select_product("Cola")
    machine.insert_money(200)
    machine.select_product("Cola")
    machine.dispense()

    print("\n" + "=" * 50)
    print("SCENARIO 3: Transactie annuleren")
    print("=" * 50)
    machine.insert_money(200)
    machine.select_product("Water")
    machine.cancel()

    print("\n" + "=" * 50)
    print("SCENARIO 4: Uitverkocht product")
    print("=" * 50)
    machine.insert_money(300)
    machine.select_product("Sap")
    machine.select_product("Water")
    machine.dispense()

    print("\n" + "=" * 50)
    print("SCENARIO 5: Foutieve acties")
    print("=" * 50)
    machine.select_product("Cola")
    machine.dispense()
    machine.cancel()