# PROGRAMMER: Khiem Nguyen, Richie Nguyen, Terrence Chung

# IMPORT STATEMENTS
import tkinter
import pickle

class ApplicationController():
    # CONSTRUCTOR
    def __init__(self, model_outside, model_inside, view):
        self.__default_circle_radius = 1.0
        self.__default_circle_line_color = "black"
        self.__default_circle_fill_color = "red"

        self.__default_rectangle_length = 1.0
        self.__default_rectangle_height = 2.0
        self.__default_rectangle_line_color = "black"
        self.__default_rectangle_fill_color = "red"

        self.__model_outside = model_outside
        self.__model_inside = model_inside
        self.__view = view

        self.__application_window = tkinter.Tk()
        self.__application_window.title("Application")
        self.__application_window.geometry("1000x500")

        self.__application_menu = tkinter.Menu(self.__application_window)

        # File menu
        self.__file_menu = tkinter.Menu(self.__application_menu)
        self.__file_menu.add_command(label="New")
        self.__file_menu.add_command(label="Open")
        self.__file_menu.add_command(label="Save as XML")
        self.__file_menu.add_command(label="Save as JSON")
        self.__application_menu.add_cascade(label="File", menu=self.__file_menu)

        # Edit Menu
        self.__edit_menu = tkinter.Menu(self.__application_menu)
        self.__edit_menu.add_command(label="Outside Shape (Circle) Radius", command = self.edit_outside_shape_radius)
        self.__edit_menu.add_command(label="Outside Shape (Circle) Line Color", command = self.edit_outside_shape_line_color)
        self.__edit_menu.add_command(label="Outside Shape (Circle) Fill Color", command = self.edit_outside_shape_fill_color)
        self.__edit_menu.add_command(label="Inside Shape (Rectangle) Length", command = self.edit_inside_shape_length)
        self.__edit_menu.add_command(label="Inside Shape (Rectangle) Height", command = self.edit_inside_shape_height)
        self.__edit_menu.add_command(label="Inside Shape (Rectangle) Line Color", command = self.edit_inside_shape_line_color)
        self.__edit_menu.add_command(label="Inside Shape (Rectangle) Fill Color", command = self.edit_inside_shape_fill_color)
        self.__edit_menu.add_command(label="Pickle File: Outside Shape (Circle) Radius", command = self.edit_pickle_outside_shape_radius)
        self.__edit_menu.add_command(label="Pickle File: Outside Shape (Circle) Line Color", command = self.edit_pickle_outside_shape_line_color)
        self.__edit_menu.add_command(label="Pickle File: Outside Shape (Circle) Fill Color", command = self.edit_pickle_outside_shape_fill_color)
        self.__edit_menu.add_command(label="Pickle File: Inside Shape (Rectangle) Length", command = self.edit_pickle_inside_shape_length)
        self.__edit_menu.add_command(label="Pickle File: Inside Shape (Rectangle) Height", command = self.edit_pickle_inside_shape_height)
        self.__edit_menu.add_command(label="Pickle File: Inside Shape (Rectangle) Line Color", command = self.edit_pickle_inside_shape_line_color)
        self.__edit_menu.add_command(label="Pickle File: Inside Shape (Rectangle) Fill Color", command = self.edit_pickle_inside_shape_fill_color)
        self.__application_menu.add_cascade(label="Edit", menu=self.__edit_menu)

        # View Menu
        self.__view_menu = tkinter.Menu(self.__application_menu)
        self.__view_menu.add_command(label="Outside Geometric Shape", command=self.view_outside_shape) # Circle
        self.__view_menu.add_command(label="Inside Geometric Shape", command=self.view_inside_shape) # Rectangle
        self.__application_menu.add_cascade(label="View", menu=self.__view_menu)

        # Help Menu
        self.__help_menu = tkinter.Menu(self.__application_menu)
        self.__help_menu.add_command(label="About")
        self.__application_menu.add_cascade(label="Help", menu=self.__help_menu)

        self.__application_window["menu"] = self.__application_menu
        self.__application_window.mainloop()

    # INSTANCE METHODS
    def file_new(self):

        # Initialize default values for pickle file for outside shape (circle)
        circle_settings = (self.__default_circle_radius, self.__default_circle_line_color, self.__default_circle_fill_color)

        with open("OutsideShape.pickle", "wb") as binary_file_input:
            pickle.dump(circle_settings, binary_file_input)

        # Initialize default values and pickle file for inside shape (rectangle)
        rectangle_settings = (self.__default_rectangle_length, self.__default_rectangle_height, self.__default_rectangle_line_color, self.__default_rectangle_fill_color)

        with open("InsideShape.pickle", "wb") as binary_file_input:
            pickle.dump(rectangle_settings, binary_file_input)

    def file_open(self):
        pass

    def file_save_xml(self):
        pass

    def file_save_json(self):
        pass

    def view_outside_shape(self):
        self.__temp_application_window = tkinter.Tk()
        self.__temp_application_window.title("Outside Shape")
        self.__temp_application_window.geometry("800x500")

        self.__temp_application_window.mainloop()

    def view_inside_shape(self):
        self.__temp_application_window = tkinter.Tk()
        self.__temp_application_window.title("Inside Shape")
        self.__temp_application_window.geometry("800x500")

        self.__temp_application_window.mainloop()

    def edit_outside_shape_radius(self):
        outside_radius = tkinter.simpledialog.askfloat("Edit Outside Radius", "Enter New Outside Radius:")
        self.__model_outside.set_radius(outside_radius)
    def edit_outside_shape_line_color(self):
        outside_line_color = tkinter.simpledialog.askstring("Edit Outside Line Color","Enter New Outside Line Color:")
        self.__model_outside.set_line_color(outside_line_color)
        return outside_line_color
    def edit_outside_shape_fill_color(self):
        outside_fill_color = tkinter.simpledialog.askstring("Edit Outside Fill Color", "Enter New Outside Fill Color")
        self.__model_outside.set_fill_color(outside_fill_color)
    def edit_inside_shape_length(self):
        inside_length = tkinter.simpledialog.askfloat("Edit Inside Shape Length", "Enter New Inside Length:")
        self.__model_inside.set_length(inside_length)
    def edit_inside_shape_height(self):
        inside_height = tkinter.simpledialog.askfloat("Edit Inside Shape Height", "Enter New Inside Height:")
        self.__model_inside.set_height(inside_height)
    def edit_inside_shape_line_color(self):
        inside_line_color = tkinter.simpledialog.askstring("Edit Inside Line Color", "Enter New Inside Line Color:")
        self.__model_inside.set_line_color(inside_line_color)
    def edit_inside_shape_fill_color(self):
        inside_fill_color = tkinter.simpledialog.askstring("Edit Inside Fill Color", "Enter New Inside Fill Color:")
        self.__model_inside.set_fill_color(inside_fill_color)

    # # Pickle File Editing
    # def edit_pickle_outside_shape_radius(self):
    #     outside_radius = tkinter.simpledialog.askfloat("Edit Outside Radius", "Enter New Outside Radius:")
        
    # def edit_pickle_outside_shape_line_color(self):
    #     outside_line_color = tkinter.simpledialog.askstring("Edit Outside Line Color","Enter New Outside Line Color:")
    #     self.__default_circle_line_color = outside_line_color
    # def edit_pickle_outside_shape_fill_color(self):
    #     outside_fill_color = tkinter.simpledialog.askstring("Edit Outside Fill Color", "Enter New Outside Fill Color")
    #      outside_fill_color
    # def edit_pickle_inside_shape_length(self):
    #     inside_length = tkinter.simpledialog.askfloat("Edit Inside Shape Length", "Enter New Inside Length:")
    #     return inside_length
    # def edit_pickle_inside_shape_height(self):
    #     inside_height = tkinter.simpledialog.askfloat("Edit Inside Shape Height", "Enter New Inside Height:")
    #     return inside_height
    # def edit_pickle_inside_shape_line_color(self):
    #     inside_line_color = tkinter.simpledialog.askstring("Edit Inside Line Color", "Enter New Inside Line Color:")
    #     return inside_line_color
    # def edit_pickle_inside_shape_fill_color(self):
    #     inside_fill_color = tkinter.simpledialog.askstring("Edit Inside Fill Color", "Enter New Inside Fill Color:")
    #     return inside_fill_color



ApplicationController("d", "e", "c")
