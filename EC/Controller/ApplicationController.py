# PROGRAMMER: Khiem Nguyen, Richie Nguyen, Terrence Chung

# IMPORT STATEMENTS
import tkinter
import pickle
import tkinter.filedialog
import tkinter.messagebox
import json
import xml.etree.ElementTree as ET

class ApplicationController():
    # CONSTRUCTOR
    def __init__(self, model_outside, model_inside, view):
        self.__default_circle_radius = 100
        self.__default_circle_line_color = "black"
        self.__default_circle_fill_color = "red"

        self.__default_rectangle_length = 100
        self.__default_rectangle_height = 200
        self.__default_rectangle_line_color = "black"
        self.__default_rectangle_fill_color = "red"

        self.__model_outside = model_outside
        self.__model_inside = model_inside
        self.__view = view

        self.__application_menu = tkinter.Menu(self.__view.application_window())

        # File menu
        self.__file_menu = tkinter.Menu(self.__application_menu)
        self.__file_menu.add_command(label="New", command=self.file_new)
        self.__file_menu.add_command(label="Open", command=self.file_open)
        self.__file_menu.add_command(label="Save as XML", command=self.file_save_xml)
        self.__file_menu.add_command(label="Save as JSON", command=self.file_save_json)
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
        self.__help_menu.add_command(label="About", command=self.__view.get_about)
        self.__application_menu.add_cascade(label="Help", menu=self.__help_menu)
        self.__view.application_window()["menu"] = self.__application_menu
        self.__view.application_window().mainloop()

    # INSTANCE METHODS
    def view_outside_shape(self):
        radius = self.__model_outside.get_radius()
        line_color = self.__model_outside.get_line_color()
        fill_color = self.__model_outside.get_fill_color()
        self.__view.show_outside_shape(radius, line_color, fill_color)

    def view_inside_shape(self):
        length = self.__model_inside.get_length()
        height = self.__model_inside.get_height()
        line_color = self.__model_inside.get_line_color()
        fill_color = self.__model_inside.get_fill_color()
        self.__view.show_inside_shape(length, height, line_color, fill_color)

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
        file_path = tkinter.filedialog.askopenfilename(filetypes=[("Pickle files", "*.pickle")])
        if file_path:
            with open(file_path, "rb") as binary_file_input:
                data = pickle.load(binary_file_input)
                tkinter.messagebox.showinfo("File Opened", f"Data: {data}")

    def file_save_xml(self):
        
        parent_root = ET.Element("ApplicationData")

        root1 = ET.SubElement(parent_root, "Circle")
        var1_element = ET.SubElement(root1, "Radius")
        var1_element.text = str(self.__model_outside.get_radius())
        var2_element = ET.SubElement(root1, "LineColor")
        var2_element.text = self.__model_outside.get_line_color()
        var3_element = ET.SubElement(root1, "FillColor")
        var3_element.text = self.__model_outside.get_fill_color()

        root2 = ET.SubElement(parent_root, "Rectangle")
        var1_element = ET.SubElement(root2, "Length")
        var1_element.text = str(self.__model_inside.get_length())
        var2_element = ET.SubElement(root2, "Height")
        var2_element.text = str(self.__model_inside.get_height())
        var3_element = ET.SubElement(root2, "LineColor")
        var3_element.text = self.__model_inside.get_line_color()
        var4_element = ET.SubElement(root2, "FillColor")
        var4_element.text = self.__model_inside.get_fill_color()

        tree = ET.ElementTree(parent_root)
        tree.write("ApplicationData.xml", encoding='utf-8', xml_declaration=True)

    def file_save_json(self):
        json_values = { 
            "outside_shape" : {},
            "inside_shape" : {}
        }
        
        json_values["outside_shape"]["radius"] = self.__model_outside.get_radius()
        json_values["outside_shape"]["line_color"] = self.__model_outside.get_line_color()
        json_values["outside_shape"]["fill_color"] = self.__model_outside.get_fill_color()
        
        json_values["inside_shape"]["length"] = self.__model_inside.get_length()
        json_values["inside_shape"]["height"] = self.__model_inside.get_height()
        json_values["inside_shape"]["line_color"] = self.__model_inside.get_line_color()
        json_values["inside_shape"]["fill_color"] = self.__model_inside.get_fill_color()
        
        save_file = open("ApplicationData.json", "w")
        json.dump(json_values, save_file, indent = 6)
        save_file.close()

    def edit_outside_shape_radius(self):
        outside_radius = tkinter.simpledialog.askfloat("Edit Outside Radius", "Enter New Outside Radius:")
        self.__model_outside.set_radius(outside_radius)
    def edit_outside_shape_line_color(self):
        outside_line_color = tkinter.simpledialog.askstring("Edit Outside Line Color","Enter New Outside Line Color:")
        self.__model_outside.set_line_color(outside_line_color)
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

    # Pickle File Editing
    def edit_pickle_outside_shape_radius(self):
        outside_radius = tkinter.simpledialog.askfloat("Edit Outside Radius", "Enter New Outside Radius:")
        self.__default_circle_radius = outside_radius
        self.file_new()
        
    def edit_pickle_outside_shape_line_color(self):
        outside_line_color = tkinter.simpledialog.askstring("Edit Outside Line Color","Enter New Outside Line Color:")
        self.__default_circle_line_color = outside_line_color
        self.file_new()

    def edit_pickle_outside_shape_fill_color(self):
        outside_fill_color = tkinter.simpledialog.askstring("Edit Outside Fill Color", "Enter New Outside Fill Color")
        self.__default_circle_fill_color = outside_fill_color
        self.file_new()

    def edit_pickle_inside_shape_length(self):
        inside_length = tkinter.simpledialog.askfloat("Edit Inside Shape Length", "Enter New Inside Length:")
        self.__default_rectangle_length = inside_length
        self.file_new()
        
    def edit_pickle_inside_shape_height(self):
        inside_height = tkinter.simpledialog.askfloat("Edit Inside Shape Height", "Enter New Inside Height:")
        self.__default_rectangle_height = inside_height
        self.file_new()

    def edit_pickle_inside_shape_line_color(self):
        inside_line_color = tkinter.simpledialog.askstring("Edit Inside Line Color", "Enter New Inside Line Color:")
        self.__default_rectangle_line_color = inside_line_color
        self.file_new()

    def edit_pickle_inside_shape_fill_color(self):
        inside_fill_color = tkinter.simpledialog.askstring("Edit Inside Fill Color", "Enter New Inside Fill Color:")
        self.__default_rectangle_fill_color = inside_fill_color
        self.file_new()
        
        
