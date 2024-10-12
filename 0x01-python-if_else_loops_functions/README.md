# 0x01. Python - if/else, loops, functions
## Resources
[More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html) (Read until “4.6. Defining Functions” included)
[IndentationError](https://www.youtube.com/watch?v=1QXOd2ZQs-Q&ab_channel=ATOM)
[How To Use String Formatters in Python 3](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3)
[Learn to Program 2 : Looping](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
[Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)

## Learning Objectives
<details>
<summary>Why indentation is so important in Python</summary>

### Indentation

| **Aspect**           | **Description**                                                                                                      |
|----------------------|----------------------------------------------------------------------------------------------------------------------|
| **Block Definition** | Indentation defines blocks of code, such as the body of functions, loops, and conditionals. Incorrect indentation can lead to `IndentationError` or unexpected behavior. |
| **Readability**      | Enhances the readability of the code, making it easier to understand the structure and flow. Consistent indentation helps identify grouped statements quickly. |
| **Syntax Enforcement** | Python enforces indentation rules as part of its syntax. Each level of indentation typically represents a different scope or block. Inconsistent indentation will lead to errors. |
| **Nested Structures** | Proper indentation is essential for nested structures (like loops within loops or conditionals) to indicate which blocks of code are associated with which control structures. |
| **Collaboration**    | Consistent indentation standards are vital in team environments to ensure all team members read and understand the code in the same way, reducing misunderstandings and errors. |

</details>
<details>
<summary>How to use the if, if ... else statements</summary>

### ``if``, ``if ... else`` statements

#### Basic ``if`` Statement
The simplest form of a conditional statement is the ``if`` statement. It checks a condition, and if the condition evaluates to ``True``, the code block under the ``if`` statement is executed.
Syntax:
```python
if condition:
    # Code to execute if condition is True
```

#### ``if ... else`` Statement
The ``if ... else`` statement allows you to provide an alternative block of code to execute if the condition evaluates to False.
Syntax:
```python
if condition:
    # Code to execute if condition is True
else:
    # Code to execute if condition is False
```

#### ``if ... elif ... else`` Statement
When you have multiple conditions to check, you can use elif (short for "else if") to handle additional conditions. You can have as many elif statements as needed.
Syntax:
```python
if condition1:
    # Code to execute if condition1 is True
elif condition2:
    # Code to execute if condition2 is True
else:
    # Code to execute if all conditions are False
```
#### Nested ``if`` Statements
You can also nest ``if`` statements within other ``if`` statements to check multiple conditions.
Example:
```python
age = 20
is_student = True

if age >= 18:
    if is_student:
        print("You are an adult student.")
    else:
        print("You are an adult.")
else:
    print("You are a minor.")
```

</details>
<details>
<summary>How to use the while and for loops</summary>

### ``while`` and ``for`` loops
#### ``while`` Loop
A ``while`` loop continues to execute a block of code as long as a specified condition is ``True``. Be careful to modify the condition within the loop; otherwise, it may result in an infinite loop.
Syntax:
```python
while condition:
    # Code to execute while condition is True
```
#### ``for`` Loop
A ``for`` loop is typically used to iterate over a sequence (like a list, tuple, string, or range). It executes a block of code for each item in the sequence.
Syntax:
```python
for item in sequence:
    # Code to execute for each item in the sequence
```
**Example with range():**
The ``range()`` function generates a sequence of numbers, which can be useful for creating loops that run a specific number of times.
```python
for i in range(5):
    print(i)
```
#### Using ``break`` and ``continue``
Both loops can be controlled further using ``break`` and ``continue`` statements.

- ``break``: Exits the loop prematurely.
```python
count = 0

while True:
    if count == 3:
        break  # Exit the loop when count is 3
    print(count)
    count += 1
```
**Output:**
```
0
1
2
```
- ``continue``: Skips the rest of the code inside the loop for the current iteration and moves to the next iteration.
```python
for i in range(5):
    if i == 2:
        continue  # Skip the rest of the loop when i is 2
    print(i)
```
**Output:**
```
0
1
3
4
```
</details>
<details>
<summary>How to use else clauses on loops</summary>

### ``else`` clauses on loops
#### Using ``else`` with ``for`` Loops
The else clause will execute after the ``for`` loop completes all its iterations, provided that it was not terminated by a break.
**Syntax:**
```python
for item in sequence:
    # Code to execute for each item
else:
    # Code to execute after the loop finishes
```
**Example:**
```python
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)
else:
    print("Loop completed successfully!")
```
**Output:**
```
1
2
3
4
5
Loop completed successfully!
```
#### Using ``else`` with ``while`` Loops
Similarly, the ``else`` clause will execute after the ``while`` loop, provided that it did not end due to a break statement.
**Syntax:**
```python
while condition:
    # Code to execute while condition is True
else:
    # Code to execute after the loop finishes
```
**Example:**
```python
count = 0

while count < 5:
    print(count)
    count += 1
else:
    print("While loop completed successfully!")
```
**Output:**
```
0
1
2
3
4
While loop completed successfully!
```
#### Example with ``break`` Statement
If you use a ``break`` statement inside the loop, the ``else`` block will not execute.
```python
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number == 3:
        print("Found 3, exiting the loop.")
        break
else:
    print("Loop completed successfully!")  # This won't execute
```
**Output:**
`Found 3, exiting the loop.`
#### Example with while and break:
```python
count = 0

while count < 5:
    if count == 3:
        print("Found 3, exiting the loop.")
        break
    count += 1
else:
    print("While loop completed successfully!")  # This won't execute
```
Output: `Found 3, exiting the loop.`

</details>
<details>
<summary>What does the pass statement do, and when to use it</summary>

### ``pass`` statement
The ``pass`` statement in Python is a null operation — it is a placeholder that does nothing when executed. It is often used in situations where a statement is syntactically required but you do not want to execute any code.

#### 1. Placeholder for Future Code
When you're working on a function or class but haven't implemented the logic yet, you can use pass to maintain the structure of your code without raising an error.
```python
def my_function():
    pass  # Implementation will be added later
```
#### 2. Empty Loop or Condition
You might want to create a loop or conditional statement without executing any action. ``pass`` allows you to do this without causing an error.
```python
for i in range(5):
    pass  # No action performed, loop just iterates

# Example with If Statement:
if condition_met:
    pass  # Placeholder for future code
else:
    print("Condition not met.")
```
#### 3. Creating Minimal Classes
When defining a class that you plan to flesh out later, pass can help you avoid syntax errors.
```python
class MyClass:
    pass  # Attributes and methods will be added later
```
#### 4. Building a Skeleton for Exception Handling
In a try block, you might want to handle an exception but choose not to take any action in that specific case. You can use ``pass`` to allow the program to continue running without doing anything.
```python
try:
    risky_operation()
except SomeException:
    pass  # Ignore the exception for now
```
</details>
<details>
<summary>How to use range</summary>

### ``range()`` function
The ``range()`` function in Python is a built-in function that generates a sequence of numbers, which is often used for iteration in loops.
#### Basic Syntax
The ``range()`` function can be called in several ways, depending on how many arguments you provide:

```python
range(stop)
range(start, stop)
range(start, stop, step)
```
``start``: The starting value of the sequence (inclusive). Defaults to 0.
``stop``: The end value of the sequence (exclusive).
``step``: The amount by which to increment the sequence. Defaults to 1.

#### Example:
```python
for i in range(10, 0, -1):
    print(i)
```
**Output:**
```
10
9
8
7
6
5
4
3
2
1
```
#### Converting range to a List
Since ``range()`` returns a range object (which is iterable), you can convert it to a list if you need to see all the values at once.
```python
numbers = list(range(5, 15, 3))
print(numbers)
```
**Output:** `[5, 8, 11, 14]`
</details>
<details>
<summary>What is a function and how do you use functions</summary>

### Functions in Python
A function in Python is a block of reusable code that performs a specific task. Functions help organize and modularize code, making it more readable, maintainable, and reusable.
**Basic Syntax:**
```python
def function_name(parameters):
    # Function body
    # Code to execute
    return value  # Optional
```
#### Function Parameters
Functions can accept parameters, which are values you pass into the function. You can also set default values for parameters.
**Example with Default Parameters:**
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
print(greet("Bob", "Hi"))  # Output: Hi, Bob!
```
#### Return Statement
The ``return`` statement is used to exit a function and send a value back to the caller. If no ``return`` statement is specified, the function will return ``None``.
```python
def multiply(x, y):
    return x * y

result = multiply(4, 5)
print(result)  # Output: 20
```
#### Variable Scope
Variables defined inside a function have **local scope** and cannot be accessed outside of that function. Conversely, variables defined outside the function have global scope and can be accessed anywhere.
```python
def my_function():
    local_var = 10  # Local variable
    return local_var

print(my_function())  # Output: 10
# print(local_var)    # This would raise a NameError
```
</details>
<details>
<summary>Scope of variables</summary>

### Scope of variables
In Python, the **scope** of a variable refers to the region of the program where that variable is accessible. Understanding variable scope is crucial for managing variables and preventing conflicts or unintended behavior in your code. There are four main types of variable scope in Python: **local**, **enclosing**, **global**, and **built-in**.

#### 1. Local Scope
- **Definition:** Variables defined within a function have local scope. They can only be accessed within that function.
- **Lifetime:** Local variables exist only while the function is executing.
```python
def my_function():
    local_var = "I am local"
    print(local_var)  # This will print "I am local"

my_function()
# print(local_var)  # This will raise a NameError because local_var is not accessible outside the function
```
#### 2. Enclosing Scope
- **Definition:** This refers to the scope of variables in the enclosing function, which is relevant when dealing with nested functions. Variables defined in an outer (enclosing) function are accessible to inner (nested) functions.
- **Lifetime:** Enclosing variables exist as long as the enclosing function is executing.
```python
def outer_function():
    outer_var = "I am from the outer function"

    def inner_function():
        print(outer_var)  # Accessing the variable from the enclosing scope

    inner_function()

outer_function()  # Output: I am from the outer function
```
#### 3. Global Scope
- **Definition:** Variables defined at the top level of a script or module have global scope. They can be accessed from any function or class within the same module.
- **Lifetime:** Global variables exist for the duration of the program execution.
```python
global_var = "I am global"

def my_function():
    print(global_var)  # This will print "I am global"

my_function()
print(global_var)  # This will also print "I am global"
```
#### 4. Built-in Scope
- **Definition:** Python has a set of built-in names (like print(), len(), etc.) that are always available in any scope. These names are predefined and part of the Python language.
- **Lifetime:** Built-in names are available as long as the Python interpreter is running
`print(len("Hello, World!"))  # len is a built-in function available in any scope`

#### Scope Resolution Order
When a variable is referenced, Python uses the **LEGB** rule to resolve the variable's scope:
- **L**ocal: The innermost scope, where the variable is defined.
- **E**nclosing: The scope of the enclosing function (if any).
- **G**lobal: The scope of the top-level script or module.
- **B**uilt-in: The scope of built-in names.

#### Using the ``global`` Keyword
If you want to modify a global variable inside a function, you need to declare it as global within that function.
```python
count = 0  # Global variable

def increment():
    global count  # Declare that we want to use the global variable
    count += 1

increment()
print(count)  # Output: 1
```
</details>

## Tasks
### 0. Positive anything is better than negative nothing
This program will assign a random signed number to the variable ``number`` each time it is executed. Complete the source code in order to print whether the number stored in the variable ``number`` is positive or negative.
- You can find the source code [here](https://github.com/alx-tools/0x01.py/blob/master/0-positive_or_negative_py)
- The variable ``number`` will store a different value every time you will run this program
- The output of the program should be:
    + The number, followed by
        - if the number is greater than 0: ``is positive``
        - if the number is 0: ``is zero``
        - if the number is less than 0: ``is negative``
    + followed by a new line
```bash
$ ./0-positive_or_negative.py 
-4 is negative
$ ./0-positive_or_negative.py 
0 is zero
$ ./0-positive_or_negative.py 
-3 is negative
$ ./0-positive_or_negative.py 
-10 is negative
$ ./0-positive_or_negative.py 
10 is positive
$ ./0-positive_or_negative.py 
-5 is negative
$ ./0-positive_or_negative.py 
6 is positive
$ ./0-positive_or_negative.py 
7 is positive
$ ./0-positive_or_negative.py 
5 is positive
```
### 1. The last digit
This program will assign a random signed number to the variable ``number`` each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable ``number``.
- You can find the source code [here](https://github.com/alx-tools/0x01.py/blob/master/1-last_digit_py)
- The variable ``number`` will store a different value every time you will run this program
- The output of the program should be:
    + The string ``Last digit of``, followed by
    + the number, followed by
    + the string ``is``, followed by the last digit of ``number``, followed by
        - if the last digit is greater than 5: the string ``and is greater than 5``
        - if the last digit is 0: the string ``and is 0``
        - if the last digit is less than 6 and not 0: the string ``and is less than 6 and not 0``
    + followed by a new line
```bash
$ ./1-last_digit.py
Last digit of 4205 is 5 and is less than 6 and not 0
$ ./1-last_digit.py
Last digit of -626 is -6 and is less than 6 and not 0
$ ./1-last_digit.py
Last digit of 1144 is 4 and is less than 6 and not 0
$ ./1-last_digit.py
Last digit of -9200 is 0 and is 0
$ ./1-last_digit.py
Last digit of 5247 is 7 and is greater than 5
$ ./1-last_digit.py
Last digit of -9318 is -8 and is less than 6 and not 0
$ ./1-last_digit.py
Last digit of 3369 is 9 and is greater than 5
$ ./1-last_digit.py
Last digit of -5224 is -4 and is less than 6 and not 0
$ ./1-last_digit.py
Last digit of -4485 is -5 and is less than 6 and not 0
$ ./1-last_digit.py
Last digit of 3850 is 0 and is 0
$ ./1-last_digit.py
Last digit of 5169 is 9 and is greater than 5
```
### 2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
- You can only use one ``print`` function with string format
- You can only use one loop in your code
- You are not allowed to store characters in a variable
- You are not allowed to import any module
```bash
$ ./2-print_alphabet.py
abcdefghijklmnopqrstuvwxyz$
```
### 3. When I was having that alphabet soup, I never thought that it would pay off
Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
- Print all the letters except ``q`` and ``e``
- You can only use one print function with string format
- You can only use one loop in your code
- You are not allowed to store characters in a variable
- You are not allowed to import any module
```bash
$ ./3-print_alphabt.py
abcdfghijklmnoprstuvwxyz$
```
### 4. Hexadecimal printing
Write a program that prints all numbers from ``0`` to ``98`` in decimal and in hexadecimal (as in the following example)
- You can only use one ``print`` function with string format
- You can only use one loop in your code
- You are not allowed to store numbers or strings in a variable
- You are not allowed to import any module
```bash
$ ./4-print_hexa.py
0 = 0x0
1 = 0x1
2 = 0x2
3 = 0x3
4 = 0x4
5 = 0x5
6 = 0x6
7 = 0x7
8 = 0x8
9 = 0x9
10 = 0xa
11 = 0xb
12 = 0xc
13 = 0xd
14 = 0xe
15 = 0xf
16 = 0x10
17 = 0x11
18 = 0x12
...
96 = 0x60
97 = 0x61
98 = 0x62
```
### 5. 00...99
Write a program that prints numbers from ``0`` to ``99``.
- Numbers must be separated by ``,``, followed by a space
- Numbers should be printed in ascending order, with two digits
- The last number should be followed by a new line
- You can only use no more than 2 ``print`` functions with string format
- You can only use one loop in your code
- You are not allowed to store numbers or strings in a variable
- You are not allowed to import any module
```bash
$ ./5-print_comb2.py
00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99
```
### 6. Inventing is a combination of brains and materials. The more brains you use, the less material you need
Write a program that prints all possible different combinations of two digits.
- Numbers must be separated by ``,``, followed by a space
- The two digits must be different
- ``01`` and ``10`` are considered the same combination of the two digits ``0`` and ``1``
- Print only the smallest combination of two digits
- Numbers should be printed in ascending order, with two digits
- The last number should be followed by a new line
- You can only use no more than 3 ``print`` functions with string format
- You can only use no more than 2 loops in your code
- You are not allowed to store numbers or strings in a variable
- You are not allowed to import any module
```bash
$ ./6-print_comb3.py
01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89
```
### 7. islower
Write a function that checks for lowercase character.
**Prototype:** ``def islower(c):``
- Returns ``True`` if `c` is lowercase
- Returns ``False`` otherwise
- You are not allowed to import any module
- You are not allowed to use ``str.upper()`` and ``str.isupper()``
- [Tips: ord()](https://docs.python.org/3.4/library/functions.html?highlight=ord#ord)
```bash
$ cat 7-main.py
#!/usr/bin/env python3
islower = __import__('7-islower').islower

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))

$ ./7-main.py
a is lower
H is upper
A is upper
3 is upper
g is lower
```
### 8. To uppercase
Write a function that prints a string in uppercase followed by a new line.
**Prototype:** ``def uppercase(str):``
- You can only use no more than 2 ``print`` functions with string format
- You can only use one loop in your code
- You are not allowed to import any module
- You are not allowed to use ``str.upper()`` and ``str.isupper()``
- [Tips: ord()](https://docs.python.org/3.4/library/functions.html?highlight=ord#ord)
```bash
$ cat 8-main.py
#!/usr/bin/env python3
uppercase = __import__('8-uppercase').uppercase

uppercase("best")
uppercase("Best School 98 Battery street")

$ ./8-main.py
BEST
BEST SCHOOL 98 BATTERY STREET
```
### 9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important
Write a function that prints the last digit of a number.
**Prototype:** ``def print_last_digit(number):``
- Returns the value of the last digit
- You are not allowed to import any module
```bash
$ cat 9-main.py
#!/usr/bin/env python3
print_last_digit = __import__('9-print_last_digit').print_last_digit

print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)

$ ./9-main.py
8044
```
### 10. a + b
Write a function that adds two integers and returns the result.
**Prototype:** ``def add(a, b):``
- Returns the value of ``a + b``
- You are not allowed to import any module
```bash
$ cat 10-main.py
#!/usr/bin/env python3
add = __import__('10-add').add

print(add(1, 2))
print(add(98, 0))
print(add(100, -2))

$ ./10-main.py
3
98
98
```
### 11. a ^ b
Write a function that computes a to the power of b and return the value.
**Prototype:** ``def pow(a, b):``
- Returns the value of ``a ^ b``
- You are not allowed to import any module
```bash
$ cat 11-main.py
#!/usr/bin/env python3
pow = __import__('11-pow').pow

print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))

$ ./11-main.py
4
9604
1
0.0001
-1024
```
### 12. Fizz Buzz
Write a function that prints the numbers from 1 to 100 separated by a space.
- For multiples of three print ``Fizz`` instead of the number and for multiples of five print ``Buzz``.
For numbers which are multiples of both three and five print ``FizzBuzz``.
- **Prototype:** ``def fizzbuzz():``
- Each element should be followed by a space
- You are not allowed to import any module
```bash
$ cat 12-main.py
#!/usr/bin/env python3
fizzbuzz = __import__('12-fizzbuzz').fizzbuzz

fizzbuzz()
print("")

$ ./12-main.py | cat -e
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 56 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 FizzBuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 86 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz $
```
### 13. Insert in sorted linked list
**Technical interview preparation:**
You are not allowed to google anything
Whiteboard first
Write a function in C that inserts a number into a sorted singly linked list.
- **Prototype:** ``listint_t *insert_node(listint_t **head, int number);``
- Return: the address of the new node, or ``NULL`` if it failed
```bash
carrie@ubuntu:0x01$ cat lists.h 
#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 *
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

listint_t *insert_node(listint_t **head, int number);

#endif /* LISTS_H */
carrie@ubuntu:0x01$ cat linked_lists.c 
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* number of nodes */

    current = h;
    n = 0;
    while (current != NULL)
    {
        printf("%i\n", current->n);
        current = current->next;
        n++;
    }

    return (n);
}

/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *new;
    listint_t *current;

    current = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = NULL;

    if (*head == NULL)
        *head = new;
    else
    {
        while (current->next != NULL)
            current = current->next;
        current->next = new;
    }

    return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
        current = head;
        head = head->next;
        free(current);
    }
}
carrie@ubuntu:0x01$ cat 13-main.c 
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - check the code for
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;

    head = NULL;
    add_nodeint_end(&head, 0);
    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 2);
    add_nodeint_end(&head, 3);
    add_nodeint_end(&head, 4);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 402);
    add_nodeint_end(&head, 1024);
    print_listint(head);

    printf("-----------------\n");

    insert_node(&head, 27);

    print_listint(head);

    free_listint(head);

    return (0);
}
carrie@ubuntu:0x01$ gcc -Wall -Werror -Wextra -pedantic -std=gnu89 13-main.c linked_lists.c 13-insert_number.c -o insert
carrie@ubuntu:0x01$ ./insert
0
1
2
3
4
98
402
1024
-----------------
0
1
2
3
4
27
98
402
1024
```
### 14. Smile in the mirror
Write a program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (``z`` in lowercase and ``Y`` in uppercase) , not followed by a new line.
- You can only use one ``print`` function with string format
- You can only use one loop in your code
- You are not allowed to store characters in a variable
- You are not allowed to import any module
```bash
$ ./100-print_tebahpla.py
zYxWvUtSrQpOnMlKjIhGfEdCbA$
```
### 15. Remove at position
Write a function that creates a copy of the string, removing the character at the position n (not the Python way, the “C array index”).
**Prototype:** ``def remove_char_at(str, n):``
- You are not allowed to import any module
```bash
$ cat 101-main.py
#!/usr/bin/env python3
remove_char_at = __import__('101-remove_char_at').remove_char_at

print(remove_char_at("Best School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))

$ ./101-main.py
Bes School
Chcago
 is fun!
School
Python
```
### 16. ByteCode -> Python #2
Write the Python function ``def magic_calculation(a, b, c):`` that does exactly the same as the following Python bytecode:
```

  3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
```
[tips - ByteCode](https://docs.python.org/3.4/library/dis.html)
