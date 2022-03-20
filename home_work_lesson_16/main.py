import requests
import csv


# language_list = ['ro','ru','en']

def get_all_languages():
    string = input("Add the list of language codes separated by a space").lower()
    string.split()
    language_list = string.split()
    #print(language_list)
    return language_list

#print(get_all_languages())


def core_translate(text_to_translate, to_language):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    headers = {
        'x-rapidapi-key': "REMOVED"
    }
    data = dict(
        q=text_to_translate,
        target=to_language
    )
    response = requests.post(url, data=data, headers=headers)
    # print(response.text)
    return response


def translate(text_to_translate, to_language):
    if to_language in get_all_languages():
        response = core_translate(text_to_translate, to_language)
        return response.text


def translate_file(path, to_language):
    with open(path, 'r') as f:
        reader = f.read()
        output_dict = translate(reader, to_language)
        print(output_dict)
        #return output_dict

translate_file('C:\\Users\\PC\\PycharmProjects\\Tekwill_Python_Home_Work\\home_work_lesson_16\\plain_text.csv', 'ro')
