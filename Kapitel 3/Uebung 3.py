import math as m

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
      self.name = name

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
      return self.r*2*m.pi
   
   def __str__(self):
      return f"{self.name} M = ({self.mx}, {self.my}) r = {self.r}"
   

class Rechteck(Figur):
   def __init__(self, sx, sy, zx, zy):
      super().__init__('Rechteck')
      self.sx = sx
      self.sy = sy
      self.zx = zx
      self.zy = zy

   def umfang(self):
      pstart = Punkt(self.sx,self.sy)
      purechts = Punkt(self.zx,self.sy)
      pziel = Punkt(self.zx,self.zy)
      return 2*pstart.dist(purechts) + 2*purechts.dist(pziel)
   
   def __str__(self):
      return f"{self.name} ({self.sx}, {self.sy}) - ({self.zx}, {self.zy})"
   

class Dreieck(Figur):
   def __init__(self, ax, ay, bx, by, cx, cy):
      super().__init__('Dreieck')
      self.A = Punkt(ax,ay)
      self.B = Punkt(bx,by)
      self.C = Punkt(cx,cy)


   def umfang(self):
      return self.A.dist(self.B) + self.B.dist(self.A) + self.C.dist(self.A)
   
   def __str__(self):
      return f"{self.name} A=({self.A}) B=({self.B}) C=({self.C}))"


class Polygon(Figur):
   def __init__(self, *values):
      super().__init__('Polygon')
      self.ecken = []
      for i in range(0,len(values),2):
         x,y=values[i], values[i+1]
         self.ecken.append(Punkt(x,y))

   def umfang(self):
      umfang = 0
      for i in range(len(self.ecken)):
         x = (i+1)%len(self.ecken)
         seite = self.ecken[i].dist(self.ecken[x])
         umfang += seite
      return umfang

   def __str__(self):
      str_ecken = ''
      for i in range(len(self.ecken)):
         str_ecken += f'({self.ecken[i]}) '
      return f"{self.name} " + str_ecken
   

class Polygon_neu(Figur):
   def __init__(self, punktliste):
      super().__init__('Polygon')
      self.pl = punktliste
   
   

   def __str__(self):
      s = f'{self.name}: '
      for punkt in self.pl:
         s += f'{punkt} '
      return s

p1 = Punkt(4,5)
print(p1)

p2 = Punkt(4,6)
print(p2.dist(p1))

f1 = Kreis(1,1,2)
f1.umfang()
print(f1)

f2 = Rechteck(0,1,6,4)
f2.umfang()
print(f2)

f3 = Dreieck(1,2,5,1,4,4)
f3.umfang()
print(f3)

f4 = Polygon(1,2,5,1,4,4,2,7)
f4.umfang()
print(f4)

polygonliste = [Punkt(1,1), Punkt(2,4), Punkt(3,3.5), Punkt(4,4), Punkt(4,1), Punkt(1,1)]
f5 = Polygon_neu(polygonliste)
print(f5)
