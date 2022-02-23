
#Ex 1
def palindrome():
    my_string = input("Add your text to check it for palindrome")
    count_var = 0
    my_list = list(my_string.replace(' ',''))
    for element in range(len(my_list)):
        if my_list[element] == my_list[((element+1)*(-1))]:
            count_var += 1
    if count_var != len(my_list):
        print("this is not a palindrome")
    else:
        print("This text is palindrome")



#Ex 2
def ex2():
    from Utils.number_utils import prime_num

    my_number = int(input("Add your number here to test if it is prime number"))
    if prime_num(my_number):
        print("prime number")
    else:
        print("not a prime number")





# Ex 3.1
def perfect_number_check():
    from Utils.number_utils import perf_num_check_arg

    perf_num_check = int(input("Add you number to check if its perfect"))
    perf_num_check_arg(perf_num_check)
    print(perf_num_check_arg(perf_num_check))


# Ex 3.2
def perfect_number_list():
    from Utils.number_utils import perf_num_check_arg

    perf_num = int(input("Add amount of perfect numbers you need "))
    while perf_num > 4:
        perf_num = int(input("The time needed for the 5-th perfect number exceeds reason, please enter a valur from 1 to 4: "))
    per_num_count = 0
    perf_num_list = list()
    i_num = 1
    while perf_num > len(perf_num_list):
        if perf_num_check_arg(i_num):
            perf_num_list.append(i_num)
        i_num += 1
    print(f'Your perfect number list is {perf_num_list}')


# Ex 4
def words_check():
    import string
    text_input = input("Add yuor text here").lower()
    text_split = text_input.split()

    text_set = set()
    punctuation_set = set()

    text_dict = dict()
    punctuation_dict = dict()

    for element in text_split:
        if element.isalpha():
            if element in text_dict:
                text_dict[element] += 1
            else:
                text_dict.update({element: 1})
                text_set.add(element)

    for simbol in text_input:
        if simbol in string.punctuation:
            if simbol in punctuation_dict:
                punctuation_dict[simbol] += 1
            else:
                punctuation_dict.update({simbol: 1})
                punctuation_set.add(simbol)

    t_v = list(text_dict.values())
    p_v = list(punctuation_dict.values())

    print(f'Set of words used in text {text_set}')
    print(f'Set of symbols used in text {punctuation_set}')
    print(f'Count of the most commonly used words  {max(t_v)}')
    print(f'Count of the most commonly used punctuation  {max(p_v)}')



if __name__ == '__main__':
    # We can store the functions as values in a dict
    exercises_map = {
        1: palindrome,
        2: ex2,
        3: perfect_number_check,
        4: perfect_number_list,
        5: words_check
    }
    print('Type the number of the exercise to test:')
    print('1: Palindrome exercise')
    print('2: Prime number exercise')
    print('3: Perfect number check')
    print('4: Perfect number list')
    print('5: Text words and punctuation')
    ex_nr = int(input('Exercise number: '))
    exercises_map[ex_nr]()  # Executing the function at the selected number