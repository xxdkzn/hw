from application.salary import *
from application.db.people import *

if __name__ == '__main__':
    print("Calling calculate_salary():")
    calculate_salary()
    print("Calling get_employees():")
    get_employees()