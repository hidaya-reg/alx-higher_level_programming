# 0x00. Python - Hello, World
## Resources
[The Python tutorial](https://docs.python.org/3/tutorial/index.html) (only the first three chapters below)
[Whetting Your Appetite](https://docs.python.org/3/tutorial/appetite.html)
[Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html)
[An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html) (Read up until “3.1.2. Strings” included)
[How To Use String Formatters in Python 3](https://realpython.com/python-f-strings/)
[Learn to Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
[Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)

## Learning Objectives
<details>
<summary>Why Python programming is awesome</summary>

### Python progarmming is awesome

| **Feature**               | **Why It's Awesome**                                                                 |
|---------------------------|---------------------------------------------------------------------------------------|
| **Easy to Learn**          | Simple syntax and readability make Python accessible for beginners and experts alike. |
| **Highly Readable**        | Code is clear and concise, enhancing maintainability and collaboration.               |
| **Versatile**              | Suitable for web development, data analysis, automation, AI, and more.                |
| **Rapid Development**      | Quick to write and test due to its interpreted nature—no compilation required.        |
| **Extensive Libraries**    | Comes with a vast collection of libraries for various tasks (e.g., file I/O, GUIs).   |
| **Cross-Platform**         | Runs on Windows, macOS, and Unix-based systems without modification.                  |
| **Automation**             | Great for automating repetitive tasks, from file management to web scraping.          |
| **Extensible**             | Can integrate with C/C++ for performance-critical tasks or use third-party libraries. |
| **Large Community**        | A strong community provides support, tutorials, and a rich ecosystem of tools.        |

</details>
<details>
<summary>Who is Guido van Rossum</summary>

### Who is Guido van Rossum
Python was created by Guido van Rossum in the late 1980s. He started working on it in December 1989 while at the Centrum Wiskunde & Informatica (CWI) in the Netherlands. Python was first released publicly in February 1991. Van Rossum created Python as a successor to the ABC programming language, with a focus on making it easy to learn and use while being powerful enough for real-world tasks.
-  "Python" comes from the British comedy show **"Monty Python's Flying Circus"**, not from the snake. Guido van Rossum, the creator of Python, chose the name because he was a fan of the show and wanted a name that was short, unique, and a bit playful.
</details>
<details>
<summary>What is the Zen of Python</summary>

### Zen of Python
The **Zen of Python** is a collection of guiding principles for writing computer programs in Python. It emphasizes simplicity, readability, and the beauty of clear code. Some key points include: "Beautiful is better than ugly," "Simple is better than complex," and "Readability counts." You can view the full Zen by running ``import this`` in a Python interpreter.
</details>
<details>
<summary>How to use the Python interpreter</summary>

### Python interpreter
To use the Python interpreter on Unix-based systems
**1. Ensure Python is Installed:** ``python --version`` or ``python3 --version``

- If Python isn't installed, you can install it using your package manager (e.g., ``sudo apt install python3`` on Ubuntu).

**2. Start the Python Interpreter:** Type ``python`` or ``python3``  and press Enter
You should see the Python version and the ``>>>`` prompt, indicating the interpreter is ready.

**3. Run Python Code:**
You can now type Python code and see the results instantly. For example:
```python
Copy code
>>> print("Hello, Unix!")
Hello, Unix!
```
**4. Exit the Interpreter:** To exit, type ``exit()`` or press ``Ctrl+D``.
</details>
<details>
<summary>How to print text and variables using print</summary>

### Print text and variables using print
#### 1. Basic Printing:
Simply pass text or variables to print():
```python
name = "Alice"
age = 25
print("Name:", name)  # Output: Name: Alice
print("Age:", age)    # Output: Age: 25
```
#### 2. Using String Concatenation:
You can concatenate strings and variables using the ``+`` operator:
```python
print("Name: " + name + ", Age: " + str(age))  # Output: Name: Alice, Age: 25
```
#### 3. Using f-strings (Formatted Strings): (Python 3.6+)
This is the most readable and recommended method:
```python
print(f"Name: {name}, Age: {age}")  # Output: Name: Alice, Age: 25
```
#### 4. Using format() Method:
Another way to format strings:
```python
print("Name: {}, Age: {}".format(name, age))  # Output: Name: Alice, Age: 25
```
#### 5. Multiple Arguments in print():
You can pass multiple arguments to print() and it will automatically add spaces between them:
```python
print("Name:", name, "Age:", age)  # Output: Name: Alice Age: 25
```
</details>
<details>
<summary>How to use strings</summary>

### Strings
#### 1. Creating Strings:
```python
single_quoted = 'Hello, World!'
double_quoted = "Hello, World!"
triple_quoted = '''This is a multi-line string
that spans multiple lines.'''
```
#### 2. Accessing Characters:
You can access individual characters in a string using indexing (0-based):
```python
greeting = "Hello"
first_char = greeting[0]  # 'H'
last_char = greeting[-1]  # 'o'
```
#### 3. String Length:
Use the ``len()`` function to find the length of a string: `length = len(greeting)  # 5`

#### 4. String Concatenation:
Combine strings using the ``+`` operator:
```python
full_greeting = greeting + " there!"  # 'Hello there!'
```
#### 5. String Repetition:
Repeat strings using the ``*`` operator:
```python
echo = "Hello! " * 3  # 'Hello! Hello! Hello! '
```
#### 6. String Methods:
Python provides many built-in string methods. Here are a few useful ones:
- ``greeting.lower()  # 'hello'``
- ``greeting.upper()  # 'HELLO'``
- ``text = "   Hello, World!   "
    text.strip()  # 'Hello, World!'``
- ``str.split()``: Splits a string into a list based on a delimiter.
```python
sentence = "Hello, World!"
words = sentence.split(", ")  # ['Hello', 'World!']
```
- ``str.join()``: Joins a list of strings into a single string.
```python
words = ['Hello', 'World']
joined = " ".join(words)  # 'Hello World'
```
- ``str.replace(old, new)``: Replaces occurrences of a substring.
```python
text = "Hello, World!"
text.replace("World", "Python")  # 'Hello, Python!'
```
#### 7. String Formatting:
You can format strings using f-strings, ``format()``, or the ``%``operator.
- ``F-strings`` (Python 3.6+):
```python
name = "Alice"
age = 30
formatted = f"{name} is {age} years old."  # 'Alice is 30 years old.'
```
- Using ``format()``:
```python
formatted = "{} is {} years old.".format(name, age)  # 'Alice is 30 years old.'
```
- Using % operator:
```python
formatted = "%s is %d years old." % (name, age)  # 'Alice is 30 years old.'
```
#### 8. Escape Characters:
Use backslashes (``\``) to escape special characters: `escaped_string = "He said, \"Hello!\""`

</details>
<details>
<summary>What is the official Python coding style and how to check your code with pycodestyle</summary>

| **Aspect**                  | **Details**                                                                                                                                                     |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Official Style Guide**    | **PEP 8** (Python Enhancement Proposal 8)                                                                                                                   |
| **Key Points of PEP 8**     | - **Code Layout**: Use 4 spaces per indentation level; limit lines to 79 characters; use blank lines to separate functions and classes.                      |
|                             | - **Imports**: Import modules at the top of the file; use absolute imports rather than relative ones.                                                          |
|                             | - **Whitespace**: Avoid extraneous whitespace in expressions and statements; use a single space around operators and after commas.                          |
|                             | - **Comments**: Use comments to explain code; block comments apply to whole sections and should be indented to the same level as that code.                  |
|                             | - **Naming Conventions**: Use lowercase with underscores for functions and variable names (e.g., `my_function`); use CapitalizedWords for class names (e.g., `MyClass`); use ALL_CAPS for constants (e.g., `MAX_SIZE`). |
|                             | - **Programming Recommendations**: Write clear and readable code; prefer `is` and `is not` for comparing with `None`; use `str.format()` or f-strings for string formatting. |
| **Checking Code with `pycodestyle`** | **Installation**: Install `pycodestyle` using pip: <br> `pip install pycodestyle`                                                                  |
|                             | **Run on Single File**: Check a Python file (e.g., `script.py`): <br> `pycodestyle script.py`                                                                |
|                             | **Run on Multiple Files**: Check all Python files in the current directory: <br> `pycodestyle *.py` <br> Check all Python files in a directory: <br> `pycodestyle directory_name/` |
|                             | **Output**: Displays style violations with line number and description (e.g., `script.py:1:1: E302 expected 2 blank lines, found 1`).                      |
|                             | **Configuration**: Create a `.pep8` or `setup.cfg` file to customize `pycodestyle` behavior (e.g., ignore certain rules or set maximum line length).      |

</details>

## Zen
```
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```
## Tasks
### 0. Run Python file
Write a Shell script that runs a Python script.
The Python file name will be saved in the environment variable ``$PYFILE``
```bash
$ cat main.py 
#!/usr/bin/python3
print("Best School")

$ export PYFILE=main.py
$ ./0-run
Best School
```
### 1. Run inline
Write a Shell script that runs Python code.
The Python code will be saved in the environment variable ``$PYCODE``
```bash
$ export PYCODE='print(f"Best School: {88+10}")'
$ ./1-run_inline 
Best School: 98
```
### 2. Hello, print
Write a Python script that prints exactly ``"Programming is like building a multilingual puzzle``, followed by a new line.
Use the function ``print``
```bash
$ ./2-print.py 
"Programming is like building a multilingual puzzle
```
### 3. Print integer
Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py) in order to print the integer stored in the variable ``number``, followed by ``Battery street``, followed by a new line.
- The output of the script should be:
    + the number, followed by ``Battery street``,
    + followed by a new line
- You are not allowed to cast the variable ``number`` into a string
- Your code must be 3 lines long
- You have to use f-strings [tips](https://realpython.com/python-f-strings/)
```bash
$ ./3-print_number.py
98 Battery street
```  
### 4. Print float
Complete the source code in order to print the float stored in the variable ``number`` with a precision of 2 digits.
- You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/4-print_float.py)
- The output of the program should be:
    + ``Float``:, followed by the float with only 2 digits
    + followed by a new line
- You are not allowed to cast ``number`` to string
- You have to use f-strings
```bash
$ ./4-print_float.py
Float: 3.14
```
### 5. Print string
Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/5-print_string.py) in order to print 3 times a string stored in the variable ``str``, followed by its first 9 characters.
- The output of the program should be:
    + 3 times the value of ``str``
    + followed by a new line
    + followed by the 9 first characters of ``str``
    + followed by a new line
- You are not allowed to use any loops or conditional statement
- Your program should be maximum 5 lines long
```bash
$ ./5-print_string.py 
Holberton SchoolHolberton SchoolHolberton School
Holberton
```
### 6. Play with strings
Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/6-concat.py) to print Welcome to Holberton School!
- You are not allowed to use any loops or conditional statements.
- You have to use the variables ``str1`` and ``str2`` in your new line of code
- Your program should be exactly 5 lines long
```bash
$ ./6-concat.py
Welcome to Holberton School!
$ wc -l 6-concat.py
5 6-concat.py
```
### 7. Copy - Cut - Paste
Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/7-edges.py)
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 8 lines long
- ``word_first_3`` should contain the first 3 letters of the variable ``word``
- ``word_last_2`` should contain the last 2 letters of the variable ``word``
- ``middle_word`` should contain the value of the variable ``word`` without the first and last letters
```bash
$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
$ wc -l 7-edges.py
8 7-edges.py
```
### 8. Create a new sentence
Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/8-concat_edges.py) to print ``object-oriented programming with Python``, followed by a new line.
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 5 lines long
- You are not allowed to create new variables
- You are not allowed to use string literals
```bash
$ ./8-concat_edges.py
object-oriented programming with Python
$ wc -l 8-concat_edges.py
5 8-concat_edges.py
```
### 9. Easter Egg
Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.
Your script should be maximum 98 characters long (please check with ``wc -m 9-easter_egg.py``)
```bash
$ ./9-easter_egg.py
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```
### 10. Linked list cycle
**Technical interview preparation:**
- You are not allowed to google anything
- Whiteboard first
- This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution’s runtime fast enough, does your solution require extra memory usage / mallocs, etc.

Write a function in C that checks if a singly linked list has a cycle in it.
**Prototype:** ``int check_cycle(listint_t *list);``
- Return: ``0`` if there is no cycle, ``1`` if there is a cycle
Requirements: Only these functions are allowed: ``write``, ``printf``, ``putchar``, ``puts``, ``malloc``, ``free``
```bash
$ cat lists.h
#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

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
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
$ cat 10-linked_lists.c
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
 * add_nodeint - adds a new node at the beginning of a listint_t list
 * @head: pointer to a pointer of the start of the list
 * @n: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
    listint_t *new;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = *head;
    *head = new;

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
```
```bash
$ cat 10-main.c
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * main - check the code
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;
    listint_t *current;
    listint_t *temp;
    int i;

    head = NULL;
    add_nodeint(&head, 0);
    add_nodeint(&head, 1);
    add_nodeint(&head, 2);
    add_nodeint(&head, 3);
    add_nodeint(&head, 4);
    add_nodeint(&head, 98);
    add_nodeint(&head, 402);
    add_nodeint(&head, 1024);
    print_listint(head);

    if (check_cycle(head) == 0)
        printf("Linked list has no cycle\n");
    else if (check_cycle(head) == 1)
        printf("Linked list has a cycle\n");

    current = head;
    for (i = 0; i < 4; i++)
        current = current->next;
    temp = current->next;
    current->next = head;

    if (check_cycle(head) == 0)
        printf("Linked list has no cycle\n");
    else if (check_cycle(head) == 1)
        printf("Linked list has a cycle\n");

    current = head;
    for (i = 0; i < 4; i++)
        current = current->next;
    current->next = temp;

    free_listint(head);

    return (0);
}
```
```bash
$ gcc -Wall -Werror -Wextra -pedantic -std=gnu89 10-main.c 10-check_cycle.c 10-linked_lists.c -o cycle
$ ./cycle 
1024
402
98
4
3
2
1
0
Linked list has no cycle
Linked list has a cycle
```
Solving a problem is already a big win! but finding the best and optimal way to solve it, it’s way better! Think about the most optimal / fastest way to do it.
### 11. Hello, write
Write a Python script that prints exactly ``and that piece of art is useful - Dora Korpar, 2015-10-19``, followed by a new line.
- Use the function ``write`` from the ``sys`` module
- You are not allowed to use ``print``
- Your script should print to ``stderr``
- Your script should exit with the status code ``1``
```bash
$ ./100-write.py
and that piece of art is useful - Dora Korpar, 2015-10-19
$ echo $?
1
$ ./100-write.py 2> q
$ cat q
and that piece of art is useful - Dora Korpar, 2015-10-19
```
### 12. Compile
Write a script that compiles a Python script file.

The Python file name will be stored in the environment variable ``$PYFILE``

The output filename has to be ``$PYFILEc`` (ex: ``export PYFILE=my_main.py`` => output filename: ``my_main.pyc``)
```bash
$ cat main.py 
#!/usr/bin/python3
print("Best School")

$ export PYFILE=main.py
$ ./101-compile
Compiling main.py ...
$ ls
101-compile  main.py  main.pyc
$ cat main.pyc | zgrep -c "Best School"
1
$ od -t x1 main.pyc # SYSTEM DEPENDANT => CAN BE DIFFERENT
0000000 ee 0c 0d 0a 91 26 3e 58 31 00 00 00 e3 00 00 00
0000020 00 00 00 00 00 00 00 00 00 02 00 00 00 40 00 00
0000040 00 73 0e 00 00 00 65 00 00 64 00 00 83 01 00 01
0000060 64 01 00 53 29 02 7a 10 48 6f 6c 62 65 72 74 6f
0000100 6e 20 53 63 68 6f 6f 6c 4e 29 01 da 05 70 72 69
0000120 6e 74 a9 00 72 02 00 00 00 72 02 00 00 00 fa 07
0000140 6d 61 69 6e 2e 70 79 da 08 3c 6d 6f 64 75 6c 65
0000160 3e 02 00 00 00 73 00 00 00 00
0000172
```
### 13. ByteCode -> Python #1
Write the Python function ``def magic_calculation(a, b):`` that does exactly the same as the following Python bytecode:

```
  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
```
Tip: [Python bytecode](https://docs.python.org/3.4/library/dis.html)