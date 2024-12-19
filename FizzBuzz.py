# FizzBuzz Program
for number in range(1, 101):  # Loop through numbers 1 to 100
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")  # Multiple of both 3 and 5
    elif number % 3 == 0:
        print("Fizz")  # Multiple of 3
    elif number % 5 == 0:
        print("Buzz")  # Multiple of 5
    else:
        print(number)  # Not a multiple of 3 or 5
