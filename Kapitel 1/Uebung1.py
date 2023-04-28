#Aufgabe 1
class vec3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def len(self):
        return ((self.x**2+self.y**2+self.z**2)**0.5)

p1 = vec3(1,1,1)
p2 = vec3()

p1.len()


#Aufgabe 2b
class wgs84coord:
    def __init__(self):
        self._longitude = 0
        self._latitude = 0

    def setLng(self, value):
        if value >180:
            self._longitude = value -360
            print(f'Länge wurde korrigiert auf {self._longitude} korrigiert!')
        elif value < -180:
            self._longitude = value +360
            print(f'Länge wurde korrigiert auf {self._longitude} korrigiert!')
        else:
            self._longitude = value

    def getLng(self):
        return self._longitude
    
    def setLat(self, value):
        if value >90:
            self._latitude = value -180
            print(f'Breite wurde korrigiert auf {self._latitude} korrigiert!')
        elif value < -90:
            self._latitude = value +180
            print(f'Breite wurde korrigiert auf {self._latitude} korrigiert!')
        else:
            self._latitude = value
 
    def getLat(self):
        return self._latitude
               
k1 = wgs84coord()
k1.setLng(-270)
k1.setLat(-120)
print(k1.getLng(),k1.getLat())


#Aufgabe 2c
class wgs84coord:
    def __init__(self, longitude=0, latitude=0):
        self.longitude = longitude
        self.latitude = latitude

    @property
    def longitude(self):
        return self._longitude
    
    @longitude.setter
    def longitude(self, value):
        if value >180:
            self._longitude = value -360
            print(f'Länge wurde korrigiert auf {self._longitude} korrigiert!')
        elif value < -180:
            self._longitude = value +360
            print(f'Länge wurde korrigiert auf {self._longitude} korrigiert!')
        else:
            self._longitude = value

    @property
    def latitude(self):
        return self._latitude
    
    @latitude.setter
    def latitude(self, value):
        if value >90:
            self._latitude = value -180
            print(f'Breite wurde korrigiert auf {self._latitude} korrigiert!')
        elif value < -90:
            self._latitude = value +180
            print(f'Breite wurde korrigiert auf {self._latitude} korrigiert!')
        else:
            self._latitude = value

k2 = wgs84coord(90,45)
print(k2.longitude)
print(k2.latitude)

k2.longitude = -190
print(k2.longitude)