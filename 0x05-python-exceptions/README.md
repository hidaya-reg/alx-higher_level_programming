# 0x05-python-exceptions
## Resources
- [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Learn to Program 11 Static & Exception Handling](https://www.youtube.com/watch?v=7vbgD-3s-w4&ab_channel=DerekBanas) (starting at minute 7)
## Learning Objectives
<details>
<summary>What’s the difference between errors and exceptions</summary>

### Errors vs Exceptions
In Python, **errors** and **exceptions** both represent issues that occur during the execution of a program, but they have distinct roles:

**1. Errors:** These are issues that prevent the program from executing. They often represent problems that can't be handled or recovered from. Errors are typically related to the syntax or other structural issues in the code.

- Example: ``SyntaxError`` occurs when the parser encounters code that doesn’t follow Python’s syntax rules.
Errors usually stop the program's execution immediately unless they are handled. Common errors in Python are:

- ``SyntaxError``
- ``IndentationError``
- ``TypeError`` (can sometimes be caught as an exception but often indicates a fundamental issue).

**2. Exceptions:** These are raised when an error occurs during the program's execution, but they can be caught and handled to prevent the program from crashing. Exceptions allow you to gracefully manage unexpected situations and continue running the program.

- Example: ``ZeroDivisionError`` is an exception raised when a number is divided by zero.
You can handle exceptions using try-except blocks:
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```
Common exceptions include:
- ``ValueError``
- ``KeyError``
- ``IndexError``
- ``FileNotFoundError``

#### Summary:
**- Errors** are more structural and usually stop the program outright (e.g., syntax issues).
**- Exceptions** occur during execution but can be caught and handled to allow the program to continue running.
</details>
<details>
<summary>What are exceptions and how to use them</summary>

### What Are Exceptions?
Exceptions in Python are events that occur during the execution of a program and disrupt its normal flow. They are a type of runtime error that can be anticipated and handled, allowing the program to continue running or fail gracefully. When an exception is raised, it stops the normal flow of the program unless it is caught and handled using exception handling mechanisms.
For example, trying to divide by zero or accessing a non-existent key in a dictionary will raise exceptions like ``ZeroDivisionError`` or ``KeyError``.
#### Key Concepts of Exceptions:
**- Raising an exception:** An exception is raised when an error occurs during the program's execution.
**- Handling exceptions:** You can use ``try-except`` blocks to catch exceptions and prevent the program from crashing.
**- Custom exceptions:** You can define your own exceptions by creating custom exception classes.

#### Common Built-in Exceptions:
- ``ValueError``: Raised when a function gets an argument of the correct type but inappropriate value.
- ``KeyError``: Raised when trying to access a dictionary key that doesn’t exist.
- ``IndexError``: Raised when trying to access an invalid index in a list or tuple.
- ``FileNotFoundError``: Raised when trying to open a file that does not exist.
- ``ZeroDivisionError``: Raised when dividing a number by zero.

#### How to Use Exceptions in Python
##### 1. Basic Exception Handling Using try-except:
- Use a ``try`` block to wrap code that may raise an exception.
- Use an ``except`` block to specify how to handle that exception.
Example:
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```
In this example, the code in the try block raises a ZeroDivisionError, but it is caught in the except block, so the program doesn’t crash.

##### 2. Handling Multiple Exceptions: You can handle different exceptions in the same block.
Example:
```python
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ValueError:
    print("Invalid input! Please enter a valid number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
```
In this example, either a ``ValueError`` or ``ZeroDivisionError`` might occur, and each is handled differently.

##### 3. Using ``else`` with ``try-except``: You can use an ``else`` block to execute code if no exceptions occur.
Example:
```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("The result is", result)
```
The ``else`` block runs only if no exceptions are raised in the ``try`` block.

##### 4. The ``finally`` Block: 
The ``finally`` block always executes, whether an exception occurs or not. It’s typically used for cleanup actions (e.g., closing a file or releasing a resource).
```python
try:
    file = open('example.txt', 'r')
except FileNotFoundError:
    print("File not found")
finally:
    print("This will always execute, whether an exception occurred or not.")
    # Close the file if it's open
    if 'file' in locals() and not file.closed:
        file.close()
```
##### 5. Raising Exceptions: 
You can raise exceptions manually using the ``raise`` keyword.
```python
def check_value(value):
    if value < 0:
        raise ValueError("Negative values are not allowed")
    return value

try:
    check_value(-5)
except ValueError as e:
    print(e)  # Output: Negative values are not allowed
```
##### 6. Custom Exceptions: 
You can define your own exceptions by creating a new class that inherits from Python’s built-in ``Exception`` class.
```python
class MyCustomError(Exception):
    pass

try:
    raise MyCustomError("An error occurred")
except MyCustomError as e:
    print(e)  # Output: An error occurred
```
</details>
<details>
<summary>When do we need to use exceptions</summary>

### Use Exceptions in Python
You should use exceptions in Python when you anticipate situations where your code might encounter **unexpected conditions** or **runtime errors**. Exceptions allow you to handle these situations gracefully without crashing your program. Below are common scenarios when using exceptions is necessary or helpful:

#### 1. Handling User Input Errors
When your program takes input from users, you can't always guarantee that they will provide valid data. Exceptions help handle invalid inputs without breaking the flow of your program.
```python
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input. Please enter a number.")
```

#### 2. Dealing with File Operations
File operations like reading, writing, or opening files can fail due to various reasons, such as the file not existing or lacking permissions. Exceptions allow you to handle these errors and take appropriate action, like notifying the user or creating the file.
```python
try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("The file doesn't exist.")
```                                                               
Without this, your program would crash if the file was missing.

#### 3. Network/IO Operations
Network-related operations (e.g., fetching data from an API) or I/O operations (e.g., reading from or writing to a device) are prone to failure. These operations might fail due to timeouts, connection issues, or incorrect data formats.
```python
import requests

try:
    response = requests.get("https://example.com")
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
```
Here, exceptions handle cases where the HTTP request fails.

#### 4. Preventing Division by Zero
In mathematical operations, certain conditions (like dividing by zero) can lead to runtime errors. Handling such cases using exceptions helps keep the program running smoothly.
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero.")
```
Without this, the program would crash.

#### 5. Accessing Non-Existent Dictionary Keys or List Indexes
If you're working with dictionaries or lists and try to access a key or index that doesn't exist, it will raise an exception. Handling these errors helps prevent unexpected crashes.
```python
my_dict = {"name": "John"}
try:
    print(my_dict["age"])
except KeyError:
    print("Key not found in the dictionary.")
```
#### 6. Validation of Preconditions
When certain functions or operations require specific preconditions (like non-negative numbers), you can raise exceptions to handle invalid states.
```python
def square_root(x):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number")
    return x ** 0.5
```
This helps ensure that your function doesn’t process invalid data.

#### 7. Resource Cleanup
When working with resources like file handles, network connections, or database connections, you need to ensure proper cleanup, even when errors occur. Using the ``finally`` block ensures that resources are released regardless of what happens in the code.
```python
try:
    file = open("data.txt", "r")
    # Do something with the file
except FileNotFoundError:
    print("File not found")
finally:
    if file:
        file.close()
```
#### 8. Working with External Libraries
When you use external libraries (e.g., for database connections, APIs, etc.), errors may arise from these interactions. Handling exceptions allows you to anticipate and manage errors like database connection failures or API rate limits.
```python
import sqlite3

try:
    conn = sqlite3.connect('nonexistent.db')
except sqlite3.DatabaseError as e:
    print(f"Database error: {e}")
```
#### 9. Failing Gracefully in Critical Applications
In critical systems like servers or applications managing important data, you don’t want the whole system to crash when a minor issue occurs. Instead, use exceptions to log errors and take corrective action.
```python
try:
    # Critical operation, like processing a payment
    process_payment()
except PaymentError as e:
    # Log error and notify the user without crashing the system
    log_error(e)
    print("Payment failed. Please try again.")
```
#### 10. Creating Custom Exceptions for Specialized Errors
In complex applications, it’s a good practice to define custom exceptions for specific error cases to make debugging and error tracking easier. This is especially useful when standard Python exceptions don't clearly convey the problem.
```python
class InsufficientFundsError(Exception):
    pass

def withdraw(amount, balance):
    if amount > balance:
        raise InsufficientFundsError("You cannot withdraw more than your balance")
    return balance - amount
```
</details>
<details>
<summary>How to correctly handle an exception</summary>

### Handling exceptions
#### 1. Use ``try-except`` Blocks for Code That Might Fail
Wrap the code that might raise an exception in a try block, and use except to handle specific exceptions. This ensures that the program doesn’t crash when an error occurs.
```python
try:
    result = 10 / int(input("Enter a number: "))
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Please enter a valid integer.")
```
In this case:
- ``ZeroDivisionError`` is caught if the user tries to divide by zero.
- ``ValueError`` is caught if the input is not a valid integer.
#### 2. Handle Specific Exceptions (Avoid Catching Everything)
It is a bad practice to use a bare except clause, as it will catch all exceptions, even ones you didn’t anticipate. Always specify the exceptions you expect.
**Correct Example:**
```python
try:
    result = 10 / int(input("Enter a number: "))
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input, please enter a number.")
```
**Incorrect Example:**
```python
try:
    result = 10 / int(input("Enter a number: "))
except:
    print("Something went wrong.")  # Not specific, hides errors
```
Catching all exceptions makes debugging harder because it can mask other issues that you did not expect.

#### 3. Log or Handle the Exception Properly
In many cases, simply printing an error message is not enough. For larger applications, it’s a good practice to log the error or take appropriate action depending on the exception.
```python
import logging

logging.basicConfig(filename='app.log', level=logging.ERROR)

try:
    file = open('data.txt', 'r')
except FileNotFoundError as e:
    logging.error("File not found: %s", e)
    print("The file could not be found. Please check the filename.")
```
Here, the exception is logged with detailed information, making it easier to troubleshoot later.

#### 4. Use ``else`` to Separate Success from Exception Handling
The else block runs if no exceptions were raised, providing a clear separation between normal execution and error handling.
```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"The result is {result}")
```
In this example, the ``else`` block will run only if no exceptions occur. This keeps the ``try`` block focused on the operation that might fail and the ``else`` block on what should happen if it succeeds.

#### 5. Use ``finally`` for Cleanup Operations
The ``finally`` block runs whether an exception occurred or not. It is useful for releasing resources like closing files or network connections, ensuring cleanup even in the case of errors.
```python
try:
    file = open('data.txt', 'r')
    # Process the file
except FileNotFoundError:
    print("File not found.")
finally:
    if 'file' in locals() and not file.closed:
        file.close()
```
Here, the file is closed whether or not an exception occurs, ensuring resource cleanup.

#### 6. Raise Exceptions When Necessary
Sometimes, instead of silently handling an error, you might want to raise an exception so that it can be handled by the calling code. This is useful when you're writing functions that need to notify their caller about failures.
```python
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")
```
#### 7. Use Custom Exceptions for Specific Error Handling
For more complex programs, you can define custom exceptions to represent specific errors in your domain. This makes your code more readable and easier to debug.
```python
class InsufficientFundsError(Exception):
    pass

def withdraw(amount, balance):
    if amount > balance:
        raise InsufficientFundsError("You cannot withdraw more than your balance.")
    return balance - amount

try:
    balance = withdraw(100, 50)
except InsufficientFundsError as e:
    print(e)  # Output: You cannot withdraw more than your balance.
```
Custom exceptions allow you to handle specific error conditions cleanly and informatively.

#### 8. Re-Raise Exceptions When Necessary
In some cases, after catching an exception, you may want to handle it partially and re-raise it to allow other parts of your program to handle it too.
```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Caught division by zero.")
    raise  # Re-raises the exception for further handling
```
#### 9. Avoid Silent Failure (Don’t Ignore Exceptions)
It’s essential to avoid writing code that completely ignores exceptions. Even if you don’t want to handle an exception right away, logging it or providing some form of feedback is important.

**Incorrect Example:**
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    pass  # Silent failure, problem ignored
```
**Correct Example:**
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero occurred, please check your input.")
```
#### 10. Use Exception Chaining (``raise from``)
When handling one exception leads to another, you can chain exceptions using raise from to maintain the original context of the exception. This provides better tracebacks and error context.
```python
try:
    raise ValueError("Original error")
except ValueError as e:
    raise RuntimeError("Secondary error occurred") from e
```

</details>
<details>
<summary>What’s the purpose of catching exceptions</summary>

### Purpose of catching exceptions
#### 1. Graceful Error Handling
Catching exceptions allows you to handle errors in a user-friendly way instead of letting the program crash abruptly. You can display error messages, retry the operation, or take alternative actions.
```python
try:
    file = open('data.txt', 'r')
except FileNotFoundError:
    print("Error: The file could not be found. Please check the file path.")
```
Without catching the exception, the program would crash if the file doesn’t exist. With the exception handled, the program can notify the user and continue running.

#### 2. Preventing Program Crashes
When an exception occurs, if it's not handled, it will terminate the program and generate a stack trace (error message). By catching exceptions, you can ensure that the program continues running or shuts down gracefully.
```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
```
Here, the program would crash if the user entered non-numeric input, but catching the exception allows the program to continue after displaying an error message.

#### 3. Allowing Program Continuity
By catching exceptions, your program can continue executing other tasks even when one part of it fails. For example, in a loop processing many files, you can catch errors for individual files but continue processing others.
```python
files = ['file1.txt', 'file2.txt', 'missing_file.txt']
for file_name in files:
    try:
        with open(file_name, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"{file_name} not found, skipping...")
```
Here, if one file is missing, the program skips it but processes the others, rather than halting entirely.

#### 4. Customizing Error Responses
Catching exceptions gives you control over how to respond to different errors. Instead of letting Python’s default error messages appear, you can create custom responses that are more informative or appropriate for your application.
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Oops! You can't divide by zero.")
```
In this case, the custom error message is more user-friendly than a raw traceback, providing a clear explanation to the user.

#### 5. Resource Cleanup (``finally``)
When your code uses external resources (like files, network connections, or database connections), exceptions might prevent you from releasing these resources properly. By catching exceptions, you can use a ``finally`` block to ensure cleanup, no matter what happens in the code.
```python
try:
    file = open('data.txt', 'r')
    # Do something with the file
except FileNotFoundError:
    print("File not found.")
finally:
    if file:
        file.close()
```
Even if an exception occurs, the finally block ensures that the file is closed properly.

#### 6. Debugging and Logging
Catching exceptions allows you to log the errors for later analysis or debugging. This is especially important in production environments, where you want to know what went wrong without crashing the entire system.
```python
import logging

logging.basicConfig(filename='app.log', level=logging.ERROR)

try:
    10 / 0
except ZeroDivisionError as e:
    logging.error(f"Error occurred: {e}")
```
Here, the error is logged in a file, making it easier to troubleshoot the issue later.

#### 7. Making Code More Robust
Catching exceptions allows you to anticipate potential issues and provide alternative solutions or fallback mechanisms. This makes your code more robust, able to handle a variety of error conditions without breaking.
```python
try:
    with open('data.txt', 'r') as file:
        data = file.read()
except FileNotFoundError:
    # Provide default data if the file is missing
    data = "Default data"
```
If the file is missing, the program can still proceed using default data instead of stopping.

#### 8. Handling External System Failures
When your program interacts with external systems (e.g., databases, APIs, or networks), you can’t always control or predict their behavior. Exceptions help manage failures in these systems without crashing your program.
```python
import requests

try:
    response = requests.get('https://example.com/api')
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"API request failed: {e}")
```
Even if the API request fails due to network issues or bad responses, your program can handle the failure and continue running.

#### 9. Separation of Normal and Error Logic
Catching exceptions allows you to separate normal application logic from error handling, making the code easier to read and maintain. The main logic stays in the ``try`` block, while error handling is kept in ``except``.
```python
try:
    result = 10 / int(input("Enter a number: "))
except ZeroDivisionError:
    print("You can't divide by zero.")
except ValueError:
    print("Please enter a valid number.")
else:
    print(f"The result is {result}")
```
The separation of logic (with ``else``) keeps the error-handling part distinct from the main computation logic.

#### 10. Supporting Failsafe Mechanisms
When handling critical operations (e.g., processing payments, transferring data), catching exceptions allows you to implement failsafe mechanisms, ensuring that the program can recover from or roll back failed operations.
```python
try:
    process_payment()
except PaymentError:
    print("Payment failed, reverting transaction.")
    revert_transaction()
```
Even if the payment processing fails, you can handle it and execute a rollback to avoid further issues.
</details>
<details>
<summary>How to raise a builtin exception</summary>

### Raising a Built-in Exception
#### Syntax 
```python
raise ExceptionType("Optional error message")
```
Where:
- ``ExceptionType`` is the built-in exception class (e.g., ``ValueError``, ``TypeError``, etc.).
- The optional error message provides additional context or explanation for the raised exception.
#### Customizing the Exception Message
You can provide detailed messages to exceptions to give more context about the error.
```python
def check_name(name):
    if not isinstance(name, str):
        raise TypeError(f"Expected a string, got {type(name).__name__}")
    if len(name) < 3:
        raise ValueError("Name should be at least 3 characters long.")
    print(f"Name is valid: {name}")

check_name(123)  # Raises TypeError: Expected a string, got int
check_name("Ed")  # Raises ValueError: Name should be at least 3 characters long.
```
</details>

## Tasks
### 0. Safe list printing
Write a function that prints ``x`` elements of a list.
**Prototype:** ``def safe_print_list(my_list=[], x=0):``
- ``my_list`` can contain any type (integer, string, etc.)
- All elements must be printed on the same line followed by a new line.
- ``x`` represents the number of elements to print
- ``x`` can be bigger than the length of ``my_list``
- Returns the real number of elements printed
- You have to use ``try: / except:``
- You are not allowed to import any module
- You are not allowed to use ``len()``
```bash
$ cat 0-main.py
#!/usr/bin/python3
safe_print_list = __import__('0-safe_print_list').safe_print_list

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

$ ./0-main.py
12
nb_print: 2
12345
nb_print: 5
12345
nb_print: 5
```
### 1. Safe printing of an integers list
Write a function that prints an integer with ``"{:d}".format()``.
**Prototype:** ``def safe_print_integer(value):``
- ``value`` can be any type (integer, string, etc.)
- The integer should be printed followed by a new line
- Returns ``True`` if ``value`` has been correctly printed (it means the ``value`` is an integer)
- Otherwise, returns ``False``
- You have to use ``try: / except:``
- You have to use ``"{:d}".format()`` to print as integer
- You are not allowed to import any module
- You are not allowed to use ``type()``
```bash
$ cat 1-main.py
#!/usr/bin/python3
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

$ ./1-main.py
89
-89
School is not an integer
```
### 2. Print and count integers
Write a function that prints the first ``x`` elements of a list and only integers.
**Prototype:** ``def safe_print_list_integers(my_list=[], x=0):``
- ``my_list`` can contain any type (integer, string, etc.)
- All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
- ``x`` represents the number of elements to access in ``my_list``
- ``x`` can be bigger than the length of ``my_list`` - if it’s the case, an exception is expected to occur
- Returns the real number of integers printed
- You have to use ``try: / except:``
- You have to use ``"{:d}".format()`` to print an integer
- You are not allowed to import any module
- You are not allowed to use ``len()``
```bash
$ cat 2-main.py
#!/usr/bin/python3
safe_print_list_integers = \
    __import__('2-safe_print_list_integers').safe_print_list_integers

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

$ ./2-main.py
12
nb_print: 2
12345
nb_print: 5
12345Traceback (most recent call last):
  File "./2-main.py", line 14, in <module>
    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
  File "/0x05/2-safe_print_list_integers.py", line 7, in safe_print_list_integers
    print("{:d}".format(my_list[i]), end="")
IndexError: list index out of range
```
### 3. Integers division with debug
Write a function that divides 2 integers and prints the result.

**Prototype:** ``def safe_print_division(a, b):``
- You can assume that ``a`` and ``b`` are integers
- The result of the division should print on the ``finally:`` section preceded by ``Inside result:``
- Returns the value of the division, otherwise: ``None``
- You have to use ``try: / except: / finally:``
- You have to use ``"{}".format()`` to print the result
- You are not allowed to import any module
```bash
$ cat 3-main.py
#!/usr/bin/python3
safe_print_division = __import__('3-safe_print_division').safe_print_division

a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

$ ./3-main.py
Inside result: 6.0
12 / 2 = 6.0
Inside result: None
12 / 0 = None
```
### 4. Divide a list
Write a function that divides element by element 2 lists.
**Prototype:** ``def list_division(my_list_1, my_list_2, list_length):``
- ``my_list_1`` and ``my_list_2`` can contain any type (integer, string, etc.)
- ``list_length`` can be bigger than the length of both lists
- Returns a new list (length = ``list_length``) with all divisions
- If 2 elements can’t be divided, the division result should be equal to ``0``
- If an element is not an integer or float:
    + print: ``wrong type``
- If the division can’t be done (``/0``):
    + print: ``division by 0``
- If ``my_list_1`` or ``my_list_2`` is too short
    + print: ``out of range``
- You have to use ``try: / except: / finally:``
- You are not allowed to import any module
```bash
$ cat 4-main.py
#!/usr/bin/python3
list_division = __import__('4-list_division').list_division

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

$ ./4-main.py
[5.0, 2.0, 1.0]
--
division by 0
wrong type
out of range
[5.0, 0, 0, 2.0, 0]
```
### 5. Raise exception
Write a function that raises a type exception.
**Prototype:** ``def raise_exception():``
- You are not allowed to import any module
```bash
$ cat 5-main.py
#!/usr/bin/python3
raise_exception = __import__('5-raise_exception').raise_exception

try:
    raise_exception()
except TypeError as te:
    print("Exception raised")

$ ./5-main.py
Exception raised
```
### 6. Raise a message
Write a function that raises a name exception with a message.
**Prototype:** ``def raise_exception_msg(message=""):``
- You are not allowed to import any module
```bash
$ cat 6-main.py
#!/usr/bin/python3
raise_exception_msg = __import__('6-raise_exception_msg').raise_exception_msg

try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)

$ ./6-main.py
C is fun
```
### 7. Safe integer print with error message
Write a function that prints an integer.

**Prototype:** def safe_print_integer_err(value):
- ``value`` can be any type (integer, string, etc.)
- The integer should be printed followed by a new line
- Returns ``True`` if ``value`` has been correctly printed (it means the ``value`` is an integer)
- Otherwise, returns ``False`` and prints in ``stderr`` the error precede by ``Exception:``
- You have to use ``try: / except:``
- You have to use ``"{:d}".format()`` to print as integer
- You are not allowed to use ``type()``
```bash
$ cat 100-main.py
#!/usr/bin/python3
safe_print_integer_err = \
    __import__('100-safe_print_integer_err').safe_print_integer_err

value = 89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer_err(value)
if not has_been_print:
    print("{} is not an integer".format(value))

$ ./100-main.py
89
-89
Exception: Unknown format code 'd' for object of type 'str'
School is not an integer
$ ./100-main.py 2> /dev/null
89
-89
School is not an integer
```
### 8. Safe function
Write a function that executes a function safely.
**Prototype:** ``def safe_function(fct, *args):``
- You can assume ``fct`` will be always a pointer to a function
- Returns the result of the function,
- Otherwise, returns ``None`` if something happens during the function and prints in ``stderr`` the error precede by ``Exception:``
- You have to use ``try: / except:``
```bash
$ cat 101-main.py
#!/usr/bin/python3
safe_function = __import__('101-safe_function').safe_function


def my_div(a, b):
    return a / b

result = safe_function(my_div, 10, 2)
print("result of my_div: {}".format(result))

result = safe_function(my_div, 10, 0)
print("result of my_div: {}".format(result))


def print_list(my_list, len):
    i = 0
    while i < len:
        print(my_list[i])
        i += 1
    return len

result = safe_function(print_list, [1, 2, 3, 4], 10)
print("result of print_list: {}".format(result))

$ ./101-main.py
result of my_div: 5.0
Exception: division by zero
result of my_div: None
1
2
3
4
Exception: list index out of range
result of print_list: None
$ ./101-main.py 2> /dev/null
result of my_div: 5.0
result of my_div: None
1
2
3
4
result of print_list: None
```
### 9. ByteCode -> Python #4
Write the Python function ``def magic_calculation(a, b):`` that does exactly the same as the following Python bytecode:
```
  3           0 LOAD_CONST               1 (0)
              3 STORE_FAST               2 (result)

  4           6 SETUP_LOOP              94 (to 103)
              9 LOAD_GLOBAL              0 (range)
             12 LOAD_CONST               2 (1)
             15 LOAD_CONST               3 (3)
             18 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             21 GET_ITER
        >>   22 FOR_ITER                77 (to 102)
             25 STORE_FAST               3 (i)

  5          28 SETUP_EXCEPT            49 (to 80)

  6          31 LOAD_FAST                3 (i)
             34 LOAD_FAST                0 (a)
             37 COMPARE_OP               4 (>)
             40 POP_JUMP_IF_FALSE       58

  7          43 LOAD_GLOBAL              1 (Exception)
             46 LOAD_CONST               4 ('Too far')
             49 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             52 RAISE_VARARGS            1
             55 JUMP_FORWARD            18 (to 76)

  9     >>   58 LOAD_FAST                2 (result)
             61 LOAD_FAST                0 (a)
             64 LOAD_FAST                1 (b)
             67 BINARY_POWER
             68 LOAD_FAST                3 (i)
             71 BINARY_TRUE_DIVIDE
             72 INPLACE_ADD
             73 STORE_FAST               2 (result)
        >>   76 POP_BLOCK
             77 JUMP_ABSOLUTE           22

 10     >>   80 POP_TOP
             81 POP_TOP
             82 POP_TOP

 11          83 LOAD_FAST                1 (b)
             86 LOAD_FAST                0 (a)
             89 BINARY_ADD
             90 STORE_FAST               2 (result)

 12          93 BREAK_LOOP
             94 POP_EXCEPT
             95 JUMP_ABSOLUTE           22
             98 END_FINALLY
             99 JUMP_ABSOLUTE           22
        >>  102 POP_BLOCK

 13     >>  103 LOAD_FAST                2 (result)
            106 RETURN_VALUE
```
Tip: [Python bytecode](https://docs.python.org/3.4/library/dis.html)

### 10. CPython #2: PyFloatObject
Create three C functions that print some basic info about Python lists, Python bytes an Python float objects.
- Python lists:
    + **Prototype:** ``void print_python_list(PyObject *p);``
    + Format: see example
    + If ``p`` is not a valid ``PyListObject``, print an error message (see example)
- Python bytes:
    + **Prototype:** ``void print_python_bytes(PyObject *p);``
    + Format: see example
    + Line “first X bytes”: print a maximum of 10 bytes
    + If ``p`` is not a valid ``PyBytesObject``, print an error message (see example)
- Python float:
    + **Prototype:** ``void print_python_float(PyObject *p);``
    + Format: see example
    + If ``p`` is not a valid ``PyFloatObject``, print an error message (see example)
    + Read ``/usr/include/python3.4/floatobject.h``
- About:
    + Python version: 3.4
    + You are allowed to use the C standard library
    + Your shared library will be compiled with this command line: ``gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c``
    + You are not allowed to use the following macros/functions:
        - ``Py_SIZE``
        - ``Py_TYPE``
        - ``PyList_Size``
        - ``PyList_GetItem``
        - ``PyBytes_AS_STRING``
        - ``PyBytes_GET_SIZE``
        - ``PyBytes_AsString``
        - ``PyBytes_AsStringAndSize``
        - ``PyFloat_AS_DOUBLE``
        - ``PySequence_GetItem``
        - ``PySequence_Fast_GET_SIZE``
        - ``PySequence_Fast_GET_ITEM``
        - ``PySequence_ITEM``
        - ``PySequence_Fast_ITEMS``
**NOTE:**
- The python script will be launched using the ``-u`` option (Force ``stdout`` to be unbuffered).
- It is strongly advised to either use ``setbuf(stdout, NULL);`` or ``fflush(stdout)`` in your C functions IF you choose to use ``printf``. The reason to that is that Python ``s`` print ``and libC``s ``printf`` don’t share the same buffer, and the output can appear disordered.
```bash
julien@ubuntu:~/CPython$ python3 --version
Python 3.4.3
julien@ubuntu:~/CPython$ gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c
julien@ubuntu:~/CPython$ cat 103-tests.py 
#!/usr/bin/python3 -u

import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_list.argtypes = [ctypes.py_object]
lib.print_python_bytes.argtypes = [ctypes.py_object]
lib.print_python_float.argtypes = [ctypes.py_object]
s = b"Hello"
lib.print_python_bytes(s);
b = b'\xff\xf8\x00\x00\x00\x00\x00\x00';
lib.print_python_bytes(b);
b = b'What does the \'b\' character do in front of a string literal?';
lib.print_python_bytes(b);
l = [b'Hello', b'World']
lib.print_python_list(l)
del l[1]
lib.print_python_list(l)
l = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], b"School", "Betty"]
lib.print_python_list(l)
l = []
lib.print_python_list(l)
l.append(0)
lib.print_python_list(l)
l.append(1)
l.append(2)
l.append(3)
l.append(4)
lib.print_python_list(l)
l.pop()
lib.print_python_list(l)
l = ["School"]
lib.print_python_list(l)
lib.print_python_bytes(l);
f = 3.14
lib.print_python_float(f);
l = [-1.0, -0.1, 0.0, 1.0, 3.14, 3.14159, 3.14159265, 3.141592653589793238462643383279502884197169399375105820974944592307816406286]
print(l)
lib.print_python_list(l);
lib.print_python_float(l);
lib.print_python_list(f);
julien@ubuntu:~/CPython$ ./103-tests.py 
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
[.] bytes object info
  size: 8
  trying string: ??
  first 9 bytes: ff f8 00 00 00 00 00 00 00
[.] bytes object info
  size: 60
  trying string: What does the 'b' character do in front of a string literal?
  first 10 bytes: 57 68 61 74 20 64 6f 65 73 20
[*] Python list info
[*] Size of the Python List = 2
[*] Allocated = 2
Element 0: bytes
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
Element 1: bytes
[.] bytes object info
  size: 5
  trying string: World
  first 6 bytes: 57 6f 72 6c 64 00
[*] Python list info
[*] Size of the Python List = 1
[*] Allocated = 2
Element 0: bytes
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
[*] Python list info
[*] Size of the Python List = 8
[*] Allocated = 8
Element 0: bytes
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
Element 1: int
Element 2: int
Element 3: float
[.] float object info
  value: 6.0
Element 4: tuple
Element 5: list
Element 6: bytes
[.] bytes object info
  size: 9
  trying string: School
  first 10 bytes: 48 6f 6c 62 65 72 74 6f 6e 00
Element 7: str
[*] Python list info
[*] Size of the Python List = 0
[*] Allocated = 0
[*] Python list info
[*] Size of the Python List = 1
[*] Allocated = 4
Element 0: int
[*] Python list info
[*] Size of the Python List = 5
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
Element 4: int
[*] Python list info
[*] Size of the Python List = 4
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
[*] Python list info
[*] Size of the Python List = 1
[*] Allocated = 1
Element 0: str
[.] bytes object info
  [ERROR] Invalid Bytes Object
[.] float object info
  value: 3.14
[-1.0, -0.1, 0.0, 1.0, 3.14, 3.14159, 3.14159265, 3.141592653589793]
[*] Python list info
[*] Size of the Python List = 8
[*] Allocated = 8
Element 0: float
[.] float object info
  value: -1.0
Element 1: float
[.] float object info
  value: -0.1
Element 2: float
[.] float object info
  value: 0.0
Element 3: float
[.] float object info
  value: 1.0
Element 4: float
[.] float object info
  value: 3.14
Element 5: float
[.] float object info
  value: 3.14159
Element 6: float
[.] float object info
  value: 3.14159265
Element 7: float
[.] float object info
  value: 3.141592653589793
[.] float object info
  [ERROR] Invalid Float Object
[*] Python list info
  [ERROR] Invalid List Object
```