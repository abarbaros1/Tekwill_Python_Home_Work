def new_file():
    name = input("Add here new file name")
    try:
        open(name,'x')
        print(f'File  {name} was successfully created')
    except Exception as excpt:
        print(f' File can not be created due: {excpt}')

new_file()