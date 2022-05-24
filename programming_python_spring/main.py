from models import Plane, Car, Bus, Tram, Trolleybus

if __name__ == '__main__':
    plane = Plane("air vehicle", "plane", 500 )
    car = Car("land vehicle", "car", "black", "audi")
    bus = Bus("public transport", "bus", is_second_floored = True )
    tram = Tram("public transport", "tram", 2)
    trolley = Trolleybus("public transport", "trolley", is_for_disable_people = True)
    print(plane.__str__())
    plane.ride()
    print(bus.__str__())
    bus.ride()


