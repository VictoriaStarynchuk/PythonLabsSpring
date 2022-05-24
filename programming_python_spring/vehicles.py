from abc import ABC, abstractmethod


class Vehicles(ABC):
    def __init__(self, type_of_vehicles: str, name: str):
        self.type_of_vehicles = type_of_vehicles
        self.name = name

    @abstractmethod
    def ride(self) -> None:
        pass
