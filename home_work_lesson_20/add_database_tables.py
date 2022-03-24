from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine, ForeignKey

engine = create_engine('sqlite:///python_lesson_20.db', echo=True)
meta = MetaData(engine)


########################################################################################################################
# CREATE Database and Tables
########################################################################################################################

def create_database_and_tables():
    # Add table employees
    try:

        employees = Table(
            'employees', meta,
            Column('idnp', String(13), primary_key=True),
            Column('first_name', String),
            Column('last_name', String),
            Column('salary', Integer),
            Column('position', String)

        )
    except Exception as exc:
        print(exc)

    # Add table projects
    try:
        projects = Table(
            'projects', meta,
            Column('name', String, primary_key=True),
            Column('country', String),
            Column('project_lead', String(13), ForeignKey(employees.c.idnp)),
            Column('project_budget', Integer),
            Column('project_year', Integer)

        )
    except Exception as exc:
        print(exc)

    meta.create_all()
