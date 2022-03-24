from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine


engine = create_engine('sqlite:///python_lesson_20.db')
meta = MetaData(engine)
meta.reflect()

########################################################################################################################
# Add New Project
########################################################################################################################

def add_new_project():
    new_prj_name = input("Add new project name")
    new_prj_country = input("Add project country")
    new_prj_project_lead = input("Add project lead idnp (13 digits)")
    new_prj_project_budget = int(input("Add project budget"))
    new_prj_project_year = int(input("Add project Year"))

    # engine = create_engine('sqlite:///python_lesson_20.db')
    # meta = MetaData(engine)
    # meta.reflect()
    projects_table = meta.tables.get('projects')

    with engine.connect() as connection:
        insert_statement = projects_table.insert(dict(name=new_prj_name,
                                                      country=new_prj_country,
                                                      project_lead=new_prj_project_lead,
                                                      project_budget=new_prj_project_budget,
                                                      project_year=new_prj_project_year))
        print(insert_statement)
        connection.execute(insert_statement)
        print(connection.execute(projects_table.select()).fetchall())

########################################################################################################################


########################################################################################################################
# Add New Employee
########################################################################################################################

def add_new_employee():
    new_emp_idnp = input("Add new employee idnp (13 digits)")
    new_emp_first_name = input("Add new employee first name")
    new_emp_last_name = input("Add new employee last name")
    new_emp_salary = int(input("Add new employee salary"))
    new_emp_position = input("Add new employee position")

    # engine = create_engine('sqlite:///python_lesson_20.db')
    # meta = MetaData(engine)
    # meta.reflect()
    employees_table = meta.tables.get('employees')

    with engine.connect() as connection:
        insert_statement = employees_table.insert(dict(idnp=new_emp_idnp,
                                                       first_name=new_emp_first_name,
                                                       last_name=new_emp_last_name,
                                                       salary=new_emp_salary,
                                                       position=new_emp_position))
        print(insert_statement)
        connection.execute(insert_statement)
        print(connection.execute(employees_table.select()).fetchall())

########################################################################################################################
