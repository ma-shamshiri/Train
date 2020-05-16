# first_numbers = input("Please enter your first list: ")
# second_numbers = input("Please enter your second list: ")


""" Create two lists of numbers """
first_numbers = list(range(20))
second_numbers = list(range(10, 17))


def array_diff(first_list, second_list):
    """ Return first list without items of second list """
    return [int(item) for item in first_list if item not in second_list]


""" Call function and pass two lists """
print(array_diff(first_numbers, second_numbers))
