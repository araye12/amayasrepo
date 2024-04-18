from dog import Dog

dog_object = []

with open ('dogs.txt') as file:
    for line in file:
        line = line.split()
        name = line[0]
        trick = line[1]
        breed = line[2]
        hungry = line[3]
        dog = Dog(name, trick, breed, hungry)
        dog_object.append(dog)
        print(dog)

first_dog = dog_object[0]     
second_dog = dog_object[1]     

#Call methods

print(f"First dog: {first_dog}, Name: {first_dog.get_name()}, Breed: {first_dog.get_breed()}, Trick: {first_dog.get_trick()}, Hungry: {first_dog.isHungry()}")

print(f"First dog: {first_dog}, Name: {first_dog.get_name()}, Breed: {first_dog.get_breed()}, Speak: {first_dog.speak()}, Feed: {first_dog.feed()} Trick: {first_dog.get_trick()}, Hungry: {first_dog.isHungry()}")
