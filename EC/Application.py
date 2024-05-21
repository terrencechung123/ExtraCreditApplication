'''Rectangle Inscribed inside of Circle'''

# PROGRAMMER: Khiem Nguyen, Richie Nguyen, Terrence Chung

# IMPORT STATEMENTS
from ApplicationController import ApplicationController
from InsideGeometricShape import InsideGeometricShape
from OutsideGeometricShape import OutsideGeometricShape
from ApplicationView import ApplicationView

# FUNCTIONS

def application():
    outside_model = Outside_Geometric_Shape(1.0, "black", "red")
    inside_model = Inside_Geometric_Shape(1.0, 2.0, "black", "red")
    view = ApplicationView()
    controller = KineticEnergyCalculatorController(outside_model, inside_model, view)

application()