from abc import ABC, abstractmethod
from typing import Protocol


# Visitor Protocol
class DocumentVisitor(Protocol):
    def visit_paragraph(self, paragraph: "Paragraph") -> None: ...

    def visit_heading(self, heading: "Heading") -> None: ...

    def visit_image(self, image: "Image") -> None: ...

    def visit_table(self, table: "Table") -> None: ...


# Element interface
class DocumentElement(ABC):
    @abstractmethod
    def accept(self, visitor: DocumentVisitor) -> None:
        """Accept a visitor"""
        pass


# Concrete Elements
class Paragraph(DocumentElement):
    def __init__(self, text: str):
        self.text = text

    def accept(self, visitor: DocumentVisitor) -> None:
        visitor.visit_paragraph(self)


class Heading(DocumentElement):
    def __init__(self, text: str, level: int):
        self.text = text
        self.level = level  # 1-6 voor H1-H6

    def accept(self, visitor: DocumentVisitor) -> None:
        visitor.visit_heading(self)


class Image(DocumentElement):
    def __init__(self, url: str, alt_text: str):
        self.url = url
        self.alt_text = alt_text

    def accept(self, visitor: DocumentVisitor) -> None:
        visitor.visit_image(self)


class Table(DocumentElement):
    def __init__(self, rows: int, columns: int, data: list[list[str]]):
        self.rows = rows
        self.columns = columns
        self.data = data

    def accept(self, visitor: DocumentVisitor) -> None:
        visitor.visit_table(self)


# Document container
class Document:
    def __init__(self, title: str):
        self.title = title
        self.elements: list[DocumentElement] = []

    def add_element(self, element: DocumentElement) -> None:
        self.elements.append(element)

    def accept(self, visitor: DocumentVisitor) -> None:
        for element in self.elements:
            element.accept(visitor)


# Concrete Visitor 1: HTML Export
class HTMLExportVisitor:
    def __init__(self):
        self.html_parts: list[str] = []

    def visit_paragraph(self, paragraph: Paragraph) -> None:
        self.html_parts.append(f"<p>{paragraph.text}</p>")

    def visit_heading(self, heading: Heading) -> None:
        self.html_parts.append(f"<h{heading.level}>{heading.text}</h{heading.level}>")

    def visit_image(self, image: Image) -> None:
        self.html_parts.append(f'<img src="{image.url}" alt="{image.alt_text}" />')

    def visit_table(self, table: Table) -> None:
        html = "<table>\n"
        for row in table.data:
            html += "  <tr>\n"
            for cell in row:
                html += f"    <td>{cell}</td>\n"
            html += "  </tr>\n"
        html += "</table>"
        self.html_parts.append(html)

    def get_html(self) -> str:
        return "\n".join(self.html_parts)


# Concrete Visitor 2: Word Counter
class WordCountVisitor:
    def __init__(self):
        self.word_count = 0
        self.heading_count = 0
        self.image_count = 0
        self.table_count = 0

    def visit_paragraph(self, paragraph: Paragraph) -> None:
        self.word_count += len(paragraph.text.split())

    def visit_heading(self, heading: Heading) -> None:
        self.word_count += len(heading.text.split())
        self.heading_count += 1

    def visit_image(self, image: Image) -> None:
        self.image_count += 1

    def visit_table(self, table: Table) -> None:
        self.table_count += 1
        for row in table.data:
            for cell in row:
                self.word_count += len(cell.split())

    def get_statistics(self) -> str:
        return f"""
📊 Document Statistieken:
   • Totaal woorden: {self.word_count}
   • Koppen: {self.heading_count}
   • Afbeeldingen: {self.image_count}
   • Tabellen: {self.table_count}
"""


# Concrete Visitor 3: Markdown Export
class MarkdownExportVisitor:
    def __init__(self):
        self.markdown_parts: list[str] = []

    def visit_paragraph(self, paragraph: Paragraph) -> None:
        self.markdown_parts.append(f"{paragraph.text}\n")

    def visit_heading(self, heading: Heading) -> None:
        prefix = "#" * heading.level
        self.markdown_parts.append(f"{prefix} {heading.text}\n")

    def visit_image(self, image: Image) -> None:
        self.markdown_parts.append(f"![{image.alt_text}]({image.url})\n")

    def visit_table(self, table: Table) -> None:
        if not table.data:
            return

        # Header row
        header = "| " + " | ".join(table.data[0]) + " |"
        separator = "|" + "|".join([" --- " for _ in table.data[0]]) + "|"
        self.markdown_parts.append(header)
        self.markdown_parts.append(separator)

        # Data rows
        for row in table.data[1:]:
            row_str = "| " + " | ".join(row) + " |"
            self.markdown_parts.append(row_str)

        self.markdown_parts.append("")

    def get_markdown(self) -> str:
        return "\n".join(self.markdown_parts)


# Concrete Visitor 4: Plain Text Export
class PlainTextVisitor:
    def __init__(self):
        self.text_parts: list[str] = []

    def visit_paragraph(self, paragraph: Paragraph) -> None:
        self.text_parts.append(paragraph.text)
        self.text_parts.append("")

    def visit_heading(self, heading: Heading) -> None:
        self.text_parts.append(heading.text.upper())
        self.text_parts.append("=" * len(heading.text))
        self.text_parts.append("")

    def visit_image(self, image: Image) -> None:
        self.text_parts.append(f"[Afbeelding: {image.alt_text}]")
        self.text_parts.append("")

    def visit_table(self, table: Table) -> None:
        for row in table.data:
            self.text_parts.append(" | ".join(row))
        self.text_parts.append("")

    def get_text(self) -> str:
        return "\n".join(self.text_parts)


# Gebruik
if __name__ == "__main__":
    # Creëer een document
    doc = Document("Mijn Artikel")

    doc.add_element(Heading("Introductie", 1))
    doc.add_element(
        Paragraph(
            "Dit is een voorbeeld document om het Visitor pattern te demonstreren."
        )
    )
    doc.add_element(
        Paragraph(
            "Het Visitor pattern is handig voor het scheiden van operaties van objecten."
        )
    )

    doc.add_element(Heading("Voorbeelden", 2))
    doc.add_element(Image("https://example.com/diagram.png", "UML Diagram"))

    doc.add_element(Heading("Data", 2))
    doc.add_element(
        Table(
            3,
            2,
            [
                ["Pattern", "Type"],
                ["Visitor", "Behavioral"],
                ["Command", "Behavioral"],
                ["Memento", "Behavioral"],
            ],
        )
    )

    # Pas verschillende visitors toe
    print("=" * 60)
    print("HTML EXPORT")
    print("=" * 60)
    html_visitor = HTMLExportVisitor()
    doc.accept(html_visitor)
    print(html_visitor.get_html())

    print("\n" + "=" * 60)
    print("STATISTIEKEN")
    print("=" * 60)
    stats_visitor = WordCountVisitor()
    doc.accept(stats_visitor)
    print(stats_visitor.get_statistics())

    print("=" * 60)
    print("MARKDOWN EXPORT")
    print("=" * 60)
    md_visitor = MarkdownExportVisitor()
    doc.accept(md_visitor)
    print(md_visitor.get_markdown())

    print("=" * 60)
    print("PLAIN TEXT EXPORT")
    print("=" * 60)
    text_visitor = PlainTextVisitor()
    doc.accept(text_visitor)
    print(text_visitor.get_text())
