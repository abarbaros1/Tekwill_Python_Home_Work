from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine
from add_database_tables import create_database_and_tables
from add_test_emp_project import add_test_employee_data, add_test_project_data
from add_new_emp_project import add_new_employee, add_new_project
from salary_change import increase_salary_to_employee, increase_salary_to_position
from queries import *


if __name__ == '__main__':
    exercises_map = {
        1: create_database_and_tables,
        2: add_test_employee_data,
        3: add_test_project_data,
        4: add_new_employee,
        5: add_new_project,
        6: increase_salary_to_employee,
        7: increase_salary_to_position,
        8: earn_more_than_ten_thousand,
        9: prj_earn_more_than_thirteen_thousand,
        10: total_projects_budget,
        11: most_expensive_project,
        12: max_budget_year,
        13: project_manager

    }

    print('Type the number of the exercise to test:')
    print('1: Add new database with employees and projects tables')
    print('2: Upload test data to the employees table')
    print('3: Upload test data to the projects table')
    print('4: Add new employee data')
    print('5: Add new project data')
    print('6: Add salary to a single employee')
    print('7: Add salary to all employees with a given position')
    print('8: Show all employees that earn more than 10 000')
    print('9: Show all project managers that earn more than 13 000')
    print('10: Show the sum of all project budgets by country')
    print('11: Show the most expensive project')
    print('12: Show the year with the most budget')
    print('13: Show which employee (name and last name) managed the projects from the projects table')
    ex_nr = int(input('Exercise number: '))
    exercises_map[ex_nr]()  # Executing the function at the selected number










