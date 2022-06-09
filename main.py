import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(art.logo)

    num1 = float(input("What's the first number?\n"))
    for symbol in operations:
        print(symbol)
    cont = True

    while cont:
        operation = input("Which operator would you like to use?\n")
        num2 = float(input("What's the next number?\n"))
        calculation_function = operations[operation]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation} {num2} = {answer}\n")

        if input(f"Pleas press Y to continue calculations with {answer}. Or press N to start a new calculation.\n").lower() == "y":
            num1 = answer
        else:
            cont = False
            calculator()


calculator()
