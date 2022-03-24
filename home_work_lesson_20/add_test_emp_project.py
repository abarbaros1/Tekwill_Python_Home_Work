from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine
########################################################################################################################
# Load Test data to employees table
########################################################################################################################
def add_test_employee_data():
    engine = create_engine('sqlite:///python_lesson_20.db')
    meta = MetaData(engine)
    meta.reflect()
    employees_table = meta.tables.get('employees')

    with engine.connect() as connection:
        insert_statement = employees_table.insert([
            # dict(idnp=new_emp_idnp, first_name=new_emp_first_name, last_name = new_emp_last_name, salary=new_emp_salary, position=new_emp_position),
            dict(idnp='2102031023011', first_name='John', last_name='Smith', salary=10500, position='Office manager'),
            dict(idnp='2102031012042', first_name='Kenau', last_name='Reeves', salary=9400, position='Office manager'),
            dict(idnp='2102031011522', first_name='Kathy', last_name='Diaz', salary=15000, position='Administrator'),
            dict(idnp='2102031681298', first_name='Juan', last_name='Rogers', salary=20000, position='Director'),
            dict(idnp='2102031138438', first_name='Ruth', last_name='Stewart', salary=12000,
                 position='Project manager'),
            dict(idnp='2102031384568', first_name='Raymond', last_name='Johnson', salary=13000,
                 position='Project manager'),
            dict(idnp='2102031684583', first_name='Rebecca', last_name='Bell', salary=8000, position='Data Analyst'),
            dict(idnp='2102036844852', first_name='Phyllis', last_name='Torres', salary=9500,
                 position='Sale representative'),
            dict(idnp='2102031689912', first_name='Frank', last_name='Harris', salary=6700, position='Worker'),
            dict(idnp='2102031588321', first_name='Linda', last_name='Taylor', salary=12000,
                 position='Sale representative'),
            dict(idnp='2102031549818', first_name='Jesse', last_name='Wood', salary=9000, position='Worker'),
            dict(idnp='2102031489458', first_name='Clarence', last_name='Martin', salary=9000, position='Data Analyst'),
            dict(idnp='2102031693428', first_name='Sandra', last_name='Bryant', salary=8000, position='Worker'),
            dict(idnp='2102188435892', first_name='Margaret', last_name='Young', salary=7000,
                 position='Sale representative'),
            dict(idnp='2102034588321', first_name='Scott', last_name='Mitchell', salary=15000,
                 position='Project manager'),
            dict(idnp='2102058123481', first_name='Heather', last_name='King', salary=12000, position='Worker'),
            dict(idnp='2102095492312', first_name='Kimberly', last_name='Turner', salary=18000,
                 position='Project manager'),
            dict(idnp='2102065493281', first_name='Walter', last_name='Perez', salary=16000, position='Worker'),
            dict(idnp='2102065488233', first_name='John', last_name='Bailey', salary=6000, position='Project manager'),
            dict(idnp='2102031235818', first_name='Judith', last_name='Robinson', salary=5000, position='Worker'),
            dict(idnp='2102036549932', first_name='Harold', last_name='Anderson', salary=8900,
                 position='Project manager'),
            dict(idnp='2102067983821', first_name='Douglas', last_name='Scott', salary=6000, position='Worker'),
            dict(idnp='2102036589891', first_name='Larry', last_name='Jackson', salary=12000, position='Worker'),
            dict(idnp='2102036981212', first_name='Paul', last_name='Walker', salary=10000,
                 position='Sale representative'),
            dict(idnp='2102031298148', first_name='Keith', last_name='Lopez', salary=15000, position='Data Analyst'),
            dict(idnp='2102084856231', first_name='Thomas', last_name='Butler', salary=17000, position='Worker'),
            dict(idnp='2102036594893', first_name='Kathleen', last_name='Clark', salary=16000, position='Data Analyst')
        ]
        )
        print(insert_statement)
        connection.execute(insert_statement)
        print(connection.execute(employees_table.select()).fetchall())


########################################################################################################################


########################################################################################################################
# Load Test data to projects table
########################################################################################################################

def add_test_project_data():
    engine = create_engine('sqlite:///python_lesson_20.db')
    meta = MetaData(engine)
    meta.reflect()
    projects_table = meta.tables.get('projects')

    with engine.connect() as connection:
        insert_statement = projects_table.insert([
            # dict(name=new_prj_name, country=new_prj_country, project_lead=new_prj_project_lead, project_budget=new_prj_project_budget, project_year=new_prj_project_year)
            dict(name='Canary', country='Switzerland', project_lead='2102036549932', project_budget=120000,
                 project_year=2021),
            dict(name='Hornets', country='England', project_lead='2102031138438', project_budget=240000,
                 project_year=2021),
            dict(name='Mercury', country='Germany', project_lead='2102036549932', project_budget=820000,
                 project_year=2021),
            dict(name='Limitless Horizons', country='Ukraine', project_lead='2102036549932', project_budget=200000,
                 project_year=2021),
            dict(name='Moving Bird', country='Moldova', project_lead='2102031384568', project_budget=100000,
                 project_year=2021),
            dict(name='Project Breeze', country='Iceland', project_lead='2102034588321', project_budget=15000000,
                 project_year=2021),
            dict(name='Command Program', country='Moldova', project_lead='2102095492312', project_budget=500000,
                 project_year=2022),
            dict(name='Project Point', country='Germany', project_lead='2102065488233', project_budget=6500000,
                 project_year=2012),
            dict(name='Project Mecha', country='France', project_lead='2102031384568', project_budget=1000000,
                 project_year=2014),
            dict(name='Program Pad', country='England', project_lead='2102065488233', project_budget=250000,
                 project_year=2015),
            dict(name='Project Synergy', country='Germany', project_lead='2102031384568', project_budget=500000,
                 project_year=2018),
            dict(name='Dynamic Program', country='Moldova', project_lead='2102031384568', project_budget=6800000,
                 project_year=2019),
            dict(name='Project Zen', country='France', project_lead='2102031384568', project_budget=9000000,
                 project_year=2017)

        ]
        )
        print(insert_statement)
        connection.execute(insert_statement)
        print(connection.execute(projects_table.select()).fetchall())


########################################################################################################################
