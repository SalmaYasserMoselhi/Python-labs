from person import Person
from car import Car
from employee import Employee
from office import Office

fiat128 = Car("Fiat 128", fuelRate=100, velocity=80)

samy  = Employee("Samy",  1, 3000, "samy@iti.com",  distanceToWork=20, car=fiat128)
ahmed = Employee("Ahmed", 2, 2500, "ahmed@iti.com",  distanceToWork=15)
sara  = Employee("Sara",  3, 2000, "sara@iti.com",   distanceToWork=30)


iti = Office("ITI Smart Village")
iti.hire(samy)
iti.hire(ahmed)
iti.hire(sara)
print(iti)


print("sleep & eat")
samy.sleep(7)
samy.eat(3)
print(samy)


print("\nwork")
samy.work(8)
print(f"Samy's mood after 8h work is {samy.mood}")


print("\ndrive")
samy.drive(samy.distanceToWork)
print(fiat128)


print("\nrefuel")
samy.refuel(50)
print(fiat128)
print("\ncheck lateness")
iti.check_lateness(empId=1, moveHour=8)
iti.check_lateness(empId=2, moveHour=8.5)

print("\ndeduct & reward")
iti.deduct(1, 200)
iti.reward(2, 300)

print("\nfire")
iti.fire(3)
print(iti)

iti.save_to_json()