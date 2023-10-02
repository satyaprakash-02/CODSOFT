# Calculator using python

def calculator(operand1, operand2, operator):
    
    operand1 = float(operand1)
    operand2 = float(operand2)
    result = None

    match operator:
        case "+":
            result = (operand1) + (operand2)
        case "-":
            result = (operand1) - (operand2)
        case "*":
            result = (operand1) * (operand2)
        case "/":
            if operand2 == 0:
                print("Division by zero is not allowed")
                return
            result = (operand1) / (operand2)
        case "^":
            if operand1 == 0:
                print("Result:",1.00)
                return
            result = (operand1)**(operand2)
        case _:
            print("Please enter a valid operator!")
            return

    if result is not None:
        print("Result:", result)

operand1 = input("Enter 1st Operand:")
operand2 = input("Enter 2nd Operand:")
operator = input("Enter Operator:")
calculator(operand1, operand2, operator)
