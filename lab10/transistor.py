class Transistor:
    def __init__(self, type: str, model: str, current_max: int, voltage_max: int) -> None:
        self.type = type
        self.model = model
        self.current_max = current_max
        self.voltage_max = voltage_max

    def __str__(self) -> str:
        return f'Transistor  type: {self.type}, brand: {self.model}, current_max = {self.current_max}, voltage_max = {self.voltage_max}. '
