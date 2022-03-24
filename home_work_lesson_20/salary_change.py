from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine


########################################################################################################################
# Increase Salary to single Employee
########################################################################################################################
def increase_salary_to_employee():
    add_first_name = input("Add employee first name").capitalize()
    add_last_name = input("Add employee last name").capitalize()
    add_salary = int(input("Add to salary"))

    engine = create_engine('sqlite:///python_lesson_20.db')
    meta = MetaData(engine)
    meta.reflect()
    employees_table = meta.tables.get('employees')

    with engine.connect() as connection:
        update_statement = employees_table.update().where(
            (employees_table.c.first_name == add_first_name) & (employees_table.c.last_name == add_last_name)).values(
            salary=employees_table.c.salary + add_salary)
        connection.execute(update_statement)
        print(connection.execute(employees_table.select()).fetchall())

########################################################################################################################


########################################################################################################################
# Increase Salary to the list of  Employees
########################################################################################################################
def increase_salary_to_position():
    set_position = input("Add employees position for salary increase").capitalize()
    add_salary = float(input("Add to salary"))

    engine = create_engine('sqlite:///python_lesson_20.db')
    meta = MetaData(engine)
    meta.reflect()
    employees_table = meta.tables.get('employees')

    with engine.connect() as connection:
        update_statement = employees_table.update().where(
            employees_table.c.position == set_position).values(
            salary=employees_table.c.salary + add_salary)
        connection.execute(update_statement)
        print(connection.execute(employees_table.select()).fetchall())

########################################################################################################################
