from typing import Protocol


class Notifier(Protocol):

    def send(self, message: str):
        pass


class EmailNotifier(Notifier):
    def send(self, message: str):
        print(f"Email: {message}")


class NotifierDecorator(Notifier):
    def __init__(self, notif: Notifier):
        self._notifier = notif

    def send(self, message: str):
        self._notifier.send(message)


class SMSDecorator(NotifierDecorator):
    def send(self, message: str):
        super().send(message)
        print(f"SMS: {message}")


class SlackDecorator(NotifierDecorator):
    def send(self, message: str):
        super().send(message)
        print(f"Slack: {message}")


notifier = EmailNotifier()
notifier = SMSDecorator(notifier)
notifier = SlackDecorator(notifier)

notifier.send("System down")
