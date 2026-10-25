#codeorbit_internship
#task 1- calculator

print("--------------------------")
print("----SIMPLE CALCULATOR----")
print("--------------------------")
try:
    # Taking input from user
    num1=float(input("enter first number:"))
    num2=float(input("enter second number:"))

    #operators menu
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice=input("enter your choice:") # Taking choice from user

    # Performing operations based on user choice
    if choice == '1':
        result = num1+num2
        print("Result:", result)
    elif choice == '2':
        result = num1-num2
        print("Result:", result)
    elif choice == '3':
        result = num1*num2
        print("Result:", result)
    elif choice == '4':
        if num2 != 0:
            result = num1/num2
            print("Result:", result)
        else:
            # Handling division by zero
            print("Error: Division by zero is not allowed.")
    else:
        # Handling invalid choice
        print("Invalid choice. Please select a valid operation.")
except ValueError:
    # Handling invalid input for numbers
    print("Invalid input. Please enter numeric values.")
    