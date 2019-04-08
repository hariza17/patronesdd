from factory.orchestra import Orchestra


class Wind(Orchestra):
    WIND_INSTRUMENT = ['guitar', 'piano']

    def create_instrument(self):
        for i in range(0, 1):
            x = self.__getattribute__('create_instrument')
            print(x())


w = Wind()

w.create_instrument()
