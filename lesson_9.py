import threading
import os


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()

    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


class Vehicle(object):
    def __init__(self, body, top_speed, miles, color, year, price):
        self.body = body
        self.top_speed = top_speed
        self.speed = 0
        self.miles = miles
        self.color = color
        self.year = year
        self.price = price
        self.drive_interval = 0
        self.acc_interval = 0

    @staticmethod
    def vehicle_information():
      print(
        'The attributes of a vehicle are: body type, top speed calculated in miles/h, distance driven, paint finish, the year and price')

    def vehicle_history(self):
        if self.year == 2020:
            print('brand new')
        else:
            print('second hand')

    def drive(self):
        if self.speed > 0:
            self.miles += self.speed / (self.speed * 60 * 60)
        print('Driving with {} miles/h'.format(self.speed))

    def accelerate(self):
        def increment():
            if self.speed < self.top_speed:
                self.speed += 111
            else:
                self.stop()
        self.acc_interval = set_interval(increment, 1)

    def start(self):
        self.drive_interval = set_interval(self.drive, 1)
        self.accelerate()
        print('Started the vehicle, miles: {}'.format(self.miles))

    def stop(self):
        print('Stopped the vehicle, new mileage: {}'.format(self.miles))
        os._exit(0)


print('Adding vehicle class car : maserati')
maserati = Vehicle('car', 230, 89000, 'green', 2020, 111111)
maserati.vehicle_history()
maserati.vehicle_information()



class Motorcycle(Vehicle):
    def __init__(self, body, top_speed, miles, color, year, price):
        super().__init__(body, top_speed, miles, color, year, price)

    def vehicle_top_speed(self):
        if self.top_speed < 300:
            print('Slow poke')
        else:
            print('Speed demon')


print('Adding vehicle class motorcycle : dodge')
dodge = Motorcycle('bike', 333, 0, 'metallic green', 1989, 11111)
dodge.vehicle_history()
dodge.start()
dodge.vehicle_top_speed()