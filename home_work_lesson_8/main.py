# Ex 1
def check_type():
    string_check = input("Add you text here")
    try:
        print(f'{int(string_check)} is integer')
    except ValueError:
        try:
            print(f'{float(string_check)} is float')
        except ValueError:
            try:
                print(f'{string_check} is string')
            except ValueError:
                pass
# Ex 2.0
def new_file():
    name = input("Add here new file name")
    try:
        open(name,'x')
        print(f'File  {name} was successfully created')
    except Exception as excpt:
        print(f' File can not be created due: {excpt}')

# Ex 2.1

def new_file_arg(file_name):
    try:
        open(file_name, 'x')
        print(f'File  {file_name} was successfully created')
    except Exception as excpt:
        print(f' File can not be created due: {excpt}')

# Ex 3
def print_ex2_file():
    file = open('ex_2_file.txt', 'r')
    data = file.read()
    file.close()
    print(f"\n Data from the file:\n  \n  {data} ")

# Ex 4
def new_write_read_file():
    name = input("Add you file name here")
    new_file_arg(name)
    file = open(name, 'a+')
    add_text = input("Add you text to append to file")
    file.write(add_text)

    file.seek(0)
    data = file.read()
    print(data)
    file.close()

# Ex 5

import json

def read_dishes_form_file():
    try:
        file = open('dishes.json', 'r')
        data = file.read()
        dishes = json.loads(data)
    except FileNotFoundError:
        dishes = []
    return dishes


def write_dishes_to_file(dishes: list):
    file = open('dishes.json', 'w')
    json_string = json.dumps(dishes)
    file.write(json_string)
    file.close()


def list_dishes():
    dishes_list = read_dishes_form_file()
    if not dishes_list:
        print('\n No dishes found \n')
    for dish in dishes_list:
        print(dish)


def add_dishes():
    dish = input('Input dish')
    dishes_list = read_dishes_form_file()
    dishes_list.append(dish)
    write_dishes_to_file(dishes_list)


def main():
    while True:
        print('\n ')
        print('Choose option: ')
        print('1. List all dishes. ')
        print('2. Add new dish ')
        print('3. Exit. ')
        option = input('Choose: ')
        if option == '1':
            list_dishes()
        elif option == '2':
            add_dishes()
        elif option == '3':
            exit()
        print('\n')


main()