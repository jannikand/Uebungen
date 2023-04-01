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
      self.ax = ax
      self.ay = ay
      self.bx = bx
      self.by = by
      self.cx = cx
      self.cy = cy
      

   def umfang(self):
      pa = Punkt(self.ax,self.ay)
      pb = Punkt(self.bx,self.by)
      pc = Punkt(self.cx,self.cy)
      return pa.dist(pb) + pb.dist(pc) + pc.dist(pa)
   
   def __str__(self):
      return f"{self.name} A=({self.ax}, {self.ay}) B=({self.bx}, {self.by}) C=({self.cx}, {self.cy}))"


class Polygon(Figur):
   def __init__(self, ):
      super().__init__('Polygon')


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