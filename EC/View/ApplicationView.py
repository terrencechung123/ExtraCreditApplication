# PROGRAMMER: Khiem Nguyen, Richie Nguyen, Terrence Chung

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
        self.__canvas = tkinter.Canvas(self.__application_frame, bg = "green", width = 800, height = 600)
        self.__canvas.pack()

    # INSTANCE METHODS
    def start(self):
        self.__application_window.mainloop()
    def application_window(self):
        return self.__application_window

    def show_outside_shape(self, radius, line_color, fill_color):
        # Clear canvas first
        self.__canvas.delete("all")
        # Draw outside shape, for example, a circle
        self.__canvas.create_oval((400 - radius / 2, 300 - radius / 2), (400 + radius / 2, 300 + radius / 2), outline= line_color, fill= fill_color)
        # Other drawing operations as needed

    def show_inside_shape(self, length, height, line_color, fill_color):
        # Clear canvas first
        self.__canvas.delete("all")
        # Draw inside shape, for example, a rectangle
        self.__canvas.create_rectangle((400 - length / 2, 300 - height / 2), (400 + length / 2, 300 + length / 2), outline=line_color, fill=fill_color)
        # Other drawing operations as needed

    def get_about(self):
        tkinter.messagebox.showinfo("Application Extra Credit", "Spring Semester 2024")
        self.__application_window.update()