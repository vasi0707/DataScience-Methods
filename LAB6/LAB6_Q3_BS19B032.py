#Parent Class Polygon
class Polygon:
    def __init__(self,side):
        self.side = side

#Inherited Class Square
class Square(Polygon):
    def __init__(self,side):
        super().__init__(side)
    def FindArea(self):
        return self.side**2

length = int(input("Enter length of the side of square: "))
print("")

square1 = Square(length)
area = square1.FindArea()
print("The area of square is:")
print(area)
