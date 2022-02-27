def print_ex2_file():
    file = open('ex_2_file.txt', 'r')
    data = file.read()
    file.close()
    print(f"\n Data from the file:\n  \n  {data} ")

print_ex2_file()
