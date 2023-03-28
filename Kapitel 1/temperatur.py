class Temperatur:
    def __init__(self):
        self._celsius = 0
        
    def kelvin(self):
        return self._celsius+273.15

    def setTemperatur(self, c):
        if c < -273.15:
            raise ValueError("Temperatur zu klein")
        self._celsius = c

    def getTemperatur(self):
        return self._celsius

    celsius = property(setTemperatur, getTemperatur)
    

basel = Temperatur()
basel.setTemperatur(12)
print(basel.getTemperatur())

