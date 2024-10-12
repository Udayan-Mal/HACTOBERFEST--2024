def count_even_odd(numbers):
    even_count = 0
    odd_count = 0

    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count

number_dict = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
}

keys = number_dict.keys()


even_count, odd_count = count_even_odd(keys)


print(f"Count of even numbers: {even_count}")
print(f"Count of odd numbers: {odd_count}")
