class Chainsaw:
    def __init__(self, brand, power, fuel_tank_capacity, fuel_level):
        self.brand = brand
        self.power = power
        self.fuelTankCapacity = fuel_tank_capacity
        self.fuelLevel = fuel_level
        self.isWorking = False

    def start(self):
        self.isWorking = True

    def stop(self):
        self.isWorking = False

    def cutWood(self, length):
        fuel_consumption = length * 0.1
        if self.fuelLevel >= fuel_consumption:
            self.fuelLevel -= fuel_consumption
        else:
            self.fuelLevel = 0
            self.isWorking = False

my_chainsaw = Chainsaw("Husqvarna", 2000, 2.5, 2.0)

my_chainsaw.start()

print(my_chainsaw.isWorking)

my_chainsaw.cutWood(3)

print(my_chainsaw.fuelLevel)

my_chainsaw.stop()

print(my_chainsaw.isWorking)
