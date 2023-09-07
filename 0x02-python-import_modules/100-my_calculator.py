#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    ac = len(sys.argv) - 1

    if ac != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    dict_ops = {"+":add, "-":sub, "*":mul, "/":div}

    if sys.argv[2] not in list(dict_ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]

    print(f"{a} {op} {b} = {dict_ops[op](a, b)}")
