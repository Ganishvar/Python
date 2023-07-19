class Rectangle:
    def __init__(self,c,l,w):
        self.color=c
        self.length=l
        self.width=w
    def area(self):
        self.area=self.length*self.width
        return self.area
    def perimeter(self):
        self.perimeter=2*(self.length+self.width)
        return self.perimeter
    def volume(self,h):
        self.volume=self.length*self.width*h
        return self.volume

rect1=Rectangle("red",2,2)
rect2=Rectangle("blue",4,4)
print(rect1.color,rect1.length,rect1.area(),rect1.perimeter())
print(rect2.color,rect2.length,rect2.area(),rect2.perimeter())
vol=rect1.volume(5)
print(vol)