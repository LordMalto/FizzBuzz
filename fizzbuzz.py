num = int(input("Enter a Number: \n"))

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 5 == 0:
    print("Buzz")
elif num % 3 == 0:
    print("Fizz")
else:
    print("Number is not divideable by 3 or 5!")
