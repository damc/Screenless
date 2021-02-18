class EventDispatcher:
    def __init__(self, listeners=None):
        self.listeners = listeners or {}

    def add_listener(self, name, listener):
        self.listeners[name] = listener

    def remove_listener(self, name):
        self.listeners.pop(name)

    def dispatch(self, *args, **kwargs):
        for listener in self.listeners.values():
            listener(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        self.dispatch(*args, **kwargs)
