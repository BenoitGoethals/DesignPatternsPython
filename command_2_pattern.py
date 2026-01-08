from typing import Protocol


# Command Protocol
class Command(Protocol):
    def execute(self) -> None: ...

    def undo(self) -> None: ...


# Receiver - de Teksteditor
class TextEditor:
    def __init__(self):
        self.text = ""

    def insert(self, position: int, content: str) -> None:
        self.text = self.text[:position] + content + self.text[position:]
        print(f"Tekst ingevoegd: '{content}'")
        print(f"Huidige tekst: '{self.text}'")

    def delete(self, position: int, length: int) -> str:
        deleted = self.text[position : position + length]
        self.text = self.text[:position] + self.text[position + length :]
        print(f"Tekst verwijderd: '{deleted}'")
        print(f"Huidige tekst: '{self.text}'")
        return deleted

    def replace(self, position: int, length: int, new_text: str) -> str:
        old_text = self.text[position : position + length]
        self.text = self.text[:position] + new_text + self.text[position + length :]
        print(f"Tekst vervangen: '{old_text}' -> '{new_text}'")
        print(f"Huidige tekst: '{self.text}'")
        return old_text

    def get_text(self) -> str:
        return self.text


# Concrete Commands
class InsertCommand:
    def __init__(self, editor: TextEditor, position: int, text: str):
        self.editor = editor
        self.position = position
        self.text = text

    def execute(self) -> None:
        self.editor.insert(self.position, self.text)

    def undo(self) -> None:
        self.editor.delete(self.position, len(self.text))


class DeleteCommand:
    def __init__(self, editor: TextEditor, position: int, length: int):
        self.editor = editor
        self.position = position
        self.length = length
        self.deleted_text = ""

    def execute(self) -> None:
        self.deleted_text = self.editor.delete(self.position, self.length)

    def undo(self) -> None:
        self.editor.insert(self.position, self.deleted_text)


class ReplaceCommand:
    def __init__(self, editor: TextEditor, position: int, length: int, new_text: str):
        self.editor = editor
        self.position = position
        self.length = length
        self.new_text = new_text
        self.old_text = ""

    def execute(self) -> None:
        self.old_text = self.editor.replace(self.position, self.length, self.new_text)

    def undo(self) -> None:
        self.editor.replace(self.position, len(self.new_text), self.old_text)


# Macro Command - combineert meerdere commands
class MacroCommand:
    def __init__(self, commands: list[Command]):
        self.commands = commands

    def execute(self) -> None:
        print("--- Macro Command Start ---")
        for command in self.commands:
            command.execute()
        print("--- Macro Command End ---")

    def undo(self) -> None:
        print("--- Macro Undo Start ---")
        # Undo in omgekeerde volgorde
        for command in reversed(self.commands):
            command.undo()
        print("--- Macro Undo End ---")


# Invoker - Command Manager met undo/redo
class CommandManager:
    def __init__(self):
        self.history: list[Command] = []
        self.redo_stack: list[Command] = []

    def execute(self, command: Command) -> None:
        command.execute()
        self.history.append(command)
        # Clear redo stack na nieuwe actie
        self.redo_stack.clear()

    def undo(self) -> None:
        if self.history:
            command = self.history.pop()
            command.undo()
            self.redo_stack.append(command)
            print("✓ Undo uitgevoerd")
        else:
            print("✗ Geen acties om ongedaan te maken")

    def redo(self) -> None:
        if self.redo_stack:
            command = self.redo_stack.pop()
            command.execute()
            self.history.append(command)
            print("✓ Redo uitgevoerd")
        else:
            print("✗ Geen acties om opnieuw te doen")


# Gebruik
if __name__ == "__main__":
    editor = TextEditor()
    manager = CommandManager()

    print("=== Tekst invoegen ===")
    manager.execute(InsertCommand(editor, 0, "Hello"))
    manager.execute(InsertCommand(editor, 5, " World"))
    manager.execute(InsertCommand(editor, 11, "!"))

    print("\n=== Undo ===")
    manager.undo()  # Verwijder "!"

    print("\n=== Redo ===")
    manager.redo()  # Voeg "!" weer toe

    print("\n=== Delete ===")
    manager.execute(DeleteCommand(editor, 5, 6))  # Verwijder " World"

    print("\n=== Replace ===")
    manager.execute(ReplaceCommand(editor, 0, 5, "Hi"))  # Vervang "Hello" met "Hi"

    print("\n=== Undo alles ===")
    manager.undo()  # Undo replace
    manager.undo()  # Undo delete

    print("\n=== Macro Command ===")
    macro = MacroCommand(
        [
            DeleteCommand(editor, 0, 5),  # Verwijder "Hello"
            InsertCommand(editor, 0, "Goodbye"),  # Voeg "Goodbye" toe
            InsertCommand(editor, 7, " cruel"),  # Voeg " cruel" toe
        ]
    )
    manager.execute(macro)

    print("\n=== Undo Macro ===")
    manager.undo()
