
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
def prime_num():
    my_prime_number = int(input("Add your number here to test if it is prime number"))
    if my_prime_number > 1:
        for element in range(2, my_prime_number):
            if (my_prime_number % element) == 0:
                print(my_prime_number, "not a prime number")
                break
            else:
                print(my_prime_number, "prime number")
                break
    else:
        print(my_prime_number, "not a prime number")



# Ex 3.1
def perfect_number_check():
    perf_num_check = int(input("Add you number to check if its perfect"))
    sum = 0
    for element in range(1, perf_num_check):
        if perf_num_check % element == 0:
            sum += element
    print(sum == perf_num_check)

# Ex 3.2.0
def perf_num_check_arg(perf_num):
    perf_num_check = int(perf_num)
    sum = 0
    for element in range(1, perf_num_check):
        if perf_num_check % element == 0:
            sum += element
    return sum == perf_num_check


# Ex 3.2.1
def perfect_number_list():
    perf_num = int(input("Add amount of numbers to be checked "))
    per_num_count = 0
    perf_num_list = list()
    i_num = 1
    while perf_num > len(perf_num_list):
        if perf_num_check_arg(i_num):
            perf_num_list.append(i_num)
        i_num += 1
    print(f'Your perfect number list is {perf_num_list}')


# Ex 4 partially done
def text_check():
    import string
    my_text = input("Add your text here").lower()
    my_text_new = str()
    punctuation_set = set()
    for element in my_text:
        if element in string.punctuation:
            punctuation_set.add(element)
        else:
            my_text_new += element
    my_text_set = set(my_text_new.split())
    print(f'Punctuation ste {punctuation_set}')
    print(f'Words set {my_text_set}')

if __name__ == '__main__':
    # We can store the functions as values in a dict
    exercises_map = {
        1: palindrome,
        2: prime_num,
        3: perfect_number_check,
        4: perfect_number_list,
        5: text_check
    }
    print('Type the number of the exercise to test:')
    print('1: Palindrome exercise')
    print('2: Prime number exercise')
    print('3: Perfect number check')
    print('4: Perfect number list')
    print('5: Text words and punctuation')
    ex_nr = int(input('Exercise number: '))
    exercises_map[ex_nr]()  # Executing the function at the selected number