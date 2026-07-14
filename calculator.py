

def addition():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result =", a + b)

def subtraction():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result =", a - b)

def multiplication():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result =", a * b)

def division():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if b == 0:
        print("Error! Division by zero is not allowed.")
    else:
        print("Result =", a / b)

def modulus():
    a = int(input("Enter first integer: "))
    b = int(input("Enter second integer: "))
    if b == 0:
        print("Error! Modulus by zero is not allowed.")
    else:
        print("Result =", a % b)

def power():
    a = float(input("Enter base: "))
    b = float(input("Enter exponent: "))
    print("Result =", a ** b)

def square():
    a = float(input("Enter a number: "))
    print("Square =", a * a)

def square_root():
    a = float(input("Enter a number: "))
    if a < 0:
        print("Square root of a negative number is not possible.")
    else:
        print("Square Root =", math.sqrt(a))

def factorial():
    n = int(input("Enter a positive integer: "))
    if n < 0:
        print("Factorial of a negative number is not possible.")
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        print("Factorial =", fact)

while True:
    print("\n******** CALCULATOR ********")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Square")
    print("8. Square Root")
    print("9. Factorial")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        addition()
    elif choice == 2:
        subtraction()
    elif choice == 3:
        multiplication()
    elif choice == 4:
        division()
    elif choice == 5:
        modulus()
    elif choice == 6:
        power()
    elif choice == 7:
        square()
    elif choice == 8:
        square_root()
    elif choice == 9:
        factorial()
    elif choice == 10:
        print("Exiting Calculator...")
        break
    else:
        print("Invalid choice! Please try again.")
