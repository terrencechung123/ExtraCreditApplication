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
        self.__application_window.geometry("1000x500")


        self.__application_frame = tkinter.ttk.Frame(self.__application_window)
        self.__application_frame.pack()
        self.__Canvas = tkinter.Canvas(self.__application_frame, bg = "green", width = 800, height = 600)
        self.__Canvas.pack()
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
    def start(self):
        self.__application_window.mainloop()
    def application_window(self):
        return self.__application_window

    def show_outside_shape(self):
    # Clear canvas first
        self.__Canvas.delete("all")
        # Draw outside shape, for example, a circle
        self.__Canvas.create_oval(100, 100, 400, 400, outline="blue", fill="red")
        # Other drawing operations as needed

    def show_inside_shape(self):
        # Clear canvas first
        self.__Canvas.delete("all")
        # Draw inside shape, for example, a rectangle
        self.__Canvas.create_rectangle(200, 200, 600, 400, outline="blue", fill="green")
        # Other drawing operations as needed