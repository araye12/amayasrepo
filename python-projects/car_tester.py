from car import Car

# create list for car objects 
car_object = []

# read in file in create five car objects, store objects in the list

with open ('cars.txt') as file:
    for line in file:
        line = line.split()
        color = line[0]
        engine_type = line[1]
        gas_tank = line[2]
        odometer = line[3]
        car = Car(color, engine_type, int(gas_tank), int(odometer))
        car_object.append(car)
        print(car)

first_car = car_object[0]     #first car is stored in index 0 of the list 
second_car = car_object[1]    #second car is stored in index 1 of the list 

#Call methods

first_car.drive()
second_car.drive()

print(f"First car: {first_car}, Engine type: {engine_type}, Gas Tank: {first_car.get_gas_tank()}, Odomoter: {first_car.get_odometer()}")
print(f"Second car: {second_car}, Engine type: {engine_type}, Gas Tank: {second_car.get_gas_tank()}, Odomoter: {second_car.get_odometer()}")