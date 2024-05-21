# PROGRAMMER

# IMPORT STATEMENTS
import tkinter
import tkinter.messagebox
import tkinter.simpledialog
import tkinter.ttk

class ApplicationView:
    # CONSTRUCTOR
    def __init__(self):
        self.__application_window = tkinter.Tk()
        self.__application_window.title("Application View")
        self.__application_window.geometry("800x600")


        self.__application_frame = tkinter.ttk.Frame(self.__application_window, title = "Application Frame")

    """
    Application Frame will contain a Canvas
    Outside Geometric Shape graphic will be centered in the Canvas
    Inside Geometric Shape graphic will be centered in the Canvas
    All File Menu selections will display an appropriate Tkinter Popup
    All Edit Menu selections will display an appropriate Tkinter Popup
    All View Menu selections will display an appropriate Tkinter Popup
    The Help Menu selections will display an appropriate Tkinter Popup
    All Exception messages will be displayed using an appropriate Tkinter Popup
    Canvas graphics will update every time that an Outside Geometric Shape value is modified
    Canvas graphics will update every time that an Inside Geometric Shape value is modified
    """
    # INSTANCE METHODS

    # File Menu 
    def edit_outside_shape_radius(self):
        pass
    def edit_outside_shape_line_color(self):
        pass
    def edit_outside_shape_fill_color(self):
        pass
    def edit_inside_shape_length(self):
        pass
    def edit_inside_shape_height(self):
        pass
    def edit_inside_shape_line_color(self):
        pass
    def edit_inside_shape_fill_color(self):
        pass

    # Pickle File Editing
    def edit_pickle_outside_shape_radius(self):
        pass
    def edit_pickle_outside_shape_line_color(self):
        pass
    def edit_pickle_outside_shape_fill_color(self):
        pass
    def edit_pickle_inside_shape_length(self):
        pass
    def edit_pickle_inside_shape_line_color(self):
        pass
    def edit_pickle_inside_shape_fill_color(self):
        pass