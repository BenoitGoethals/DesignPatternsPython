class NewsAgency:
    def __init__(self):
        self._subscribers = []
        self._news = None

    def subscribe(self, subscriber):
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self._subscribers.remove(subscriber)

    def publish_news(self, news):
        self._news = news
        self._notify_subscribers()

    def _notify_subscribers(self):
        for subscriber in self._subscribers:
            subscriber.receive_news(self._news)


class NewsSubscriber:
    def __init__(self, name):
        self.name = name

    def receive_news(self, news):
        print(f"{self.name} received: {news}")


# Gebruik
agency = NewsAgency()

subscriber1 = NewsSubscriber("Alice")
subscriber2 = NewsSubscriber("Bob")

agency.subscribe(subscriber1)
agency.subscribe(subscriber2)

agency.publish_news("Breaking: Python 4.0 released!")
# Output:
# Alice received: Breaking: Python 4.0 released!
# Bob received: Breaking: Python 4.0 released!