from typing import Protocol
from dataclasses import dataclass
from datetime import datetime


# Memento - slaat de state op
@dataclass
class EditorMemento:
    """Immutable snapshot van de editor state"""
    text: str
    cursor_position: int
    timestamp: datetime

    def get_info(self) -> str:
        preview = self.text[:30] + "..." if len(self.text) > 30 else self.text
        return f"[{self.timestamp.strftime('%H:%M:%S')}] Text: '{preview}' | Cursor: {self.cursor_position}"


# Originator Protocol - object waarvan we state willen opslaan
class Originator(Protocol):
    def save(self) -> EditorMemento:
        """Creëer een memento met huidige state"""
        ...

    def restore(self, memento: EditorMemento) -> None:
        """Herstel state van een memento"""
        ...


# Concrete Originator - de Teksteditor
class TextEditor:
    def __init__(self):
        self.text = ""
        self.cursor_position = 0

    def type(self, content: str) -> None:
        """Type tekst op huidige cursor positie"""
        self.text = (self.text[:self.cursor_position] +
                     content +
                     self.text[self.cursor_position:])
        self.cursor_position += len(content)
        print(f"✎ Getypt: '{content}'")
        self._print_state()

    def delete(self, length: int) -> None:
        """Verwijder tekst voor de cursor"""
        start = max(0, self.cursor_position - length)
        deleted = self.text[start:self.cursor_position]
        self.text = self.text[:start] + self.text[self.cursor_position:]
        self.cursor_position = start
        print(f"⌫ Verwijderd: '{deleted}'")
        self._print_state()

    def move_cursor(self, position: int) -> None:
        """Verplaats cursor naar positie"""
        self.cursor_position = max(0, min(position, len(self.text)))
        print(f"→ Cursor verplaatst naar positie {self.cursor_position}")
        self._print_state()

    def save(self) -> EditorMemento:
        """Maak een snapshot van huidige state"""
        return EditorMemento(
            text=self.text,
            cursor_position=self.cursor_position,
            timestamp=datetime.now()
        )

    def restore(self, memento: EditorMemento) -> None:
        """Herstel state van een memento"""
        self.text = memento.text
        self.cursor_position = memento.cursor_position
        print(f"↺ State hersteld van {memento.timestamp.strftime('%H:%M:%S')}")
        self._print_state()

    def _print_state(self) -> None:
        """Helper om huidige state te tonen"""
        cursor_visual = " " * self.cursor_position + "↑"
        print(f"  Text: '{self.text}'")
        print(f"       {cursor_visual}")


# Caretaker - beheert de mementos
class EditorHistory:
    def __init__(self, editor: TextEditor):
        self.editor = editor
        self.history: list[EditorMemento] = []
        self.current_index = -1

    def save_checkpoint(self) -> None:
        """Sla huidige state op als checkpoint"""
        # Verwijder alle states na huidige index (voor nieuwe branch)
        self.history = self.history[:self.current_index + 1]

        memento = self.editor.save()
        self.history.append(memento)
        self.current_index += 1
        print(f"💾 Checkpoint opgeslagen (#{len(self.history)})")

    def undo(self) -> None:
        """Ga terug naar vorige state"""
        if self.current_index > 0:
            self.current_index -= 1
            self.editor.restore(self.history[self.current_index])
            print(f"⎌ Undo naar checkpoint #{self.current_index + 1}")
        else:
            print("✗ Geen eerdere checkpoints om naar terug te gaan")

    def redo(self) -> None:
        """Ga vooruit naar volgende state"""
        if self.current_index < len(self.history) - 1:
            self.current_index += 1
            self.editor.restore(self.history[self.current_index])
            print(f"⎌ Redo naar checkpoint #{self.current_index + 1}")
        else:
            print("✗ Geen latere checkpoints om naartoe te gaan")

    def show_history(self) -> None:
        """Toon alle opgeslagen checkpoints"""
        print("\n📋 Checkpoint History:")
        for i, memento in enumerate(self.history):
            marker = "→" if i == self.current_index else " "
            print(f"  {marker} #{i + 1}: {memento.get_info()}")

    def restore_checkpoint(self, index: int) -> None:
        """Spring naar specifieke checkpoint"""
        if 0 <= index < len(self.history):
            self.current_index = index
            self.editor.restore(self.history[index])
            print(f"↺ Gesprongen naar checkpoint #{index + 1}")
        else:
            print("✗ Ongeldige checkpoint index")


# Gebruik
if __name__ == "__main__":
    editor = TextEditor()
    history = EditorHistory(editor)

    print("=== Beginnen met typen ===")
    history.save_checkpoint()  # Checkpoint 1: leeg document

    editor.type("Hello")
    history.save_checkpoint()  # Checkpoint 2

    editor.type(" World")
    history.save_checkpoint()  # Checkpoint 3

    editor.type("!")
    history.save_checkpoint()  # Checkpoint 4

    print("\n=== History bekijken ===")
    history.show_history()

    print("\n=== Undo tests ===")
    history.undo()  # Terug naar "Hello World"
    history.undo()  # Terug naar "Hello"

    print("\n=== Redo test ===")
    history.redo()  # Vooruit naar "Hello World"

    print("\n=== Nieuwe bewerkingen na undo ===")
    editor.delete(6)  # Verwijder " World"
    history.save_checkpoint()

    editor.type(" Python")
    history.save_checkpoint()

    print("\n=== Finale history ===")
    history.show_history()

    print("\n=== Spring naar specifiek checkpoint ===")
    history.restore_checkpoint(1)  # Terug naar "Hello"