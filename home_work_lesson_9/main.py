#Ex 1



def fibonacci(n):
    fn_list = [0, 1]
    for i in range(2, n):
        fn_list.append(fn_list[i-1] + fn_list[i-2])
    return fn_list

def fib_test():
    check_num = int(input("Add amount of Fibonacci Sequences"))
    print(fibonacci(check_num))

# fib_test()


#Ex 2 partial
import json

def list_names():
    try:
        file = open('employee_list.json', 'r')
        data = file.read()
        names = json.loads(data)
        names_list = [el['name'] for el in names]
    except FileNotFoundError:
        names = []
    return names_list

def list_positions():
    try:
        file = open('employee_list.json', 'r')
        data = file.read()
        position_names = json.loads(data)
        position_names_list = [el['position'] for el in position_names]
    except FileNotFoundError:
        names = []
    return position_names_list

def salary_budget():
    try:
        file = open('employee_list.json', 'r')
        data = file.read()
        employee_list = json.loads(data)
        salaries_list = [el['salary'] for el in employee_list]
    except FileNotFoundError:
        names = []
    return sum(salaries_list)

def taxes_to_pay_per_month():
    try:
        tax_rate = float(input("Add tax rate here in %"))
        tax_sum = salary_budget()*tax_rate/100
    except Exception as excpt:
        print(excpt)
    return tax_sum



