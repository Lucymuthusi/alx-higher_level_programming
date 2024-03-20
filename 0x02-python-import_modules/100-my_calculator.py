#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1  # Import all functions from calculator_1.py

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        operator = sys.argv[3]
    except ValueError:
        print("All arguments must be integers")
        exit(1)

    operators = {"+": calculator_1.add, "-": calculator_1.sub, "*": calculator_1.mul, "/": calculator_1.div}

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    result = operators[operator](a, b)
    print(f"{a} {operator} {b} = {result}")
