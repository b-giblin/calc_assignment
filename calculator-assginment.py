'''
Simple Calculator
1. Addition
2. Subtraction
3. Multiplication
4. Division

Enter your choice (1/2/3/4): 3   # anything other than 1,2,3,4 invalid choice
Enter the first number: 5        # float, handle ValueError
Enter the second number: 4       # float, handle ValueError
Result of multiplication: 20
# Handle the ZeroDivisionError
# All other general exception that might arise, print a message saying "An unexpected error occurred: {e}"
'''

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        raise ZeroDivisionError
    return x / y


def main():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1/2/3/4): ")
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        if choice == "1":
            result = add(num1, num2)
            print(f"Result of addition: {result}")
        elif choice == "2":
            result = subtract(num1, num2)
            print(f"Result of subtraction: {result}")
        elif choice == "3":
            result = multiply(num1, num2)
            print(f"Result of multiplication: {result}")
        elif choice == "4":
            result = divide(num1, num2)
            print(f"Result of division: {result}")
        else:
            print("Invalid input")

    except ValueError:
        print("input must be an integer")
    except ZeroDivisionError:
        print("Divide by zero is not allowed")
    except Exception as e:
        print(f"An unexpected error occurred {e}")

if __name__ == "__main__":
    main()

