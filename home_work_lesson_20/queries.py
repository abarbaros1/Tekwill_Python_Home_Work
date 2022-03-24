from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine, func

engine = create_engine('sqlite:///python_lesson_20.db')
meta = MetaData(engine)
meta.reflect()


# employees that earn more than 10000
def earn_more_than_ten_thousand():
    try:
        employees_table = meta.tables.get('employees')

        with engine.connect() as connection:
            select_expression = employees_table.select().where(employees_table.c.salary > 10000)
            print(select_expression)
            result = connection.execute(select_expression)
            for a in result:
                print(a)
            result = connection.execute(select_expression)
            single_result = result.fetchone()
            print(single_result)
    except Exception as exc:
        print(exc)


# project managers that earn more than 13000
def prj_earn_more_than_thirteen_thousand():
    try:
        employees_table = meta.tables.get('employees')

        with engine.connect() as connection:
            select_expression = employees_table.select().where((employees_table.c.salary > 13000)
                                                               & (employees_table.c.position == 'Project manager')
                                                               )
            print(select_expression)
            result = connection.execute(select_expression)
            for a in result:
                print(a)
            result = connection.execute(select_expression)
            single_result = result.fetchone()
            print(single_result)
    except Exception as exc:
        print(exc)


# show the sum of all project budgets by country
def total_projects_budget():
    try:
        projects_table = meta.tables.get('projects')

        with engine.connect() as connection:
            select_expression = projects_table.select().with_only_columns(
                [projects_table.c.country, func.sum(projects_table.c.project_budget).label('total')]).group_by(
                projects_table.c.country)
            print(select_expression)
            result = connection.execute(select_expression)
            for a in result:
                print(a)
            single_result = result.fetchone()
            print(single_result)
    except Exception as exc:
        print(exc)


# Show the most expensive project
def most_expensive_project():
    try:
        projects_table = meta.tables.get('projects')

        with engine.connect() as connection:
            select_expression = projects_table.select().with_only_columns(
                [projects_table.c.name, func.max(projects_table.c.project_budget)])
            print(select_expression)
            result = connection.execute(select_expression)
            single_result = result.fetchall()
            print(single_result)
    except Exception as exc:
        print(exc)


# Show the year with the most budget
def max_budget_year():
    try:
        projects_table = meta.tables.get('projects')

        with engine.connect() as connection:
            select_expression = projects_table.select().with_only_columns(
                [projects_table.c.project_year, func.max(projects_table.c.project_budget)])
            print(select_expression)
            result = connection.execute(select_expression)
            single_result = result.fetchall()
            print(single_result)
    except Exception as exc:
        print(exc)


# employee (name and last name) managed the projects from the projects table.
def project_manager():
    try:
        employees_table = meta.tables.get('employees')
        projects_table = meta.tables.get('projects')

        with engine.connect() as connection:
            join_stmt = employees_table.join(projects_table).select().with_only_columns(
                [employees_table.c.first_name,
                 employees_table.c.last_name,
                 projects_table.c.name
                 ]
            )
            print(connection.execute(join_stmt).fetchall())
    except Exception as exc:
        print(exc)
