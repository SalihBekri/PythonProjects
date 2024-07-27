from art import logo
def add(n1, n2):
    return n1 + n2
def substract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}



def calculate():
    print(logo)
    n1 = float(input("What's the first number?: "))
    for i in operations:
        print(i)
    # restart = False
    while True:
    
  
        operation = input("Pick an operation: ")
        n2 = float(input("What's the next number?: "))
        decimal = int(input("How many decimal places would you like your number to be?: "))
        result = round(operations[operation](n1, n2), decimal)
        print(f"{n1} {operation} {n2} = {result}")
        ans = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit.: ")
        if ans == "n":
            calculate()
        else:
            n1 = result
calculate()

  

