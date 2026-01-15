import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from typing import List, Protocol


# Target: De klasse die de client verwacht
class Product:
    """Product klasse - het doel formaat"""

    def __init__(self, id: int, name: str, price: float, category: str):
        self.id = id
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"Product(id={self.id}, name='{self.name}', price=€{self.price:.2f}, category='{self.category}')"

    def __repr__(self):
        return self.__str__()


# Interface voor data providers
class DataProvider(Protocol):
    """Abstract interface voor verschillende data bronnen"""

    @abstractmethod
    def get_products(self) -> List[Product]:
        """Haal producten op als een lijst van Product objecten"""
        pass


# Adaptee 1: XML Parser
class XMLDataSource:
    """Bestaande XML data bron die niet compatibel is met onze interface"""

    def __init__(self, xml_string: str):
        self.xml_string = xml_string

    def parse_xml(self):
        """Parse XML en retourneer raw XML elementen"""
        root = ET.fromstring(self.xml_string)
        return root.findall("product")


# Adapter 1: XML naar Product lijst
class XMLAdapter(DataProvider):
    """Adapter die XML data converteert naar Product objecten"""

    def __init__(self, xml_data_source: XMLDataSource):
        self.xml_data_source = xml_data_source

    def get_products(self) -> List[Product]:
        """Converteer XML elementen naar Product objecten"""
        products = []
        xml_products = self.xml_data_source.parse_xml()

        for xml_product in xml_products:
            product = Product(
                id=int(xml_product.find("id").text),
                name=xml_product.find("name").text,
                price=float(xml_product.find("price").text),
                category=xml_product.find("category").text,
            )
            products.append(product)

        return products


# Adaptee 2: JSON Parser
class JSONDataSource:
    """Bestaande JSON data bron met een ander formaat"""

    def __init__(self, json_string: str):
        self.json_string = json_string

    def get_json_data(self):
        """Parse JSON en retourneer raw Python dictionaries"""
        data = json.loads(self.json_string)
        return data["items"]


# Adapter 2: JSON naar Product lijst
class JSONAdapter(DataProvider):
    """Adapter die JSON data converteert naar Product objecten"""

    def __init__(self, json_data_source: JSONDataSource):
        self.json_data_source = json_data_source

    def get_products(self) -> List[Product]:
        """Converteer JSON data naar Product objecten"""
        products = []
        json_items = self.json_data_source.get_json_data()

        for item in json_items:
            product = Product(
                id=item["product_id"],
                name=item["product_name"],
                price=item["unit_price"],
                category=item["product_category"],
            )
            products.append(product)

        return products


# Client code
class ProductManager:
    """Client die werkt met de DataProvider interface"""

    def __init__(self, data_provider: DataProvider):
        self.data_provider = data_provider

    def display_products(self):
        """Toon alle producten"""
        products = self.data_provider.get_products()
        print(f"Aantal producten: {len(products)}")
        print("-" * 80)
        for product in products:
            print(product)
        print("-" * 80)

    def calculate_total_value(self):
        """Bereken totale waarde van alle producten"""
        products = self.data_provider.get_products()
        total = sum(p.price for p in products)
        return total

    def filter_by_category(self, category: str):
        """Filter producten op categorie"""
        products = self.data_provider.get_products()
        return [p for p in products if p.category.lower() == category.lower()]


# Demo data
XML_DATA = """<?xml version="1.0"?>
<products>
    <product>
        <id>1</id>
        <name>Laptop</name>
        <price>899.99</price>
        <category>Electronics</category>
    </product>
    <product>
        <id>2</id>
        <name>Muis</name>
        <price>24.99</price>
        <category>Electronics</category>
    </product>
    <product>
        <id>3</id>
        <name>Bureau</name>
        <price>299.99</price>
        <category>Furniture</category>
    </product>
</products>
"""

JSON_DATA = """{
    "items": [
        {
            "product_id": 10,
            "product_name": "Smartphone",
            "unit_price": 599.99,
            "product_category": "Electronics"
        },
        {
            "product_id": 11,
            "product_name": "Koptelefoon",
            "unit_price": 149.99,
            "product_category": "Electronics"
        },
        {
            "product_id": 12,
            "product_name": "Stoel",
            "unit_price": 199.99,
            "product_category": "Furniture"
        }
    ]
}
"""

if __name__ == "__main__":
    print("=" * 80)
    print("ADAPTER PATTERN: XML/JSON naar Product Objecten")
    print("=" * 80)

    # Gebruik XML data via de adapter
    print("\n### XML DATA BRON ###")
    xml_source = XMLDataSource(XML_DATA)
    xml_adapter = XMLAdapter(xml_source)
    xml_manager = ProductManager(xml_adapter)

    xml_manager.display_products()
    print(f"Totale waarde: €{xml_manager.calculate_total_value():.2f}")

    electronics = xml_manager.filter_by_category("Electronics")
    print(f"\nElectronics producten: {len(electronics)}")
    for item in electronics:
        print(f"  - {item.name}: €{item.price:.2f}")

    # Gebruik JSON data via de adapter
    print("\n\n### JSON DATA BRON ###")
    json_source = JSONDataSource(JSON_DATA)
    json_adapter = JSONAdapter(json_source)
    json_manager = ProductManager(json_adapter)

    json_manager.display_products()
    print(f"Totale waarde: €{json_manager.calculate_total_value():.2f}")

    furniture = json_manager.filter_by_category("Furniture")
    print(f"\nFurniture producten: {len(furniture)}")
    for item in furniture:
        print(f"  - {item.name}: €{item.price:.2f}")

    # Demonstratie: Beide adapters werken met dezelfde interface
    print("\n\n### BEIDE BRONNEN SAMEN ###")
    print("De ProductManager werkt met beide data bronnen via dezelfde interface!")

    all_providers = [xml_adapter, json_adapter]
    total_products = 0
    grand_total = 0.0

    for provider in all_providers:
        products = provider.get_products()
        total_products += len(products)
        grand_total += sum(p.price for p in products)

    print(f"Totaal aantal producten uit alle bronnen: {total_products}")
    print(f"Totale waarde van alle producten: €{grand_total:.2f}")
