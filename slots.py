class Point2D:
    __slots__=('x','y')

    def __init__(self,x,y):
        self.x=x
        self.y=y

    @property
    def length(self):
        return (self.x**2+ self.y**2)**0.5

pt1=Point2D(2,1)
print(pt1.length)

class Point3D(Point2D):
    __slots__=('z')

    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z=z

        