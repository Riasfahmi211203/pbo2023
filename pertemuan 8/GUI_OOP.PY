import tkinter as tk
from tkinter import Label, Entry, Button,W, Frame, BOTH, YES
from TemperatureConverterCelcius import *

class TemperatureConverterApp:
    def __init__(self, parent, title):
        self.parent = parent
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.create_widgets()

    def create_widgets(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        self.celsius_label = Label(mainFrame, text="Enter temperature in Celsius:")
        self.celsius_label.grid(row=0, column=0, sticky=W, padx=10, pady=10)

        self.celsius_entry = Entry(mainFrame)
        self.celsius_entry.grid(row=0, column=1, padx=10, pady=10)

        self.convert_button = Button(mainFrame, text="Convert", command=self.convert)
        self.convert_button.grid(row=1, column=1, padx=10, pady=10)

        self.result_label = Label(mainFrame, text="Fahrenheit")
        self.result_label.grid(row=2, column=0, padx=10, pady=10)
        
        self.fahrenheit_entry = Entry(mainFrame)
        self.fahrenheit_entry.grid(row=2, column=1, padx=10, pady=10)
        
        self.kelvin_label = Label(mainFrame, "Kelvin")
        self.kelvin_label.grid(row=3, column=0, sticky=W, padx=10, pady=10)
        
        self.kelvin_entry = Entry(mainFrame)
        self.kelvin_entry.grid(row=3, column=1, padx=10, pady=10)
        
        self.reamur_label = Label(mainFrame, "Reamur")
        self.reamur_label.grid(row=4, column=0, sticky=W, padx=10, pady=10)
        
        self.reamur_reamur = Entry(mainFrame)
        self.reamur_reamur.grid(row=4, column=1, padx=10, pady=10)

    def convert(self):
        C = C.celsius(int(self.celsius_entry.get()))
        
        F = C.get_fahrenheit()
            
    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverterApp(root, title="Celcius")
    root.mainloop()
