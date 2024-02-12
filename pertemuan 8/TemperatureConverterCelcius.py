class TemperatureConverter:
    def __init__(self, celsius):
        self.celsius = celsius

    def get_fahrenheit(self):
        val = (9/5 * self.celsius) + 32
        return val

    def get_reamur(self):
        val = (4/5 * self.celsius)
        return val
    
    def get_kelvin(self):
        val = self.celsius + 273
        return val