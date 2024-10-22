# 0x07. Python - Test-driven development
## Resources
- [doctest — Test interactive Python examples](https://docs.python.org/3.4/library/doctest.html) (until “26.2.3.7. Warnings” included)
- [doctest – Testing through documentation](https://pymotw.com/3/doctest/)
- [Unit Tests in Python](https://www.youtube.com/watch?v=1Lfv5tUGsn8&ab_channel=Socratica)
- [Unittest module](https://www.youtube.com/watch?v=6tNS--WetLI&ab_channel=CoreySchafer)
- [Interactive and Non-interactive tests](https://mattermost.com/blog/testing-python-understanding-doctest-and-unittest/)

## Learning Objectives
<details>
<summary>What’s an interactive test</summary>

### Interactive test
Interactive testing can occur when a developer manually runs code in the Python shell or terminal to interact with the program directly, similar to how doctests are demonstrated by running commands in a Python shell to see immediate outputs.

**Example of Interactive Testing:**
1. Run the Program: Open a Python shell.
2. Provide Input: Manually input data into the shell, for instance, creating a Customer object and calling its methods.
3. Observe Output: Check the program's response and verify if it's correct based on the inputs you gave.

```python
>>> from customer import Customer
>>> customer_1 = Customer("John", "Brad", 5000)
>>> customer_1.customer_mail()
'John.Brad@email.com'
>>> customer_1.apply_discount()
4750
```
In this test, you're manually interacting with the Customer class, verifying its behavior based on the commands you provide.

Interactive tests are often used in development stages for quickly verifying how a program behaves with different inputs but are less practical for repeated large-scale testing, where automation (e.g., ``unittest``, ``doctest``) would be more efficient.
</details>
<details>
<summary>How to write Docstrings to create tests</summary>

### Docstrings
To write docstrings that can be used for testing with Python’s ``doctest`` module, you include examples of how your functions or methods are expected to behave directly within the docstring. These examples are written in the format of an interactive Python session (as if you're typing in the Python interpreter). Then, ``doctest`` can run those examples as tests.

#### 1. Basic Structure of a Doctest in a Docstring
```python
def function_name(parameters):
    """
    Short description of the function.

    Example:
    >>> function_name(arg1, arg2)
    expected_output
    """
    pass  # The actual implementation of your function
```
#### 2. Steps to Write Docstrings with Doctests
**- Describe the function:** Begin with a brief description of what the function does.
**- Provide examples:** Inside the docstring, show how to call the function and what its output should be, prefixed with ``>>>`` as if typing at the Python prompt. Ensure the example is complete and shows the expected behavior.
**- Expected output:** Follow the call to the function with the expected output.
#### 3. Example of Writing Docstrings for Doctests
Consider this simple function that adds two numbers:
```python
def add(a, b):
    """
    Adds two numbers and returns the result.

    Example:
    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    >>> add(0, 0)
    0
    """
    return a + b
```
#### 4. How to Run Doctests
Once you’ve written the doctests inside the docstrings, you can run them using the doctest module.

**4.1. Import the ``doctest`` module** at the bottom of the file and call ``doctest.testmod()``:
```python
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```
Run the script in the terminal using:
```bash
python script_name.py -v
```
The ``-v`` flag gives a verbose output, showing which tests passed or failed.

#### 5. Example with a Class
If you have a class, you can include doctests in the class’s methods. For instance:
```python
class Calculator:
    """
    A simple calculator class.

    Example:
    >>> calc = Calculator()
    >>> calc.add(5, 3)
    8
    >>> calc.subtract(10, 4)
    6
    """
    
    def add(self, a, b):
        """
        Adds two numbers.

        Example:
        >>> Calculator().add(2, 3)
        5
        """
        return a + b

    def subtract(self, a, b):
        """
        Subtracts b from a.

        Example:
        >>> Calculator().subtract(10, 4)
        6
        """
        return a - b
```
#### 6. Handling Edge Cases
Doctests can also cover edge cases or exceptions:
```python
def divide(a, b):
    """
    Divides a by b.

    Example:
    >>> divide(10, 2)
    5.0
    >>> divide(10, 0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero
    """
    return a / b
```
In the ``ZeroDivisionError`` example, the ``Traceback`` and error message are shown as part of the expected output.

</details>
<details>
<summary>Creating a Doctest in an External File</summary>

### Doctest in an External File
#### 1. Creating a Doctest in an External File
You can write the doctests in a plain text file with examples in the same format as you would use in a docstring.
For example, create a file named ``tests.txt``:
```python
>>> from your_module import add
>>> add(2, 3)
5
>>> add(0, 0)
0
>>> add(-1, 1)
0
```
#### 2. Running the External Doctest
Once the file ``tests.txt`` is ready, you can load it and run the doctests using Python’s ``doctest`` module.
```python
import doctest

if __name__ == "__main__":
    doctest.testfile("tests.txt", verbose=True)
```
#### 3. Example of External File Doctest
Let’s say you have a Python module named ``my_module.py`` with a simple function like this:
```python
# my_module.py

def add(a, b):
    return a + b
```
Then, create a separate tests.txt file for the doctests:
```text
>>> from my_module import add
>>> add(1, 2)
3
>>> add(-1, 1)
0
>>> add(0, 0)
0
```
Now, to run the tests in ``tests.txt``, add the following to ``my_module.py`` or to a separate script that imports the module:
```python
import doctest

if __name__ == "__main__":
    doctest.testfile("tests.txt", verbose=True)
```
#### 4. Running the Tests
To run the external doctests, simply run the script in the terminal:
```bash
python my_module.py
```
#### 5. Customizing doctest.testfile
You can pass additional parameters to ``doctest.testfile`` for customization:
- ``verbose=True``: Provides detailed output of test results.
- ``module_relative=True``: By default, the path to the text file is relative to the calling module. Set this to ``False`` if you want to specify an absolute path.
- ``encoding='utf-8'``: If your file contains non-ASCII characters, you can specify an encoding.
```python
doctest.testfile("tests.txt", verbose=True, module_relative=True, encoding="utf-8")
```
#### 6. Benefits of External Doctests
**- Separation of concerns:** Keeps your code and test examples separate, which can make both more maintainable.
**- Easier to manage large test suites:** You can have multiple external test files if needed.
**- Reusability: **External files can be used to test multiple modules or across different test environments.
This method offers flexibility for large projects or for cases where docstrings may not be the best place to store tests.
</details>
<details>
<summary>What is unittest?</summary>

### ``unittest``
``unittest`` is a built-in Python module used for writing and running tests. It is based on the xUnit framework design, which is common for unit testing frameworks. The purpose of ``unittest`` is to allow developers to test small units of code (functions, methods, classes) to ensure they work as expected.

#### Key Concepts of unittest
**- TestCase:** The smallest unit of testing. A ``TestCase`` class contains individual methods that represent tests.
**-Test Suite:** A collection of test cases.
**- Test Runner:** A component that runs the test suite and outputs the results.
**- Assertions:** Methods used to check if the output of your code is what you expect. Common assertions include ``assertEqual``, ``assertTrue``, ``assertRaises``, etc.

#### How to Use ``unittest`` in Python
#### 1. Creating a Test Case
To create a test, you define a class that inherits from ``unittest.TestCase`` and write methods within it. Each method represents a test and must start with the prefix ``test_`` so that the ``unittest`` module knows it's a test method.
```python
import unittest

# Code to be tested
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Test class inheriting from unittest.TestCase
class TestMathOperations(unittest.TestCase):
    # Test case for the add function
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    # Test case for the subtract function
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)

# Run the tests
if __name__ == '__main__':
    unittest.main()
```
#### 2. Running Tests
- You can run tests by calling ``unittest.main()`` at the bottom of your script.
- If you save the above code to a file called ``test_math.py``, you can run the tests from the command line:
```bash
python -m unittest test_math.py
```
#### Key Features of unittest
##### 1. Assertions
``unittest`` provides a variety of assertion methods to check conditions. Here are some common ones:

- ``assertEqual(a, b)``: Test that ``a == b``.
- ``assertNotEqual(a, b)``: Test that ``a != b``.
- ``assertTrue(x)``: Test that ``x`` is ``True``.
- ``assertFalse(x)``: Test that ``x`` is ``False``.
- ``assertRaises(exc, func, *args, **kwds)``: Test that ``func`` raises exception ``exc``.
```python
class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('hello'.upper(), 'HELLO')

    def test_isupper(self):
        self.assertTrue('HELLO'.isupper())
        self.assertFalse('Hello'.isupper())
```
##### 2. SetUp and TearDown
``setUp`` and ``tearDown`` are methods that are executed before and after each test method, respectively. These are used to set up test environments and clean up after tests.
```python
class TestWithSetup(unittest.TestCase):
    def setUp(self):
        # Code to set up resources or data
        self.value = 42

    def tearDown(self):
        # Code to clean up resources after each test
        del self.value

    def test_value(self):
        self.assertEqual(self.value, 42)
```
##### 3. Running a Test Suite
You can create a test suite that contains multiple test cases and run them together.
```python
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestMathOperations('test_add'))
    suite.addTest(TestMathOperations('test_subtract'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
```
##### 4. Skipping Tests
You can skip tests using @unittest.skip() or related decorators.
```python
class TestSkipped(unittest.TestCase):
    @unittest.skip("Skipping this test for now")
    def test_skipped(self):
        self.assertEqual(1, 1)
```
##### 5. Grouping Tests
You can use the ``TestLoader`` class to discover and group tests, making it easy to run them.
```python
if __name__ == "__main__":
    loader = unittest.TestLoader()
    tests = loader.discover('.')
    runner = unittest.TextTestRunner()
    runner.run(tests)
```

#### Example Workflow for Using ``unittest``
**1. Write the Code:** Write your actual code that performs tasks.
```python
def multiply(a, b):
    return a * b
```
**2. Write Tests:** Create a separate file with test cases.
```python
import unittest
from math_operations import multiply

class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)

if __name__ == "__main__":
    unittest.main()
```
**3. Run Tests:**
```bash
python -m unittest test_math_operations.py
```
</details>
<details>
<summary>What are the basic option flags to create tests</summary>

### Basic option flags to create tests


| **Flag**      | **Description**                                                                 | **Example Command**                                    |
|---------------|---------------------------------------------------------------------------------|--------------------------------------------------------|
| `-v`          | Run tests with detailed output (verbose).                                        | `python -m unittest -v`                                |
| `-q`          | Run tests with minimal output (quiet).                                           | `python -m unittest -q`                                |
| `-f`          | Stop on the first failure (failfast).                                            | `python -m unittest -f`                                |
| `-c`          | Handle `KeyboardInterrupt` and show results so far (catch).                      | `python -m unittest -c`                                |
| `-b`          | Buffer `stdout` and `stderr` during test execution to suppress output.           | `python -m unittest -b`                                |
| `--locals`    | Show local variables in tracebacks on failure.                                   | `python -m unittest --locals`                          |
| `discover`    | Automatically discover and run all test files (default pattern: `test*.py`).     | `python -m unittest discover`                          |


</details>
<details>
<summary>How to find edge cases</summary>

### Edge cases
Finding edge cases in software testing involves identifying inputs, situations, or interactions that are at the "boundary" of what your software can handle. These are often where bugs or unexpected behavior occur.

| **Edge Case Type**           | **Description**                                                | **Simple Example**                                             |
|------------------------------|----------------------------------------------------------------|---------------------------------------------------------------|
| **Minimum/Maximum Values**    | Test the smallest and largest values allowed.                  | A function accepts numbers from 1 to 100. Test with `1` and `100`. |
| **Empty Values**              | Check how the code handles empty inputs.                       | A string function: Test with `""` (empty string).              |
| **Null or None Values**       | Test with `None` or null-like values to see how they are handled. | A list function: Test with `None` instead of a valid list.     |
| **Invalid Values**            | Provide values outside the valid range.                        | A function expects positive numbers: Test with `-1` or `-100`. |
| **Special Characters**        | Input non-alphabetic characters or unusual input.              | A username validation function: Test with `@`, `#`, or `&`.    |
| **Boundary Values**           | Test values at and just beyond the boundary of valid input.     | A function accepts numbers from 1 to 100. Test with `0`, `1`, `100`, and `101`. |
| **Empty Collections**         | Check how functions handle empty data structures.              | Sorting a list: Test with an empty list `[]`.                  |
| **Large Inputs**              | Test with inputs much larger than usual.                       | A list-processing function: Test with a list of 100,000 items. |
| **Single Element Collection** | Test how functions behave with a collection containing only one item. | Sorting a list: Test with a list `[5]`.                        |
| **Data Type Mismatch**        | Test with different data types than expected.                  | A function expects integers: Test with `"text"` or `2.5`.      |
| **Concurrency Issues**        | Test with simultaneous access or processes.                    | Two users updating the same record at the same time.           |
| **State Transitions**         | Test how the system handles changes in state.                  | A user logs out and then submits a request.                    |
| **Algorithmic Complexity**    | Test with varying sizes to observe how performance scales.      | Sorting an array: Test with 1,000 and 1,000,000 elements.      |
| **Past Bug Patterns**         | Look at previously reported bugs and target similar areas.      | A known off-by-one error was fixed: Test similar boundary inputs again. |

</details>

## Tasks
### 0. Integers addition
Write a function that adds 2 integers.
**Prototype:** ``def add_integer(a, b=98):``
- ``a`` and ``b`` must be integers or floats, otherwise raise a ``TypeError`` exception with the message ``a must be an integer`` or ``b must be an integer``
- ``a`` and ``b`` must be first casted to integers if they are float
- Returns an integer: the addition of ``a`` and ``b``
- You are not allowed to import any module
```bash
$ cat 0-main.py
#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)

$ ./0-main.py
3
98
100
98
b must be an integer
a must be an integer
$ python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
9 passed and 0 failed.
Test passed.
$ python3 -c 'print(__import__("0-add_integer").__doc__)' | wc -l
5
$ python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)' | wc -l
3
``` 
### 1. Divide a matrix
Write a function that divides all elements of a matrix.
**Prototype:** ``def matrix_divided(matrix, div):``
- ``matrix`` must be a list of lists of integers or floats, otherwise raise a ``TypeError`` exception with the message ``matrix must be a matrix (list of lists) of integers/floats``
- Each row of the ``matrix`` must be of the same size, otherwise raise a ``TypeError`` exception with the message ``Each row of the matrix must have the same size``
- ``div`` must be a number (integer or float), otherwise raise a ``TypeError`` exception with the message ``div must be a number``
- ``div`` can’t be equal to 0, otherwise raise a ZeroDivisionError exception with the message ``division by zero``
- All elements of the matrix should be divided by ``div``, rounded to 2 decimal places
- Returns a new matrix
- You are not allowed to import any module
```bash
$ cat 2-main.py
#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

$ ./2-main.py
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
[[1, 2, 3], [4, 5, 6]]
$ python3 -m doctest -v ./tests/2-matrix_divided.txt | tail -2
5 passed and 0 failed.
Test passed.
```
Note: you might have a different number of tests than in the above example. As usual, your tests should cover all possible cases.

### 2. Say my name
Write a function that prints ``My name is <first name> <last name>``
**Prototype:** ``def say_my_name(first_name, last_name=""):``
- ``first_name`` and ``last_name`` must be strings otherwise, raise a TypeError exception with the message ``first_name must be a string or last_name must be a string``
- You are not allowed to import any module
```bash
$ cat 3-main.py
#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)

$ ./3-main.py | cat -e
My name is John Smith$
My name is Walter White$
My name is Bob $
first_name must be a string$
$ python3 -m doctest -v ./tests/3-say_my_name.txt | tail -2
5 passed and 0 failed.
Test passed.
```
Note: you might have a different number of tests than in the above example. As usual, your tests should cover all possible cases.

### 3. Print square
Write a function that prints a square with the character ``#``.
**Prototype:** ``def print_square(size):``
- ``size`` is the size length of the square
- ``size`` must be an integer, otherwise raise a ``TypeError`` exception with the message ``size must be an integer``
- if ``size`` is less than ``0, raise a ``ValueError`` exception with the message ``size must be >= 0``
- if ``size`` is a float and is less than ``0``, raise a ``TypeError`` exception with the message ``size must be an integer``
- You are not allowed to import any module
```bash
$ cat 4-main.py
#!/usr/bin/python3
print_square = __import__('4-print_square').print_square

print_square(4)
print("")
print_square(10)
print("")
print_square(0)
print("")
print_square(1)
print("")
try:
    print_square(-1)
except Exception as e:
    print(e)
print("")

$ ./4-main.py
####
####
####
####

##########
##########
##########
##########
##########
##########
##########
##########
##########
##########


#

size must be >= 0

$ python3 -m doctest -v ./tests/4-print_square.txt
```

### 4. Text indentation
Write a function that prints a text with 2 new lines after each of these characters: ``.``, ``?`` and ``:``
**Prototype:** ``def text_indentation(text):``
- ``text`` must be a string, otherwise raise a ``TypeError`` exception with the message ``text must be a string``
- There should be no space at the beginning or at the end of each printed line
- You are not allowed to import any module
```bash
$ cat 5-main.py
#!/usr/bin/python3
text_indentation = __import__('5-text_indentation').text_indentation

text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")

$ ./5-main.py | cat -e
Lorem ipsum dolor sit amet, consectetur adipiscing elit.$
$
Quonam modo?$
$
Utrum igitur tibi litteram videor an totas paginas commovere?$
$
Non autem hoc:$
$
igitur ne illud quidem.$
$
Fortasse id optimum, sed ubi illud:$
$
Plus semper voluptatis?$
$
Teneo, inquit, finem illi videri nihil dolere.$
$
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum rationi oboediens.$
$
Si id dicis, vicimus.$
$
Inde sermone vario sex illa a Dipylo stadia confecimus.$
$
Sin aliud quid voles, postea.$
$
Quae animi affectio suum cuique tribuens atque hanc, quam dico.$
$
Utinam quidem dicerent alium alio beatiorem! Iam ruinas videres$
$ python3 -m doctest -v ./tests/5-text_indentation.txt
```

### 5. Max integer - Unittest
Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.
In this task, you will write unittests for the function ``def max_integer(list=[]):``.
- Your test file should be inside a folder ``tests``
- You have to use the [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
- Your test file should be python files (extension: ``.py``)
- Your test file should be executed by using this command: ``python3 -m unittest tests.6-max_integer_test``
- All tests you make must be passable by the function below
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case
```bash
$ cat 6-max_integer.py
#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

$ 
$ cat 6-main.py
#!/usr/bin/python3
max_integer = __import__('6-max_integer').max_integer

print(max_integer([1, 2, 3, 4]))
print(max_integer([1, 3, 4, 2]))
$
$ ./6-main.py
4
4
$
$ python3 -m unittest tests.6-max_integer_test 2>&1 | tail -1
OK
$
$ head -7 tests/6-max_integer_test.py 
#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
```

### 6. Matrix multiplication
Write a function that multiplies 2 matrices:
Read: [Matrix multiplication - only Matrix product (two matrices)](https://en.wikipedia.org/wiki/Matrix_multiplication)
**Prototype:** ``def matrix_mul(m_a, m_b):``
- ``m_a`` and ``m_b`` must be validated with these requirements in this order
- ``m_a`` and ``m_b`` must be an list of lists of integers or floats:
    + if ``m_a`` or ``m_b`` is not a list: raise a ``TypeError`` exception with the message ``m_a must be a list or m_b must be a list``
    + if ``m_a`` or ``m_b`` is not a list of lists: raise a ``TypeError`` exception with the message`` m_a must be a list of lists or m_b must be a list of lists``
    + if ``m_a`` or ``m_b`` is empty (it means: ``= []`` or ``= [[]]``): raise a ``ValueError`` exception with the message ``m_a can't be empty or m_b can't be empty``
    + if one element of those list of lists is not an integer or a float: raise a ``TypeError`` exception with the message ``m_a should contain only integers or floats`` or ``m_b should contain only integers or floats``
    + if ``m_a`` or ``m_b`` is not a rectangle (all ‘rows’ should be of the same size): raise a ``TypeError`` exception with the message ``each row of m_a must be of the same size`` or ``each row of m_b must be of the same size``
- If ``m_a`` and ``m_b`` can’t be multiplied: raise a ``ValueError`` exception with the message ``m_a and m_b can't be multiplied``
- You are not allowed to import any module
```bash
$ cat 100-main.py
#!/usr/bin/python3
matrix_mul = __import__('100-matrix_mul').matrix_mul

print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))

$ ./100-main.py 
[[7, 10], [15, 22]]
[[13, 16]]
$ python3 -m doctest -v ./tests/100-matrix_mul.txt | tail -2
6 passed and 0 failed.
Test passed.
```
### 7. Lazy matrix multiplication
Write a function that multiplies 2 matrices by using the module [NumPy](https://numpy.org/)
To install it: ``pip3 install numpy==1.15.0``
**Prototype:** ``def lazy_matrix_mul(m_a, m_b):``
Test cases should be the same as ``100-matrix_mul`` but with new exception type/message
```bash
$ cat 101-main.py
#!/usr/bin/python3
lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul

print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))

$ ./101-main.py 
[[ 7 10]
 [15 22]]
[[13 16]]
$ python3 -m doctest -v ./tests/101-lazy_matrix_mul.txt 
```
### 8. CPython #3: Python Strings
Create a function that prints Python strings.
**Prototype:** ``void print_python_string(PyObject *p);``
- Format: see example
- If ``p`` is not a valid string, print an error message (see example)
- Read: [Unicode HOWTO](https://docs.python.org/3.4/howto/unicode.html)

About:
- Python version: 3.4
- You are allowed to use the C standard library
- Your shared library will be compiled with this command line: ``gcc -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c``
```bash
julien@ubuntu:~/0x07. Pyhton Strings$ cat 102-tests.py
import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_string.argtypes = [ctypes.py_object]
s = "The spoon does not exist"
lib.print_python_string(s)
s = "ложка не существует"
lib.print_python_string(s)
s = "La cuillère n'existe pas"
lib.print_python_string(s)
s = "勺子不存在"
lib.print_python_string(s)
s = "숟가락은 존재하지 않는다."
lib.print_python_string(s)
s = "スプーンは存在しない"
lib.print_python_string(s)
s = b"The spoon does not exist"
lib.print_python_string(s)
julien@ubuntu:~/0x07. Pyhton Strings$ gcc -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 102-python.c
julien@ubuntu:~/0x07. Pyhton Strings$ python3 ./102-tests.py
[.] string object info
  type: compact ascii
  length: 24
  value: The spoon does not exist
[.] string object info
  type: compact unicode object
  length: 19
  value: ложка не существует
[.] string object info
  type: compact unicode object
  length: 24
  value: La cuillère n'existe pas
[.] string object info
  type: compact unicode object
  length: 5
  value: 勺子不存在
[.] string object info
  type: compact unicode object
  length: 14
  value: 숟가락은 존재하지 않는다.
[.] string object info
  type: compact unicode object
  length: 10
  value: スプーンは存在しない
[.] string object info
  [ERROR] Invalid String Object
```
