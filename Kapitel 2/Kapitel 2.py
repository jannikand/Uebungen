class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"{self.x},{self.y}"
    
p1 = Punkt(2600000, 1200000)

print(p1)


class Temperatur:
    def __init__(self, c=0):
        self.c = c

    def __str__(self):
        return f"[{self.c}]"
    
    def __gt__(self, other):
        return self.c > other.c

t0 = Temperatur(10)
t1 = Temperatur(20)

print(t0)

if t1 > t0:
    print("t1 grösser")
if t1 < t0:
    print("t1 kleiner")


class vec2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'
    
    def __add__(self, other):
        return vec2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return vec2(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return vec2(self.x*other.x, self.y*other.y)
    
    def __getitem__(self, key):
        if key == 0:
            return self.x
        if key == 1:
            return self.y
        else:
            raise IndexError
    
def skalarprodukt(a, b):
    return a.x*b.x + a.y*b.y

v1 = vec2(3,6)
v2 = vec2(4,8)

v12 = v1 + v2

v2446 = v1 +v2 +v1 -v2 +v2

print(v12)
print(v2446)

v1.skalarprodukt(v2)