class Car:
    num_wheels = 4

    def __init__(self, color, style):
        self.color = color
        self.style = style
        self.speed = 0

    def change_speed(self, speed):
        self.speed = speed

    def change_color(self, color):
        self.color = color

# my_car = Car(color="Black", style= "Sedan")
# your_car = Car(color="White", style= "Hatchback")
# her_car = Car(color="Red", style= "SUV")

# print(my_car.color)
# my_car.change_color("Orange")
# print(my_car.color)
# print(my_car.style)
# print(my_car.num_wheels)

class FuelCar(Car):

    def __init__(self, color, style, fuel_type):
        super().__init__(color, style)
        self.fuel_type = fuel_type

    def change_fuel_type(self, fuel_type):
         self.fuel_type = fuel_type

class ElectricCar(Car):
    def __init__(self, color, style, fuel_type):
        super().__init__(color, style)
        self.fuel_type = fuel_type

my_car = FuelCar(color = "Black", style = "Sedan", fuel_type = "Gas_online")
my_car.change_fuel_type("Diesel")
my_car.change_speed(200)

print(my_car.fuel_type)
print(my_car.speed)

