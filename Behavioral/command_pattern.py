from typing import Protocol


class Command(Protocol):
    def execute(self) -> None: ...

    def undo(self) -> None: ...


# Receiver - de TV
class Television:
    def __init__(self):
        self.is_on = False
        self.volume = 10
        self.channel = 1

    def turn_on(self):
        self.is_on = True
        print("TV is aangezet")

    def turn_off(self):
        self.is_on = False
        print("TV is uitgezet")

    def volume_up(self):
        if self.is_on:
            self.volume += 1
            print(f"Volume verhoogd naar {self.volume}")

    def volume_down(self):
        if self.is_on and self.volume > 0:
            self.volume -= 1
            print(f"Volume verlaagd naar {self.volume}")

    def next_channel(self):
        if self.is_on:
            self.channel += 1
            print(f"Kanaal gewisseld naar {self.channel}")


# Concrete Commands
class TurnOnCommand:
    def __init__(self, tv: Television):
        self.tv = tv

    def execute(self) -> None:
        self.tv.turn_on()

    def undo(self) -> None:
        self.tv.turn_off()


class TurnOffCommand:
    def __init__(self, tv: Television):
        self.tv = tv

    def execute(self) -> None:
        self.tv.turn_off()

    def undo(self) -> None:
        self.tv.turn_on()


class VolumeUpCommand:
    def __init__(self, tv: Television):
        self.tv = tv

    def execute(self) -> None:
        self.tv.volume_up()

    def undo(self) -> None:
        self.tv.volume_down()


class VolumeDownCommand:
    def __init__(self, tv: Television):
        self.tv = tv

    def execute(self) -> None:
        self.tv.volume_down()

    def undo(self) -> None:
        self.tv.volume_up()


# Invoker - de afstandsbediening
class RemoteControl:
    def __init__(self):
        self.history: list[Command] = []

    def press_button(self, command: Command) -> None:
        command.execute()
        self.history.append(command)

    def press_undo(self) -> None:
        if self.history:
            command = self.history.pop()
            command.undo()
            print("Laatse actie ongedaan gemaakt")
        else:
            print("Geen acties om ongedaan te maken")


# Gebruik
if __name__ == "__main__":
    # Maak een TV aan
    tv = Television()

    # Maak commands aan
    turn_on = TurnOnCommand(tv)
    turn_off = TurnOffCommand(tv)
    volume_up = VolumeUpCommand(tv)
    volume_down = VolumeDownCommand(tv)

    # Maak een afstandsbediening aan
    remote = RemoteControl()

    # Voer commands uit
    print("=== Test Commands ===")
    remote.press_button(turn_on)
    remote.press_button(volume_up)
    remote.press_button(volume_up)
    remote.press_button(volume_up)

    print("\n=== Test Undo ===")
    remote.press_undo()  # Undo volume up
    remote.press_undo()  # Undo volume up

    print("\n=== Meer acties ===")
    remote.press_button(volume_down)
    remote.press_button(turn_off)

    print("\n=== Undo alles ===")
    remote.press_undo()  # Undo turn off
    remote.press_undo()  # Undo volume down
