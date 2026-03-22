class Car:
    def __init__(self, name, fuelRate=100, velocity=0):
        self.name     = name
        self.fuelRate = fuelRate
        self.velocity = velocity

    @property
    def fuelRate(self):
        return self.__fuelRate
 
    @fuelRate.setter
    def fuelRate(self, value):
        if value > 100 or value < 0:
            print("Fuel rate is invalid, must be between 0 and 100")
        else:
            self.__fuelRate = value

    @property
    def velocity(self):
        return self.__velocity
 
    @velocity.setter
    def velocity(self, value):
        if value > 200 or value < 0:
            print("Velocity is invalid, must be between 0 and 200")
        else:
            self.__velocity = value

    def run(self, velocity, distance):
        self.velocity = velocity 
        max_km = self.fuelRate
        if max_km >= distance:
            fuel_used = (distance // 10) * 10
            self.fuelRate -= fuel_used
            remain = 0
        else:
            remain = distance - max_km
            self.fuelRate = 0
        self.stop(remain)

    def stop(self, remainDistance=0):
        self.velocity = 0
        if remainDistance == 0:
            print(f"Arrived successfully with fuel rate {self.fuelRate}%")
        else:
            print(f"Ran out of fuel, {remainDistance}km away from destination")

    def __str__(self):
        return f"Car({self.name}, fuel={self.fuelRate}%, velocity={self.velocity}km/h)"
