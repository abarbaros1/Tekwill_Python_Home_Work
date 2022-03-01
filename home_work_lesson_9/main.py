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

def open_read_load(file_name,mode):
    try:
        file = open(file_name, mode)
        data = file.read()
        data_list = json.loads(data)
    except FileNotFoundError:
        data_list =[]
    return data_list

def list_names():
    try:
        new_list = open_read_load('employee_list.json', 'r')
        names_list = [el['name'] for el in new_list ]
    except FileNotFoundError:
        names = []
    return names_list


def list_positions():
    try:
        position_names = open_read_load('employee_list.json', 'r')
        position_names_list = [el['position'] for el in position_names]
    except FileNotFoundError:
        names = []
    return position_names_list


def salary_budget():
    try:
        employee_list = open_read_load('employee_list.json', 'r')
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



