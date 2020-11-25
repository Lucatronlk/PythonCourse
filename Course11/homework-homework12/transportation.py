class Transport:
    def __init__(self, consumption, speed, capacity, transport_type, wheels):
        self.number_of_wheels = wheels
        self.consumption = consumption  # litrii pe suta de km
        self.mileage = 0
        self.speed = speed  # km/h
        self.type = transport_type
        self.capacity = capacity  # capacity of people


class PeopleTransport(Transport):
    def __init__(self, consumption, speed, capacity, wheels):
        #call the parent init
        super().__init__(consumption, speed, capacity, 'people', wheels)


class Bus(PeopleTransport):
    def __init__(self):
        #call the parent init
        super().__init__(15, 40, 50, 4)


class Car(PeopleTransport):
    def __init__(self):
        # call the parent init
        super().__init__(6, 60, 4, 4)


class Morgan(PeopleTransport):
    def __init__(self):
        #call the parent init
        super().__init__(3, 30, 4, 3)

class Minivan(Transport):
    def __init__(self):
        #call the parent __init__
         super().__init__(10, 50, 30, 'electronics', 4)

class FoodTransport(Transport):
    def __init__(self, consumption, speed, delivery_time):
        #call the parent init
        super().__init__(consumption, speed, 1, 'food', 2)
        self.delivery_time = delivery_time

class Bicycle(FoodTransport):
    def __init__(self):
        #call the parent init
      super().__init__(0, 20, 20)


class Motorcycle(FoodTransport):
    def __init__(self):
        #call the parent init
        super().__init__(3, 80, 10)

# bus = Bus()
# car = Car()
# minivan = Minivan()
# bicycle = Bicycle()
# motorcycle = Motorcycle()
# morgan = Morgan()
# print(bus.__dict__)
# print(car.__dict__)
# print(minivan.__dict__)
# print(bicycle.__dict__)
# print(motorcycle.__dict__)
# print(morgan.__dict__)