class vec3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'({self.x},{self.y},{self.z})'
    
    def __add__(self, other):
        return vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        return vec3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other):
        if type(other) == vec3:
            return vec3(self.x * other.x, self.y * other.y, self.z * other.z)
        if type(other) == float or int:
            return vec3(self.x * other, self.y * other, self.z * other)
        
    def length(self):
        return (self.x**2+self.y**2+self.z**2)**0.5
        
    def cross(self, other):
        return vec3(
            self.y*other.z - self.z*other.y,
            self.z*other.x - self.x*other.z,
            self.x*other.y - self.y*other.x
        )

    def dot(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z


    def normalize(self):
        return vec3(
            self.x/self.length(),
            self.y/self.length(),
            self.z/self.length()
        )



v1 = vec3(1,2,3)
v2 = vec3(2,4,6)

v10 = v1*1.1
v11 = v1+v2
v12 = v2-v1

print(v10,v11,v12)
print(v1.length())
print(v1.cross(v2))
print(v1.dot(v2))
print(v1.normalize())