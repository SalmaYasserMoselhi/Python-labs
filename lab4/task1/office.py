class Office:
    employeesNum = 0

    def __init__(self, name):
        self.name = name
        self.employees = []

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum += num

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        if velocity <= 0:
            print("Velocity must be greater than 0")
            return True
        travel_time = distance / velocity
        arrival_hour = moveHour + travel_time
        is_late = arrival_hour > targetHour
        return is_late

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empId):
        for emp in self.employees:
            if emp.id == empId:
                return emp
        print(f"Employee with id={empId} not found")
        return None

    def hire(self, employee):
        self.employees.append(employee)
        Office.change_emps_num(1)
        print(f"{employee.name} hired at {self.name}")

    def fire(self, empId):
        emp = self.get_employee(empId)
        if emp:
            self.employees.remove(emp)
            Office.change_emps_num(-1)
            print(f"{emp.name} fired from {self.name}")

    def deduct(self, empId, deduction):
        emp = self.get_employee(empId)
        if emp:
            emp.salary -= deduction
            print(f"Deducted {deduction} L.E from {emp.name}  "
                  f"salary now: {emp.salary} L.E")

    def reward(self, empId, reward):
        emp = self.get_employee(empId)
        if emp:
            emp.salary += reward
            print(f"Rewarded {reward} L.E to {emp.name}  "
                  f"salary now: {emp.salary} L.E")


    def check_lateness(self, empId, moveHour):
        emp = self.get_employee(empId)
        if not emp:
            return
        if emp.car is None:
            print(f"{emp.name} has no car, cannot check lateness")
            return

        is_late = Office.calculate_lateness(
            targetHour = 9,
            moveHour = moveHour,
            distance = emp.distanceToWork,
            velocity = emp.car.velocity if emp.car.velocity > 0 else 60
        )

        if is_late:
            self.deduct(empId, 10)
        else:
            self.reward(empId, 10)

    def __str__(self):
        result = f"\nOffice: {self.name}\n"
        for emp in self.employees:
            result += f"{emp}\n"
        return result

    def save_to_json(self):
        import json

        data = {
            "office": self.name,
            "total_employees": len(self.employees),
            "employees": []
        }

        for emp in self.employees:
            emp_dict = {
                "id": emp.id,
                "name": emp.name,
                "email": emp.email,
                "salary": emp.salary,
                "mood": emp.mood,
                "healthRate": emp.healthRate,
                "money": emp.money,
                "distanceToWork": emp.distanceToWork,
                "car": {
                    "name": emp.car.name,
                    "fuelRate": emp.car.fuelRate,
                    "velocity": emp.car.velocity
                } if emp.car else None
            }
            data["employees"].append(emp_dict)

        filename = self.name.replace(" ", "_") + ".json"
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

        print(f"Office data saved to '{filename}'")
        return filename