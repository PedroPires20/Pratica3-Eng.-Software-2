from mathlib.fraction import Fraction

if __name__ == "__main__":
    print("Fraction calculator:")
    print("Usage: [fraction 1] operation [fraction 2]")
    print("The supported arithmetic operations are: addition (+), subtraction (-), multiplication (*), division (/)")
    print("The following comparison operations are also supported: equality (=), inequality (!=), greater than (>), less than (<), greater of equal (>=), lesser or equal (<=)")
    while True:
        input_line = input("Enter an operation: ")
        if input_line == "exit":
            break
        tokens = input_line.split(' ')
        if len(tokens) != 3:
            print(f"The given input \"{input_line}\" is invalid!")
            continue
        f1 = Fraction.from_string(tokens[0])
        op = tokens[1]
        f2 = Fraction.from_string(tokens[2])
        if op == "+":
            result = f1 + f2
        elif op == "-":
            result = f1 - f2
        elif op == "*":
            result = f1 * f2
        elif op == "/":
            result = f1 / f2
        elif op == "=":
            result = f1 == f2
        elif op == "!=":
            result = f1 != f2
        elif op == ">":
            result = f1 > f2
        elif op == "<":
            result = f1 < f2
        elif op == ">=":
            result = f1 >= f2
        elif op == "<=":
            result = f1 <= f2
        else:
            print("Invalid operation specified!")
            continue
        print(f"The result is: {result}")
