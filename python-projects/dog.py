class Dog:
    def __init__(self, name, trick, breed, hungry):
        self.name = name
        self.trick = trick
        self.breed = breed
        self.hungry = hungry
    
    def __str__(self):
        return f"{self.name}: {self.breed}"
    
    def speak(self):
        return "Woof"
    
    def feed(self):
        if{self.breed} != False:
            return False
        return False
    
    def change_trick(self):
        return f"{self.trick()}"

    def get_name(self):
        return f"{self.name}"

    def get_breed(self):
        return f"{self.breed}"

    def get_trick(self):
        return f"{self.trick}"

    def isHungry(self):
        if {self.feed} == False:
            return False
        return False
        