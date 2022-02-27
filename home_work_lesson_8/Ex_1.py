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

check_type()

