import random
import string


def get_employees():
    print("Retrieving list of employees...")

    # Логика получения списка сотрудников
    employees = []
    for _ in range(10):
        first_name = ''.join(random.choices(string.ascii_uppercase, k=5))
        last_name = ''.join(random.choices(string.ascii_uppercase, k=7))
        employee = f"{first_name} {last_name}"
        employees.append(employee)

    # Вывод списка сотрудников
    print("List of employees:")
    for employee in employees:
        print(employee)

    print("Employee list retrieved.")