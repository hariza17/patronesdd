from factory.instrumento import Instrument


class Piano(Instrument):
    def __init__(self):
        self.type = "wind"

    def play(self):
        print(f"{self.type}: playing the piano")
