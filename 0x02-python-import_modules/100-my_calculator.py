#!/usr/bin/python3
if __name__ == '__main__':

    import sys
    import calculator_1.py

    argument = sys.argv[1:]
    op1 = int(argument[0])
    op2 = int(argument[2])
    operator = argument[1]
    if(len(argument) < 3):
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)

    if(operator not in ['+', '-', '*', '/']):
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)

    if (operator == '+'):
        result = calculator_1.add(op1, op2)
        print(f"{op1} {operator} {op2} = {result}")
    elif (operator == '-'):
        result = calculator_1.sub(op1, op2)
        print(f"{op1} {operator} {op2} = {result}")
    elif (operator == '*'):
        result = calculator_1.mul(op1, op2)
        print(f"{op1} {operator} {op2} = {result}")
    elif (operator == '/'):
        result = calculator_1.div(op1, op2)
        print(f"{op1} {operator} {op2} = {result}")

    sys.exit(0)
