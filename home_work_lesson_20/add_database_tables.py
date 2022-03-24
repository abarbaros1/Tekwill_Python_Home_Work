from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine , ForeignKey


########################################################################################################################
# CREATE Database and Tables
########################################################################################################################

def create_database_and_tables():
    engine = create_engine('sqlite:///python_lesson_20.db', echo=True)

    # MetaData object will hold database related information
    meta = MetaData(engine)

    # Add table employees
    employees = Table(
        'employees', meta,
        Column('idnp', String(13), primary_key=True),
        Column('first_name', String),
        Column('last_name', String),
        Column('salary', Integer),
        Column('position', String)

    )

        # Add table projects
    projects = Table(
        'projects', meta,
        Column('name', String),
        Column('country', String),
        Column('project_lead', String(13), ForeignKey(employees.c.idnp)),
        Column('project_budget', Integer),
        Column('project_year', Integer)

    )
    meta.create_all()



########################################################################################################################
