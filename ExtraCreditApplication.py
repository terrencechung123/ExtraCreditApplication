'''Rectangle Inscribed inside of Circle'''

# PROGRAMMER: Khiem Nguyen, Richie Nguyen, Terrence Chung

# IMPORT STATEMENTS
from Controller.KineticEnergyCalculatorController import KineticEnergyCalculatorController
from Model.KineticEnergy import KineticEnergy
from View.KineticEnergyCalculatorView import KineticEnergyCalculatorView
# FUNCTIONS

def kinetic_energy_application():
    model = KineticEnergy()
    view = KineticEnergyCalculatorView()
    controller = KineticEnergyCalculatorController(model, view)

kinetic_energy_application()