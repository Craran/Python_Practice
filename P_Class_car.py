class Car:
    """a simple try to simulate car"""

    def __init__(self, make, model, year):
        """initialize the attribute of car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def read_odometer(self):
        """print a message to show the odometer of the car"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def get_descriptive_name(self):
        """return a concise descriptive message"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def update_odometer(self, mileage):
        """set the odometer to a specific value"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cant roll back an odometer!")

    def increment_odometer(self, miles):
        """put an specific increment on odometer"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You cant roll back an odometer!")


my_new_car = Car('subaru', 'outback', 2020)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(2000.5)
my_new_car.read_odometer()

my_new_car.increment_odometer(43.275)
my_new_car.read_odometer()
