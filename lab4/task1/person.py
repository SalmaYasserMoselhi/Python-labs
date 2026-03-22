class Person:
    moods = ("happy", "tired", "lazy")

    def __init__(self, name, money=0, mood="happy", healthRate=100):
        self.name       = name
        self.money      = money
        self.mood       = mood
        self.healthRate = healthRate

    @property
    def healthRate(self):
        return self.__healthRate

    @healthRate.setter
    def healthRate(self, value):
        if value > 100:
            self.__healthRate = 100
        elif value < 0:
            self.__healthRate = 0
        else:
            self.__healthRate = value

    def sleep(self, hours):
        if hours == 7:
            self.mood = Person.moods[0]
        elif hours < 7:
            self.mood = Person.moods[1]
        else:
            self.mood = Person.moods[2]

    def eat(self, meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50

    def buy(self, items):
        cost = items * 10
        self.money -= cost

    def __str__(self):
        return f"Person(name:{self.name}, mood:{self.mood}, health:{self.healthRate}%)"