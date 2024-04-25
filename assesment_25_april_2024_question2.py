numbers = [1, 2, 3, 4, 5]
sq_numbers = [num ** 2 for num in numbers]
print("squared numbers:", sq_numbers)

def square(x):
    return x ** 2

mapped_numbers = list(map(square, numbers))
print("squared mapped numbers:", mapped_numbers)

def is_even(x):
    return x % 2 == 0

filtered_numbers = list(filter(is_even, numbers))
print("filtered numbers:", filtered_numbers)

def add_n_to_x(n):
    def adder(x):
        return x + n
    return adder

add_five = add_n_to_x(5)
print("added five to x:", add_five(10))