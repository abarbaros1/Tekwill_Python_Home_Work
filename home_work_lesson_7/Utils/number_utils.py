def prime_num(number):
    for element in range(2, (number // 2) + 1):
        if number % 2 == 0:
            return False
    return True


def perf_num_check_arg(perf_num):
    perf_num_check = int(perf_num)
    sum = 0
    for element in range(1, perf_num_check):
        if perf_num_check % element == 0:
            sum += element
    return sum == perf_num_check
