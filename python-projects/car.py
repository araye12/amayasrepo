class Car:
    # __init__ method is like the constructor in Java
    # instance variales declared in the __init__ method are global and MUST
    # be refereced using self
    # self is like 'this' in Java
    def __init__(self, color, engine_type, gas_type, odometer):
        self.color = color
        self.engine_type = engine_type
        self.gas_type = gas_type 
        self.odometer = odometer
    
    def __str__(self):
        return f"{self.color} has the engine type {self.engine_type}"
    
    def drive(self):
        if self.engine_type == "4_cylinder":
            self.gas_type -= 3
            self.odometer += 90
        elif self.engine_type == "v8":
            self.gas_type -= 4
            self.odometer += 50
        
    def get_gas_tank(self):
        return f"{self.gas_type}"
        
    def get_odometer(self):
        return f"{self.odometer}"

