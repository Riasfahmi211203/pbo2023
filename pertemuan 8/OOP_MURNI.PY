import tkinter as tk
from tkinter import Label, Entry, Button

class CelsiusConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Celsius Converter")

        self.celsius_label = Label(root, text="Masukkan suhu Celsius:")
        self.celsius_label.pack()

        self.celsius_entry = Entry(root)
        self.celsius_entry.pack()

        self.convert_button = Button(root, text="Konversi", command=self.convert)
        self.convert_button.pack()

        self.result_label = Label(root, text="")
        self.result_label.pack()

    def convert(self):
        try:
            celsius = float(self.celsius_entry.get())
            converter = CelsiusConverter(celsius)
            fahrenheit = converter.get_fahrenheit()
            reamur = converter.get_reamur()
            kelvin = converter.get_kelvin()

            result_text = (
                f"{celsius} Celsius, sama dengan:\n"
                f"{fahrenheit} Fahrenheit\n"
                f"{reamur} Reamur\n"
                f"{kelvin} Kelvin"
            )

            self.result_label.config(text=result_text)

        except ValueError as e:
            self.result_label.config(text=f"Error: {e}")
        except Exception as e:
            self.result_label.config(text=f"An error occurred: {e}")

class CelsiusConverter:
    def __init__(self, celsius):
        self.celsius = celsius

    def get_fahrenheit(self):
        return (9/5 * self.celsius) + 32

    def get_reamur(self):
        return (4/5 * self.celsius)

    def get_kelvin(self):
        return self.celsius + 273

if __name__ == "__main__":
    root = tk.Tk()
    app = CelsiusConverterApp(root)
    root.mainloop()
