#ex.1
# elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# squared = list(map(lambda el: el ** 2, elements))
# print(squared)
# cube = list(map(lambda el: el ** 3, elements))
# print(cube)

#ex.2

# elements = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
#
# palindromes = filter(lambda el: el == el[::-1], elements)
# print(list(palindromes))

#ex3
# def validate_numeric(func):
#     def wrapped(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if not isinstance(result, (int, float, complex)):
#             raise ValueError("Result type is not numeric")
#         return result
#
#     return wrapped
#
#
# @validate_numeric
# def return_number():
#     return 10
#
#
# @validate_numeric
# def return_str():
#     return '123'
#
#
# print(return_number())
# # 10
# print(return_str())
# # ValueError: Result type is not numeric

#ex.4
# def my_user_input_generator(stop_at):
#     while True:
#         user_input = input("Please enter something: ")
#         if user_input == stop_at:
#             break
#         yield user_input
#
#
# for user_input in my_user_input_generator('STOP'):
#     print(user_input)
