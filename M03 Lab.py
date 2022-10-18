"""
Matthew Hayden
M03 Lab
Program that asks the user for various information about their car and uses two classes to store the info and print it.
Variables:
   Vehicle class: class that determines the vehicle type.
   Automobile class: class that stores the different specifications of the user and outputs them
   info method returns the printed list of car specifications.
   year, make, model, doors, roof variables: each take the input of the user for a different car spec and stores it into its respective variable
"""
class Vehicle():
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year= year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    def info(self):
        return print(f'Vehicle type: {self.vehicle_type}\nYear: {self.year}\nMake: {self.make}\nModel: {self.model}\nNumber of doors: {self.doors}\nType of roof: {self.roof}')

year=input("What is the year of the vehicle? ")
make=input("What is the make of the vehicle? ")
model=input("What is the model of the vehicle? ")
doors=input("How many doors does the vehicle have? ")
roof=input("Does the vehicle have a roof? ")

Automobile("Car",year,make,model,doors,roof).info()