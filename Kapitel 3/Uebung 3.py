
class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str___(self):
        return f"{self.x},{self.y}"

class Figur:
   def __init__(self):
      self.name = "Figur"

   def Umfang(self):
      return 0
   
   def __str__(self):
      return self.name
   
