from observer.Observer import Observer


class ConcreteObserver(Observer):
    def update(self, arg):
        self._observer_state = arg
        print(self._observer_state)
