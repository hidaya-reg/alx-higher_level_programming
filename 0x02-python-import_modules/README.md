# 0x02. Python - import & modules
## Resources
[Modules](https://docs.python.org/3/tutorial/modules.html)
[Command line arguments](https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments)

## Learning Objectives
<details>
<summary>How to import functions from another file</summary>

### Import Functions from another file
To import functions from another file (module) in Python, you can use the ``import`` statement. 
#### 1. Basic Import
- First, create a Python file (module) containing the functions you want to import.
```python
# my_functions.py

def greet(name):
    return f"Hello, {name}!"
```

- Now, in another Python file (e.g., ``main.py``), you can import and use the ``greet`` function:
```python
# main.py

# Import the greet function from the my_functions module
from my_functions import greet

# Use the function
message = greet("Alice")
print(message)  # Output: Hello, Alice!
```
#### 2. Importing Multiple Functions
```python
# my_functions.py

def greet(name):
    return f"Hello, {name}!"

def farewell(name):
    return f"Goodbye, {name}!"
```
In ``main.py``, you can import both functions like this:
```python
# main.py

from my_functions import greet, farewell

print(greet("Alice"))   # Output: Hello, Alice!
print(farewell("Alice"))  # Output: Goodbye, Alice!
```
#### 3. Importing All Functions
You can import all functions from a module using the asterisk ``*``, though this is generally not recommended as it can lead to name clashes:
```python
# main.py

from my_functions import *

print(greet("Alice"))   # Output: Hello, Alice!
print(farewell("Alice"))  # Output: Goodbye, Alice!
```
#### 4. Importing the Entire Module
You can import the entire module and access its functions using the module name as a prefix:
```python
# main.py

import my_functions

print(my_functions.greet("Alice"))   # Output: Hello, Alice!
print(my_functions.farewell("Alice"))  # Output: Goodbye, Alice!
```
#### 5. Dynamic Import with ``__import__()``
You can also use the ``__import__()`` function if you need to import a module dynamically:
```python
# main.py

module_name = 'my_functions'
my_functions = __import__(module_name)

print(my_functions.greet("Alice"))   # Output: Hello, Alice!
```
</details>
<details>
<summary>How to use the built-in function dir()</summary>

### ``dir()`` Function
The built-in function ``dir()`` in Python is used to obtain a list of attributes and methods of an object. It provides a convenient way to inspect the contents of modules, classes, or any object, helping you understand what you can do with it.

#### How to Use the ``dir()`` Function
**Basic Syntax** `dir([object])`
- *object*: An optional parameter. If provided, ``dir()`` will return the list of attributes and methods of the specified object. If no argument is passed, it returns the list of names in the current local scope.

#### Examples
**1. Using ``dir()`` Without Arguments**
When called without arguments, ``dir()`` will return the names in the current local scope:
```python
a = 10
b = "Hello"
def my_function():
    pass

print(dir())  # Output: A list of names in the current local scope
```
**2. Using ``dir()`` on Built-in Types**
You can use ``dir()`` on built-in types like lists, dictionaries, strings, etc., to see their methods and properties:
```python
my_list = [1, 2, 3]
print(dir(my_list))
```
Output (truncated):
```css
['__add__', '__class__', '__contains__', '__delattr__', '__dir__',  '__doc__', '__eq__', '__ge__', '__getattribute__', '__getitem__',  ... , 'sort', 'reverse']
```
**3. Using ``dir()`` on Custom Classes**
You can also use ``dir()`` to inspect custom classes you’ve created:
```python
class MyClass:
    def method_one(self):
        pass

    def method_two(self):
        pass

# Creating an instance of MyClass
obj = MyClass()

# Using dir() on the instance
print(dir(obj))
```
Output (truncated):
```css
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__',  '__eq__', '__format__', '__ge__', '__getattribute__',  'method_one', 'method_two']
```
**4. Using ``dir()`` on Modules**
You can also use ``dir()`` to inspect the contents of imported modules:
```python
import math

# Get a list of attributes and methods in the math module
print(dir(math))
```
Output (truncated):
```css
['__builtins__', '__doc__', '__name__', 'acos', 'asin', 'atan',  'atan2', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'exp', ...]
```
</details>
<details>
<summary>How to prevent code in your script from being executed when imported</summary>

### To prevent code from being executed when imported
To prevent certain code in your Python script from being executed when the script is imported as a module, you can use the ``if __name__ == "__main__":`` construct. This technique allows you to differentiate between when a script is run directly and when it is imported into another module.

#### How It Works
**1. `__name__` Variable:** In Python, every module has a built-in variable called `__name__`.
- When a module is run directly (e.g., `python my_script.py`), `__name__` is set to `"__main__"`.
- When a module is imported into another module, `__name__` is set to the module's name.
**2. Using the Construct:** By placing the code you want to run only when the module is executed directly within an `if __name__ == "__main__":` block, you ensure that it will not run if the module is imported elsewhere.
**Example**
Here’s a complete example:
**Step 1: Create a Script**
Create a file named `my_script.py` with the following content:
```python
# my_script.py

def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

# Code to run only when this script is executed directly
if __name__ == "__main__":
    print("This script is being run directly.")
    print(greet("Alice"))
```
**Step 2: Import the Script**
Now, create another file named `main.py` to import `my_script.py`:
```python
# main.py

import my_script

print("This is the main script.")
```
- If you run `my_script.py` directly:
```arduino
This script is being run directly.
Hello, Alice!
```
If you run `main.py`:
```
This is the main script.
```
**Use Cases**
- Testing functionality when the script is run directly.
- Keeping your module clean and preventing unwanted side effects when it’s imported.
</details>
<details>
<summary>How to use command line arguments with your Python programs</summary>

### command line arguments in Python programs
Using command line arguments in Python programs allows you to pass information to your script from the command line when you run it. This can be useful for making your programs more flexible and interactive. You can achieve this in two main ways: using the built-in ``sys`` module or the ``argparse`` module, which provides a more powerful and user-friendly interface.

#### Method 1: Using the ``sys`` Module
The ``sys`` module provides access to command line arguments via the ``sys.argv`` list.
- ``sys.argv`` is a list in which the first element is the name of the script, and subsequent elements are the command line arguments passed to the script.
```python
# my_script.py
import sys

# Access command line arguments
script_name = sys.argv[0]  # Name of the script
arguments = sys.argv[1:]    # Command line arguments

print(f"Script name: {script_name}")
print("Arguments:", arguments)
```
Running the Script
```bash
python my_script.py 42 "hello world"
```
Output:
```
Script name: my_script.py
Arguments: ['42', 'hello world']
```
#### Method 2: Using the ``argparse`` Module
The argparse module is a more powerful and flexible way to handle command line arguments, allowing you to specify argument types, help messages, and more.
**Step-by-Step Guide**
- Import the argparse Module: Import ``argparse`` to create an argument parser.
- Create a Parser: Instantiate an ``ArgumentParser`` object.
- Define Arguments: Use the ``add_argument`` method to specify the arguments your script should accept.
- Parse the Arguments: Call ``parse_args()`` to read the command line arguments.
```python
# my_script.py
import argparse

# Create the parser
parser = argparse.ArgumentParser(description="Process some integers.")

# Add arguments
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

# Parse the arguments
args = parser.parse_args()

# Use the arguments
print(f"Arguments: {args.integers}")
print(f"Result: {args.accumulate(args.integers)}")
```
Running the Script
```bash
python my_script.py 1 2 3 4 --sum
```
Output:
```makefile
Arguments: [1, 2, 3, 4]
Result: 10
```
</details>


## Tasks
### 0. Import a simple function from a simple file
Write a program that imports the function def ``add(a, b):`` from the file add_0.py and prints the result of the addition ``1 + 2 = 3``
- You have to use ``print`` function with string format to display integers
- You have to assign:
    + the value ``1`` to a variable called ``a``
    + the value ``2`` to a variable called ``b``
    + and use those two variables as arguments when calling the functions ``add`` and ``print``
- ``a`` and ``b`` must be defined in 2 different lines: ``a = 1`` and another ``b = 2``
- Your program should print: ``<a value> + <b value> = <add(a, b) value>`` followed with a new line
- You can only use the word ``add_0`` once in your code
- You are not allowed to use ``*`` for importing or ``__import__``
- Your code should not be executed when imported - by using ``__import__``, like the example below
```bash
$ cat add_0.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)

$ ./0-add.py
1 + 2 = 3
$ cat 0-import_add.py
__import__("0-add")
$ python3 0-import_add.py 
```
### 1. My first toolbox!
Write a program that imports functions from the file ``calculator_1.py``, does some Maths, and prints the result.
- Do not use the function ``print`` (with string format to display integers) more than 4 times
- You have to define:
    + the value ``10`` to a variable ``a``
    + the value ``5`` to a variable ``b``
    + and use those two variables only, as arguments when calling functions (including ``print``)
- ``a`` and ``b`` must be defined in 2 different lines: ``a = 10`` and another ``b = 5``
- Your program should call each of the imported functions. See example below for format
- the word ``calculator_1`` should be used only once in your file
- You are not allowed to use ``*`` for importing or`` __import__``
- Your code should not be executed when imported
```bash
$ cat calculator_1.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)


def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)


def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)


def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    return int(a / b)

$ ./1-calculation.py
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
```
### 2. How to make a script dynamic!
Write a program that prints the number of and the list of its arguments.
- The output should be:
    + Number of argument(s) followed by ``argument`` (if number is one) or ``arguments`` (otherwise), followed by
    + ``:`` (or ``.`` if no arguments were passed) followed by
    + a new line, followed by (if at least one argument),
    + one line per argument:
        - the position of the argument (starting at ``1``) followed by ``:``, followed by the argument value and a new line
- Your code should not be executed when imported
- The number of elements of ``argv`` can be retrieved by using: ``len(argv)``
- You do not have to fully understand lists yet, but imagine that ``argv`` can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.
```bash
$ ./2-args.py 
0 arguments.
$ ./2-args.py Hello
1 argument:
1: Hello
$ ./2-args.py Hello Welcome To The Best School
6 arguments:
1: Hello
2: Welcome
3: To
4: The
5: Best
6: School
```
### 3. Infinite addition
Write a program that prints the result of the addition of all arguments
- The output should be the result of the addition of all arguments, followed by a new line
- You can cast arguments into integers by using ``int()`` (you can assume that all arguments can be casted into integers)
- Your code should not be executed when imported
```bash
$ ./3-infinite_add.py
0
$ ./3-infinite_add.py 79 10
89
$ ./3-infinite_add.py 79 10 -40 -300 89 
-162
```
Last but not least, your program should also handle big numbers. And the good news is: if your program works for the above example, it will work for the following example:
```bash
$ ./3-infinite_add.py 1111111111111111111111111111111111111111111111111111111111112222222222222222222222222222222222223435467866765443534434222222254444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555666666666666666666666666666666777777777777777777777777777777888888888888888888888888888888899999999999999999999999990000000000000000000 11111111111111111111111111111111111111111111111111222222222222222222222222222333333333333333333334567788888899999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
11111111111111111111111111111111111111111111111111222222222222222222222222222333333333333333333334568900000011111111111111111111111111111111111111111111111111112222222222222222222222222222222222223435467866765443534434222222254444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555666666666666666666666666666666777777777777777777777777777777888888888888888888888888888888899999999999999999999999989999999999999999999
```
Remember how you did (or did not) do it in C? ``#pythoniscool``
### 4. Who are you?
Write a program that prints all the names defined by the compiled module [hidden_4.pyc](https://github.com/alx-tools/0x02.py/raw/master/hidden_4.pyc) (please download it locally).
- You should print one name per line, in alpha order
- You should print only names that do not start with ``__``
- Your code should not be executed when imported
- Make sure you are running your code in Python3.8.x (``hidden_4.pyc`` has been compiled with this version)
```bash
$ curl -Lso "hidden_4.pyc" "https://github.com/alx-tools/0x02.py/raw/master/hidden_4.pyc"
$ ./4-hidden_discovery.py | sort
my_secret_santa
print_hidden
print_school
```
### 5. Everything can be imported
Write a program that imports the variable ``a`` from the file ``variable_load_5.py`` and prints its value.
- You are not allowed to use ``*`` for importing or ``__import__``
- Your code should not be executed when imported
```bash
$ cat variable_load_5.py
#!/usr/bin/python3
a = 98
"""Simple variable
"""

$ ./5-variable_load.py
98
```
### 6. Build my own calculator!
Write a program that imports all functions from the file ``calculator_1.py`` and handles basic operations.
- Usage: ``./100-my_calculator.py a operator b``
    + If the number of arguments is not 3, your program has to:
        - print ``Usage: ./100-my_calculator.py <a> <operator> <b>`` followed with a new line
        - exit with the value ``1``
    + ``operator`` can be:
        - ``+`` for addition
    	- ``-`` for subtraction
        - ``*`` for multiplication
        - ``/`` for division
    + If the operator is not one of the above:
        - print ``Unknown operator. Available operators: +, -, * and /`` followed with a new line
        - exit with the value ``1``
    + You can cast ``a`` and ``b`` into integers by using ``int()`` (you can assume that all arguments will be castable into integers)
    + The result should be printed like this: ``<a> <operator> <b> = <result>``, followed by a new line
- You are not allowed to use ``*`` for importing or ``__import__``
- Your code should not be executed when imported
```bash
$ cat calculator_1.py
#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)


def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)


def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)


def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    return int(a / b)

$ ./100-my_calculator.py ; echo $?
Usage: ./100-my_calculator.py <a> <operator> <b>
1
$ ./100-my_calculator.py 3 + 5 ; echo $?
3 + 5 = 8
0
$ ./100-my_calculator.py 3 H 5 ; echo $?
Unknown operator. Available operators: +, -, * and /
1
```
### 7. Easy print
Write a program that prints ``#pythoniscool``, followed by a new line, in the standard output.
- Your program should be maximum 2 lines long
- You are not allowed to use ``print`` or ``eval`` or ``open`` or ``import sys`` in your file ``101-easy_print.py``
```bash
$ ./101-easy_print.py
#pythoniscool
```
### 8. ByteCode -> Python #3
Write the Python function ``def magic_calculation(a, b):`` that does exactly the same as the following Python bytecode:
```

  3           0 LOAD_CONST               1 (0)
              3 LOAD_CONST               2 (('add', 'sub'))
              6 IMPORT_NAME              0 (magic_calculation_102)
              9 IMPORT_FROM              1 (add)
             12 STORE_FAST               2 (add)
             15 IMPORT_FROM              2 (sub)
             18 STORE_FAST               3 (sub)
             21 POP_TOP

  4          22 LOAD_FAST                0 (a)
             25 LOAD_FAST                1 (b)
             28 COMPARE_OP               0 (<)
             31 POP_JUMP_IF_FALSE       94

  5          34 LOAD_FAST                2 (add)
             37 LOAD_FAST                0 (a)
             40 LOAD_FAST                1 (b)
             43 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             46 STORE_FAST               4 (c)

  6          49 SETUP_LOOP              38 (to 90)
             52 LOAD_GLOBAL              3 (range)
             55 LOAD_CONST               3 (4)
             58 LOAD_CONST               4 (6)
             61 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             64 GET_ITER
        >>   65 FOR_ITER                21 (to 89)
             68 STORE_FAST               5 (i)

  7          71 LOAD_FAST                2 (add)
             74 LOAD_FAST                4 (c)
             77 LOAD_FAST                5 (i)
             80 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             83 STORE_FAST               4 (c)
             86 JUMP_ABSOLUTE           65
        >>   89 POP_BLOCK

  8     >>   90 LOAD_FAST                4 (c)
             93 RETURN_VALUE

 10     >>   94 LOAD_FAST                3 (sub)
             97 LOAD_FAST                0 (a)
            100 LOAD_FAST                1 (b)
            103 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
            106 RETURN_VALUE
            107 LOAD_CONST               0 (None)
            110 RETURN_VALUE
```
Tip: [Python bytecode](https://docs.python.org/3.4/library/dis.html)
### 9. Fast alphabet
Write a program that prints the alphabet in uppercase, followed by a new line.
- Your program should be maximum 3 lines long
- You are not allowed to use:
    + any loops
    + any conditional statements
    + ``str.join()``
    + any string literal
    + any system calls
```bash
$ ./103-fast_alphabet.py
ABCDEFGHIJKLMNOPQRSTUVWXYZ
$ wc -l 103-fast_alphabet.py
3 103-fast_alphabet.py
```