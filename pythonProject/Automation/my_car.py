from car import Car

my_new_car = Car('Fortuner', 'Legender', 2020)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 150
my_new_car.read_odometer()
