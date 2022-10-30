from os import system, name
from D10_CalculatorArt import logo

def add(n1, n2):
    """returns an addition of two numbers"""
    return n1 + n2

def sub(n1, n2):
    """returns an subtraction of two numbers"""
    return n1 - n2

def mul(n1, n2):
    """returns an Multiplication of two numbers"""
    return n1 * n2

def div(n1, n2):
    """returns an Division of two numbers"""
    return n1 / n2

operators = {
    "+": add, 
    "-": sub, 
    "*": mul, 
    "/": div,
}
# dictionary can also be created using dict function as below
# orerators = dict(
#     "+" = add, 
#     "-" = sub, 
#     "*" = mul, 
#     "/" = div,
# )


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operators:
        print(symbol)
        
    should_continue = True

    while should_continue:
        # TODO need to check raise as default value
        # func = operators.get(input("Pick an operation: "), 
        #         exec("raise TypeError('Error, operator should be one from top')"))
        operator_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        # func = operators.get(operator_symbol, "Unknown key")
        # result = func(num1, num2)
        # single line below
        answer = operators.get(operator_symbol, "Unknown key")(num1, num2)
        print(f"{num1} {operator_symbol} {num2} = {answer}")

        cal_flag = input(f"Type 'y' to continue calculating with {answer}, "
                        "or type 'n' to start a new calculation."
                        "any other key stop calculation: ").lower()
        
        if cal_flag == 'y':
            num1 = answer
        elif cal_flag == 'n':
            should_continue = False
            system('cls' if name in ('nt', 'dos') else 'clear')
            calculator()
        else:
            should_continue = False

calculator()