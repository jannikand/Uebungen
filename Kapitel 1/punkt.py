class Punkt:
    def __init__(self, n, sx, sy, sh):
        self.nummer = n
        self.x = sx
        self.y = sy
        self.h = sh
    
    def anzeigen(self):
        print(self.nummer, self.x, self.y, self.h)

    def hdiff(self, other):
        return abs(self.h-other.h)

    def dist(self, other):
        return(((self.x-other.x)**2
        +(self.y-other.y)**2
        +(self.h-other.h)**2)**0.5)