#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    ac = len(sys.argv) - 1

    if ac != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    dict_ops = {"+":add, "-":sub, "*":mul, "/":div}

    op = sys.argv[2]
    if op not in list(dict_ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    result = dict_ops[op](a, b)

    print("{} {} {} = {}".format(a, op, b, result))
