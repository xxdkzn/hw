import random


def calculate_salary():
    print("Calculating employee salaries...")

    # Логика расчета заработной платы
    salaries = {}
    for employee_id in range(1, 11):
        base_salary = random.randint(40000, 80000)
        bonus = random.randint(0, 10000)
        total_salary = base_salary + bonus
        salaries[f"Employee {employee_id}"] = total_salary

    # Вывод рассчитанных зарплат
    for employee, salary in salaries.items():
        print(f"{employee} - {salary} руб.")

    print("Salaries calculated successfully.")