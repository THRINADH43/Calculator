from art import logo


def add(m, t):  # Addition Function
    return m + t


def sub(m, t):  # Subtraction Function
    return m - t


def multi(m, t):  # Multiplication Function
    return m * t


def divide(m, t):  # Division Function
    return m / t


print(logo)

operation = {  # Operation Dictionary
    "+": add,
    "-": sub,
    "*": multi,
    "/": divide
}

number1 = int(input("Enter a number\n"))
for symbol in operation:
    print(symbol)
operation_selection = input("Select the kind of operation you want to perform from the above list\n")
number2 = int(input("Enter Next Number\n"))
selected_operation = operation[operation_selection]
answer = selected_operation(number1, number2)
print(f"{number1}{operation_selection}{number2}={answer}")
continuation = input("type yes if you want to calculate more and no if you want to quit\n")
while continuation == "yes":
    recontinue = input("Do you want to use the previous result type yes or no\n")
    if recontinue == "yes":
        for symbol in operation:
            print(symbol)
        operation_selection = input("Select the kind of operation you want to perform from the above list\n")
        number3 = int(input("Enter Next Number\n"))
        selected_operation = operation[operation_selection]
        result = selected_operation(answer, number3)
        print(f"{answer}{operation_selection}{number3}={result}")
        continuation = input("type yes if you want to calculate more and no if you want to quit\n")
    else:
        number1 = int(input("Enter a number\n"))
        for symbol in operation:
            print(symbol)
        operation_selection = input("Select the kind of operation you want to perform from the above list\n")
        number2 = int(input("Enter Next Number\n"))
        selected_operation = operation[operation_selection]
        answer = selected_operation(number1, number2)
        print(f"{number1}{operation_selection}{number2}={answer}")
        continuation = input("type yes if you want to calculate more and no if you want to quit\n")
while continuation == "no":
    print("Thanks for using :)")
    print("Visit Again")
    break
