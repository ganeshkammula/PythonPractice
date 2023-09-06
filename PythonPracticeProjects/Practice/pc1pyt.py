employee1 = {
    "name": "Ganesh",
    "age": 38,
    "position": "developer",
    "salary": 1200
}

employee2 = {
    "name": "Sai",
    "age": 44,
    "position": "tester",
    "salary": 1000
}


def increase_salary(employee, percent):
    employee['salary'] += employee['salary'] * (percent / 100)


def employee_info(employee):
    print(f"{employee['name']} is {employee['age']} years old. Employee is a {employee['position']}"
          f" with the salary of ${employee['salary']}")


employees = [employee1, employee2]
increase_salary(employee2, 20)
for e in employees:
    employee_info(e)
