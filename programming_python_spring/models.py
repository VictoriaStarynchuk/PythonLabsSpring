from vehicles import Vehicles


class Plane(Vehicles):
    def __init__(self, type_of_vehicles: str, name: str, capacity_of_people: int):
        super().__init__(type_of_vehicles, name)
        self.capacity_of_people = capacity_of_people

    def __str__(self) -> str:
        return "Vehicles: {}, type:  {}, capacity of people: {}.".format(self.name, self.type_of_vehicles,
                                                                         self.capacity_of_people)

    def ride(self) -> None:
        print("In the sky!")


class Car(Vehicles):
    def __init__(self, type_of_vehicles: str, name: str, colour: str, brand: str):
        super().__init__(type_of_vehicles, name)
        self.colour = colour
        self.brand = brand

    def __str__(self) -> str:
        return "Vehicles: {}, type:  {}, colour: {}, brand: {}.".format(self.name, self.type_of_vehicles,
                                                                        self.colour, self.brand)

    def ride(self) -> None:
        print("On the road!")


class Bus(Vehicles):
    def __init__(self, type_of_vehicles: str, name: str, is_second_floored: bool):
        super().__init__(type_of_vehicles, name)
        self.is_second_floored = is_second_floored

    def __str__(self) -> str:
        return "Vehicles: {}, type:  {}, second floor: {}.".format(self.name, self.type_of_vehicles,
                                                                   self.is_second_floored)

    def ride(self) -> None:
        print("On the highway!")


class Tram(Vehicles):
    def __init__(self, type_of_vehicles: str, name: str, number_of_wagons: int):
        super().__init__(type_of_vehicles, name)
        self.number_of_wagons = number_of_wagons

    def __str__(self) -> str:
        return "Vehicles: {}, type:  {}, number of wagons: {}.".format(self.name, self.type_of_vehicles,
                                                                       self.number_of_wagons)

    def ride(self) -> None:
        print("On the railway!")


class Trolleybus(Vehicles):
    def __init__(self, type_of_vehicles: str, name: str, is_for_disable_people: bool):
        super().__init__(type_of_vehicles, name)
        self.is_for_disable_people = is_for_disable_people

    def __str__(self) -> str:
        return "Vehicles: {}, type:  {}, for disabled people: {}.".format(self.name, self.type_of_vehicles,
                                                                          self.is_for_disable_people)

    def ride(self) -> None:
        print("On the road using wires!")
