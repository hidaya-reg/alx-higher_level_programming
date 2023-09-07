#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    ac = len(sys.argv) - 1
    if ac == 0:
        print("0 arguments.")
    elif ac == 1:
        print(f"{ac} argument:")
    else:
        print(f"{ac} arguments:")
    for i in range(ac):
        print(f"{i + 1}: {sys.argv[i + 1]}")
