prime_numbers = [2, 3, 5, 7, 6, 11, 13, 17, 19, 23, 29,31]

# a) Extract the middle five primes: Create a new list containing the five primes in the middle of the original list.

number_of_items_to_print = 5
list_length = len(prime_numbers)
remaining_items = list_length - number_of_items_to_print
starting_index = int(remaining_items / 2)
ending_index = starting_index + number_of_items_to_print

new_list = []
for i in prime_numbers[starting_index:ending_index]:
    new_list.append(i)

copy_with_slicing = prime_numbers[starting_index:ending_index].copy()

print(new_list)
print(copy_with_slicing)
# b) Get every second prime: Create a new list containing every second number from the original list, starting from the beginning.

print(prime_numbers[1::2])
second_item_list = sorted(prime_numbers[-2::-2])

print(second_item_list)

# c) Use negative indexing: Create a new list containing the last three primes of the list.

print(prime_numbers[-1:-4:-1].sort())
print(prime_numbers)
last_three = sorted(prime_numbers[-1:-4:-1])
print(last_three)

# d) Reverse the list: Create a new list that contains all the elements of the original list in reverse order.

reverse_list = list(reversed(prime_numbers))
print(reverse_list)

# e) Descending Order: Sort the list in descending order and store it in a new list
prime_numbers.sort(reverse=True)
print(prime_numbers)

