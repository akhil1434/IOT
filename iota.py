class Shape:
    def no_of_side(self):
        print("This shape has many sides")

class Square(Shape):
    def no_of_sides(self):
        print("A square has many sides")

class square(Shape):
    def no_of_sides(sides):
        print("A square has many 4 sides")

        #Creating objects
        s1=Shape()
        s2=square()
        #calling the method
        s1.no_of_sides()
        s2.no_of_sides()
