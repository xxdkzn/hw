from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees
from colorama import init, Fore, Style

if __name__ == '__main__':
    print("Calling calculate_salary():")
    calculate_salary()
    print("Calling get_employees():")
    get_employees()

    init()  # Инициализируем colorama
    current_date = datetime.now().strftime('%Y-%m-%d %A %H:%M')
    print(f"{Fore.GREEN}Current date: {current_date}{Style.RESET_ALL}")
    print(f"{Fore.BLUE}Calling calculate_salary(){Style.RESET_ALL}:")
    calculate_salary()
    print(f"{Fore.BLUE}Calling get_employees(){Style.RESET_ALL}:")
    get_employees()