import pandas as pd
import openpyxl

students_data_frame = pd.read_excel('homework.xlsx', sheet_name='Exam Results')

def default_dataframe():
    print(students_data_frame)

def wo_score():
    student_without_score = students_data_frame[(students_data_frame['score'].isna())]
    #students_data_frame.dropna(subset=['score'])
    print(student_without_score)
    #return student_without_score

def score_between():
    min_score = float(input("Add min score"))
    max_score = float(input("Add max score"))
    student_score_between = students_data_frame[students_data_frame['score'].between(min_score, max_score)]
    print(student_score_between)
    #return student_score_between

def sort_name():
    sorted_name_data_frame = students_data_frame.sort_values(by='name')
    print(sorted_name_data_frame)
    #return sorted_name_data_frame

def sort_score():
    sorted_score_data_frame = students_data_frame.sort_values(by='score')
    print(sorted_score_data_frame)
    #return sorted_score_data_frame

def add_new_record():
    name = input("Add name")
    score = float(input("Add score"))
    attempts = int(input("Add attempts num"))
    qualify = None
    while qualify not in ['yes','no']:
        qualify_input = input("Add qualify yes or no")
        qualify = qualify_input.lower()
    dict = {'name': name, 'score': score, 'attempts': attempts, 'qualify': qualify}
    #new_students_data_frame = students_data_frame.append(dict, ignore_index=True)
    dict_data_frame = pd.DataFrame.from_dict([dict], orient='columns')
    new_students_data_frame = pd.concat([students_data_frame, dict_data_frame], ignore_index=True)
    print(new_students_data_frame)
    #return new_students_data_frame

def remove_by_index():
    df_index = int(input('Add index id to remove the row'))
    new_data_frame = students_data_frame.drop(df_index)
    print(new_data_frame)
    #return new_data_frame


def save_to_excel_qualified():
    qualified_df = students_data_frame[students_data_frame['qualify'] == 'yes'][['name','score']]
    qualified_df.to_excel('qualified_students.xlsx', sheet_name='qualified')
    print('data frame was saved successfully to qualified_students.xlsx')
    #return qualified_df



if __name__ == '__main__':
    exercises_map = {
        0: default_dataframe,
        1: wo_score,
        2: score_between,
        3: sort_score,
        4: sort_name,
        5: add_new_record,
        6: remove_by_index,
        7: save_to_excel_qualified
    }

    print('Type the number of the exercise to test:')
    print('0: print students initial data frame')
    print('1: Rows where the score is missing, i.e. is NaN')
    print('2: Rows the score is between a and b, where a and b are values input from console')
    print('3: Rows sorted by score')
    print('4: Rows sorted by name')
    print('5: Add new element (result) to the dataframe (values input from console)')
    print('6: Remove results from the dataframe (by index)')
    print('7: Save a list of all students that qualified, in a separate Excel file called qualified_students.xlsx. '
          '\n Only columns name and score should be visible there')
    ex_nr = int(input('Exercise number: '))
    exercises_map[ex_nr]()  # Executing the function at the selected number
