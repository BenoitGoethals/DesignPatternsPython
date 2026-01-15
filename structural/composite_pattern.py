from abc import ABC, abstractmethod
from typing import List


# Component: De basis interface voor zowel leaf als composite objecten
class FileSystemComponent(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def display(self, indent: int = 0) -> None:
        """Toon de component met indentatie"""
        pass

    @abstractmethod
    def get_size(self) -> int:
        """Bereken de grootte van de component"""
        pass


# Leaf: Representeert een bestand (eindpunt, geen kinderen)
class File(FileSystemComponent):
    def __init__(self, name: str, size: int):
        super().__init__(name)
        self.size = size

    def display(self, indent: int = 0) -> None:
        print(f"{'  ' * indent}📄 {self.name} ({self.size} KB)")

    def get_size(self) -> int:
        return self.size


# Composite: Representeert een map (kan kinderen bevatten)
class Directory(FileSystemComponent):
    def __init__(self, name: str):
        super().__init__(name)
        self.children: List[FileSystemComponent] = []

    def add(self, component: FileSystemComponent) -> None:
        """Voeg een bestand of map toe"""
        self.children.append(component)

    def remove(self, component: FileSystemComponent) -> None:
        """Verwijder een bestand of map"""
        self.children.remove(component)

    def display(self, indent: int = 0) -> None:
        print(f"{'  ' * indent}📁 {self.name}/")
        for child in self.children:
            child.display(indent + 1)

    def get_size(self) -> int:
        """Bereken totale grootte van alle bestanden in de map"""
        total_size = 0
        for child in self.children:
            total_size += child.get_size()
        return total_size


# Voorbeeld gebruik
if __name__ == "__main__":
    # Maak bestanden
    file1 = File("document.txt", 10)
    file2 = File("foto.jpg", 250)
    file3 = File("video.mp4", 5000)
    file4 = File("rapport.pdf", 150)
    file5 = File("code.py", 5)
    file6 = File("code.py", 5)

    # Maak mappen
    root = Directory("root")
    documenten = Directory("Documenten")
    media = Directory("Media")
    projecten = Directory("Projecten")
    tmp = Directory("tmp")

    # Bouw de boomstructuur
    root.add(documenten)
    root.add(media)
    root.add(projecten)

    documenten.add(file1)
    documenten.add(file4)

    media.add(file2)
    media.add(file3)

    tmp.add(file6)

    projecten.add(file5)
    projecten.add(tmp)

    # Toon de volledige structuur
    print("=== Bestandssysteem Structuur ===")
    root.display()

    print(f"\n=== Groottes ===")
    print(f"Totale grootte root: {root.get_size()} KB")
    print(f"Grootte Documenten: {documenten.get_size()} KB")
    print(f"Grootte Media: {media.get_size()} KB")
    print(f"Grootte Projecten: {projecten.get_size()} KB")

    # Demonstreer: je kunt individuele bestanden EN mappen op dezelfde manier behandelen
    print(f"\n=== Uniform gedrag ===")
    components = [file1, documenten, media]
    for component in components:
        print(f"{component.name}: {component.get_size()} KB")
