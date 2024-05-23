'''Rectangle Inscribed inside of Circle'''

# PROGRAMMER: Khiem Nguyen, Richie Nguyen, Terrence Chung

# IMPORT STATEMENTS
from Controller.ApplicationController import ApplicationController
from Model.InsideGeometricShape import InsideGeometricShape
from Model.OutsideGeometricShape import OutsideGeometricShape
from View.ApplicationView import ApplicationView

# FUNCTIONS

def application():
    outside_model = OutsideGeometricShape(1.0, "black", "red")
    inside_model = InsideGeometricShape(1.0, 2.0, "black", "red")
    view = ApplicationView()
    controller = ApplicationController(outside_model, inside_model, view)
    view.start()
application()