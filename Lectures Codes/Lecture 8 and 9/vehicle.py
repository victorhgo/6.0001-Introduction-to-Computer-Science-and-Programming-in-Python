class Vehicle(object):
    def __init__(self):
        pass

    # Standard methods for class Vehicle
    def start(self):
        return "Vehicle is starting..."
    def stop(self):
        return "Vehicle is stopping..."
    
class Car(Vehicle):
    def start(self):
        return "Car is starting..."
    def stop(self):
        return "Car is stopping..."
    
class Bike(Vehicle):
    def start(self):
        return "Bike is starting..."
    def stop(self):
        return "Bike is stopping..."
    
def operateVehicle(vehicle):
    return vehicle.start() + " " + vehicle.stop()
    
    
car = Car()
bike = Bike()

# Test object car
assert car.start() == "Car is starting..."
assert car.stop() == "Car is stopping..."
assert operateVehicle(car) == "Car is starting... Car is stopping..."

print(operateVehicle(car))
# Test object bike
assert bike.start() == "Bike is starting..."
assert bike.stop() == "Bike is stopping..."
assert operateVehicle(bike) == "Bike is starting... Bike is stopping..."

print(operateVehicle(bike))