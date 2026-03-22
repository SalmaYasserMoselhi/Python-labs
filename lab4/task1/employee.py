import re
from person import Person

class Employee(Person):
    EMAIL_REGEX = r'^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$'

    def __init__(self, name, emp_id, salary, email, distanceToWork=20,
                 car=None, money=0, mood="happy", healthRate=100):
        super().__init__(name, money, mood, healthRate)
        self.id             = emp_id
        self.car            = car
        self.salary         = salary
        self.email          = email
        self.distanceToWork = distanceToWork

    @property
    def salary(self):
        return self.__salary
 
    @salary.setter
    def salary(self, value):
        if value < 1000:
            print("Salary is too low, must be >= 1000")
        else:
            self.__salary = value

    @property
    def email(self):
        return self.__email
 
    @email.setter
    def email(self, value):
        if re.match(Employee.EMAIL_REGEX, value):
            self.__email = value
        else:
            print(f"'{value}' is not a valid email")
            self.__email = None

    def work(self, hours):
        if hours == 8:
            self.mood = Person.moods[0] #happy
        elif hours > 8:
            self.mood = Person.moods[1] #tired
        else:
            self.mood = Person.moods[2] #lazy

    def drive(self, distance):
        if self.car is None:
            print(f"{self.name} has no car")
            return
        self.car.run(self.car.velocity, distance)

    def refuel(self, gasAmount=100):
        if self.car is None:
            print(f"{self.name} has no car to refuel")
            return
        new_fuel = self.car.fuelRate + gasAmount
        self.car.fuelRate = min(new_fuel, 100)

    def send_mail(self, to, subject, msg, receiver_name):
        content = (
            f"From: {self.email}\n"
            f"To: {to}\n"
            f"\n"
            f"Hi, {receiver_name}\n"
            f"{msg}\n"
            f"\nthanks"
        )
        filename = subject.replace(" ", "_") + ".txt"
        with open(filename, "w") as f:
            f.write(content)
        print(f"Email saved as '{filename}'")

    def __str__(self):
        return (f"Employee(id:{self.id}, name:{self.name}, "
                f"salary:{self.salary}, mood:{self.mood})")