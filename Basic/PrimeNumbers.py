def check_prime_numbers(list_of_numbers):
    for number in list_of_numbers:
        number = int(number)
        not_prime = False
        for divisible in range (2,number):
            if number % divisible == 0:
                not_prime = True
        if not not_prime:
            print(number)

string_list_of_numbers = input("Enter numbers : ")
list_of_numbers = string_list_of_numbers.split(",")
check_prime_numbers(list_of_numbers)