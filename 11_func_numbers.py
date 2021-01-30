numbers = list(range(10))
print(numbers)


def my_filter(list_numbers, other_function):
    result = []
    for number in list_numbers:
        if other_function(number):
            result.append(number)
    return result


def even(number):
    return number % 2 == 0


def not_even(number):
    return number % 2 != 0


print(my_filter(numbers, even))  # передавая функцию, а не вызывая ее () использовать не надо!
print(my_filter(numbers, not_even))

# лямбда функция

print(my_filter(numbers, lambda number: number % 2 != 0))
print(my_filter(numbers, lambda number: number > 5))

