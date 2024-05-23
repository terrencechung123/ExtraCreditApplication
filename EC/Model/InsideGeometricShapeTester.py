# PROGRAMMER: Khiem Nguyen, Richie Nguyen, Terrence Chung

# IMPORT STATEMENTS
from InsideGeometricShape import InsideGeometricShape

# FUNCTIONS
def setUp():
    shape = InsideGeometricShape(10, 20, "red", "blue")

    print(shape.get_length(), "should be", 10)
    print(shape.get_height(), "should be", 20)
    print(shape.get_line_color(), "should be", "red")
    print(shape.get_fill_color(), "should be", "blue")

    shape.set_length(15)
    print(shape.get_length(), "should be", 15)

    shape.set_height(25)
    print(shape.get_height(), "should be", 25)

    shape.set_line_color("green")
    print(shape.get_line_color(), "should be", "green")

    shape.set_fill_color("yellow")
    print(shape.get_fill_color(), "should be", "yellow")

    print(shape.area(), "should be", 200)

    print(shape.perimeter(), "should be", 60)