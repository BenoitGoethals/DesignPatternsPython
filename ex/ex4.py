# Exercise 4: File System Composite
from typing import Protocol, List


class IFile(Protocol):
    name: str

    def get_size(self) -> int:
        ...

    def list_contents(self, indent: int = 0) -> str:
        ...


class File(IFile):
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def get_size(self) -> int:
        return self.size

    def list_contents(self, indent: int = 0) -> str:
        spaces = "  " * indent
        return f"{spaces}{self.name} ({self.size} bytes)"


class Directory(IFile):
    def __init__(self, name: str):
        self.name = name
        self.children: List[IFile] = []

    def add(self, component: IFile):
        self.children.append(component)

    def get_size(self) -> int:
        return sum(child.get_size() for child in self.children)

    def list_contents(self, indent: int = 0) -> str:
        spaces = "  " * indent
        res = [f"{spaces}{self.name}/"]
        for child in self.children:
            res.append(child.list_contents(indent + 1))
        return "\n".join(res)


if __name__ == "__main__":
    # Create structure
    root = Directory("root")
    root.add(File("readme.txt", 100))

    docs = Directory("documents")
    docs.add(File("report.pdf", 5000))
    docs.add(File("notes.txt", 200))

    root.add(docs)

    # Output results
    print(root.list_contents())
    print(f"Total size: {root.get_size()} bytes")