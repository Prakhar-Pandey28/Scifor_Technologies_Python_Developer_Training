def unique_fibonacci_generator():
    first_num, second_num = 0, 1
    while True:
        yield first_num
        first_num, second_num = second_num, first_num + second_num

fibonacci_gen = unique_fibonacci_generator()

for i in range(10):
    print(next(fibonacci_gen))
