
class Passenger:
    def __init__(self, name):
        self.name = name


class Flight:
    def __init__(self):
        self.passengers = []  

    def add_passenger(self, passenger_obj):
        self.passengers.append(passenger_obj)
p1 = Passenger("Ali")
p2 = Passenger("Sara")

flight = Flight()
flight.add_passenger(p1)
flight.add_passenger(p2)

for p in flight.passengers:
    print(p.name)