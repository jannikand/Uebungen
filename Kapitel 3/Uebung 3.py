import math

class Punkt:
   def __init__(self, x, y):
      self.x = x
      self.y = y

   def dist(self, other):
      return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        
   def __str__(self):
      return f"{self.x}, {self.y}"

class Figur:
   def __init__(self, name):
      self.name = "Figur"

   def umfang(self):
      return 0
   
   def __str__(self):
      return self.name
   
class Kreis(Figur):
   def __init__(self, mx, my, r):
      super().__init__("Kreis")
      self.mx = mx
      self.my = my
      self.r = r
      

   def umfang(self):
      return self.r*2*pi
   
   def __str__(self):
      m = Punkt(self.mx,self.my)
      return f"{self.name}, M = ({m}) r = {self.r}"
   

p1 = Punkt(4,5)
print(p1)
p2 = Punkt(4,6)
print()

f1 = Kreis(1,1,2)
print(f1)