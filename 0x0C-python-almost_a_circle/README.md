# 0x0C. Python - Almost a circle
## Resources
- [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
- [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
- [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)
## Learning Objectives
<details>
<summary>What is Unit testing and how to implement it in a large project</summary>

### Unit testing
Unit testing is a software testing technique where individual components or functions of a program are tested in isolation to ensure that they work correctly. The primary goal of unit testing is to validate each part of the codebase independently, ensuring that it performs as expected and meets its specifications. This helps catch bugs early in the development process, making it easier to maintain and refactor code.

#### Key Concepts of Unit Testing
**1. Isolation:** Each unit test should test a single "unit" of code (e.g., a function or method) in isolation from other parts of the system. This often involves using mock objects or stubs to simulate dependencies.
**2. Automated Testing:** Unit tests should be automated to facilitate continuous testing. This allows developers to run tests frequently and consistently.
**3. Test Cases:** Each test should cover a specific scenario, including normal cases, edge cases, and error conditions.
**4. Frameworks:**Popular frameworks include ``unittest``, ``pytest``, and ``nose``.

#### Implementing Unit Testing in a Large Project
**1. Choose a Testing Framework:** Select a unit testing framework that suits your programming language and project needs. For Python, unittest and pytest are popular choices.
**2. Organize Your Tests:**
- Create a dedicated directory for tests, often named ``tests``.
- Structure the tests to mirror the project structure, allowing for easier navigation and understanding.
Example structure:
```
my_project/
├── src/
│   ├── module1.py
│   └── module2.py
└── tests/
    ├── test_module1.py
    └── test_module2.py
```
**3. Write Test Cases:**
- For each unit of code (e.g., function or method), write one or more test cases.
- Use assertions to check expected outcomes against actual results.

Example using ``unittest``:
```python
import unittest
from src.module1 import my_function

class TestMyFunction(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(my_function(1, 2), 3)

    def test_case_2(self):
        self.assertRaises(ValueError, my_function, -1, 5)

if __name__ == '__main__':
    unittest.main()
```
**4. Mock External Dependencies:** For functions that interact with external systems (like databases or APIs), use mocking to simulate these interactions. This helps to isolate the unit being tested.
Example using ``unittest.mock``:
```python
from unittest import mock

@mock.patch('module1.external_dependency')
def test_case_with_mock(self, mock_dependency):
    mock_dependency.return_value = "mocked value"
    result = my_function()
    self.assertEqual(result, expected_value)
```
**5. Run Tests Regularly:**
- Integrate unit testing into your development workflow. Run tests frequently, especially after making changes to the codebase.
- Use Continuous Integration (CI) tools to automate running tests on new commits or pull requests.

**6. Maintain Tests:**
- Keep tests up-to-date with changes to the codebase. As the application evolves, the corresponding tests should also be updated.
- Refactor tests when necessary to improve readability and maintainability.

**7. Measure Code Coverage:** Use tools to measure code coverage and ensure that a significant portion of your codebase is covered by tests. Aim for a reasonable coverage percentage, but understand that 100% coverage does not guarantee that the code is bug-free.

**Example with ``pytest``**
```python
# src/calculator.py
def add(a, b):
    return a + b

# tests/test_calculator.py
import pytest
from src.calculator import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

if __name__ == "__main__":
    pytest.main()
```
You can run the tests by executing pytest in your terminal.
</details>
<details>
<summary>How to serialize and deserialize a Class</summary>

### Serialize and Deserialize a Class

Serialization is the process of converting a Python object into a format that can be easily stored or transmitted, and deserialization is the reverse process of converting the serialized format back into a Python object. In Python, the most common way to perform serialization is by using the ``pickle`` module or the ``json`` module, depending on the use case.

#### Using the ``pickle`` Module
The ``pickle`` module can serialize and deserialize Python objects, including complex objects like classes.

##### Example: Serializing and Deserializing with ``pickle``
**1. Define a Class:**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"
```
**2. Serialize the Object:**
```python
import pickle

person = Person("Alice", 30)

# Serialize
with open("person.pkl", "wb") as file:
    pickle.dump(person, file)
```
**3. Deserialize the Object:**
```python
# Deserialize
with open("person.pkl", "rb") as file:
    loaded_person = pickle.load(file)

print(loaded_person)  # Output: Person(name=Alice, age=30)
```
#### Using the ``json`` Module
The ``json`` module can also be used for serialization, but it can only handle basic data types (like dictionaries, lists, strings, numbers, etc.). To serialize a custom class, you need to provide a method to convert the object to a serializable format, typically a dictionary. You can also create a custom deserialization function.

##### Example: Serializing and Deserializing with ``json``
**1. Define a Class with ``to_dict`` and ``from_dict`` Methods:**
```python
import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_dict(self):
        return {"name": self.name, "age": self.age}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["age"])

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"
```
**2. Serialize the Object:**
```python
person = Person("Alice", 30)

# Serialize
person_json = json.dumps(person.to_dict())
with open("person.json", "w") as file:
    file.write(person_json)
```
**3. Deserialize the Object:**
```python
# Deserialize
with open("person.json", "r") as file:
    loaded_person_data = json.load(file)

loaded_person = Person.from_dict(loaded_person_data)
print(loaded_person)  # Output: Person(name=Alice, age=30)
```
#### Summary
- Serialization: Use ``pickle`` for complex objects, including instances of classes. Use ``json`` for simpler, standard data types, and provide methods to convert custom objects.
- Deserialization: Load the serialized data back into the original object format using the respective load methods.
</details>
<details>
<summary>What is ``*args`` and how to use it</summary>

### `*args`

In Python, ``*args`` is a special syntax used in function definitions to allow the function to accept a variable number of positional arguments. The ``*`` operator collects any excess positional arguments as a tuple. This can be particularly useful when you're not sure how many arguments will be passed to the function.

**1. Defining a Function with ``*args``:** You can define a function that accepts any number of positional arguments by using ``*args``.
```python
def my_function(*args):
    for arg in args:
        print(arg)
```
``2. Calling the Function``: You can call the function with as many positional arguments as you like.
```python
my_function(1, 2, 3)       # Output: 1, 2, 3
my_function('apple', 'banana', 'cherry')  # Output: apple, banana, cherry
```
**3. Combining with Other Parameters:** You can combine ``*args`` with regular parameters and keyword arguments.
```python
def greet(greeting, *args):
    for name in args:
        print(f"{greeting}, {name}!")

greet("Hello", "Alice", "Bob", "Charlie")
# Output:
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!
```
**4. Accessing the Arguments:** Inside the function, ``args`` behaves like a tuple, so you can access elements using indexing or iteration.
```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))  # Output: 10
```
#### Example Use Cases
- Dynamic Functions: When creating functions that need to handle a varying number of inputs, such as logging functions or mathematical operations.
- Wrapper Functions: When creating decorators that need to pass arguments to the original function.

#### Important Notes
- You can use any name in place of ``args``, but it’s a convention to use ``*args`` for readability. If you want to capture keyword arguments, you would use ``**kwargs``.
- ``*args`` can only appear once in a function definition. If it appears more than once, you'll get a syntax error.
</details>
<details>
<summary>What is ``**kwargs`` and how to use it</summary>

### ``**kwargs``

In Python, ``**kwargs`` is a special syntax used in function definitions to allow the function to accept a variable number of keyword arguments. The ``**`` operator collects these keyword arguments as a dictionary, where the keys are the argument names and the values are the argument values. This is particularly useful when you want to handle named parameters dynamically.

#### How to Use ``**kwargs``
**1. Defining a Function with ``**kwargs:``** You can define a function that accepts any number of keyword arguments by using ``**kwargs``.
```python
def my_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```
**2. Calling the Function:** You can call the function with as many keyword arguments as you like.
```python
my_function(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York
```
**3. Combining with Other Parameters:** You can combine ``**kwargs`` with regular parameters and ``*args``.
```python
def describe_person(name, **kwargs):
    print(f"Name: {name}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe_person("Alice", age=30, city="New York")
# Output:
# Name: Alice
# age: 30
# city: New York
```
**4. Accessing the Arguments:** Inside the function, ``kwargs`` behaves like a dictionary, so you can access elements using keys or iterate through the items.
```python
def print_info(**kwargs):
    if 'name' in kwargs:
        print(f"Name: {kwargs['name']}")
    else:
        print("Name not provided")

print_info(name="Bob")  # Output: Name: Bob
print_info()            # Output: Name not provided
```
#### Example Use Cases
- Dynamic Functions: When creating functions that need to handle a varying number of named parameters, such as configuration functions or API calls.
- Wrapper Functions: When creating decorators that need to pass keyword arguments to the original function.

#### Important Notes
- You can use any name in place of kwargs, but it’s a convention to use ``**kwargs`` for readability. If you want to capture positional arguments, you would use ``*args``.
- ``**kwargs`` can only appear once in a function definition. If it appears more than once, you'll get a syntax error.
</details>
<details>
<summary>How to handle named arguments in a function</summary>

### Named arguments in a function

Handling named arguments in a function in Python can be done using various methods, including regular positional arguments, keyword arguments, and the special syntaxes `*args` and `**kwargs`.
#### 1. Using Regular Keyword Arguments
You can define a function with specific named arguments:
```python
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# Calling the function with named arguments
greet(name="Alice", age=30)
```
#### 2. Using Default Values
You can set default values for your named arguments, making them optional:
```python
def greet(name, age=25):
    print(f"Hello, {name}! You are {age} years old.")

# Calling the function
greet("Alice")          # Uses default age
greet("Bob", age=40)    # Overrides default age
```
#### 3. Using ``*args`` and ``**kwargs``
If you want to handle a variable number of positional and named arguments, you can use ``*args`` for positional arguments and ``**kwargs`` for keyword arguments.
```python
def describe_person(name, *args, **kwargs):
    print(f"Name: {name}")
    print("Other info:")
    for arg in args:
        print(f"- {arg}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function with various arguments
describe_person("Alice", "Engineer", "New York", age=30, city="New York")
```
#### 4. Combining Positional, Default, and Keyword Arguments
You can combine positional arguments, default values, and keyword arguments in a single function:
```python
def register_user(username, password, email, is_active=True, **kwargs):
    print(f"User: {username}, Email: {email}, Active: {is_active}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function
register_user("alice", "pass123", "alice@example.com", age=30, location="USA")
```
#### 5. Keyword-Only Arguments
You can specify that certain arguments must be passed as keywords by placing them after a ``*`` in the function definition:
```python
def create_user(username, password, *, age, email):
    print(f"Creating user: {username}, Email: {email}, Age: {age}")

# Calling the function
create_user("alice", "pass123", age=30, email="alice@example.com")
# create_user("bob", "pass456", 25, "bob@example.com")  # This would raise an error
```
</details>
<details>
<summary>``__init__.py`` file</summary>

### ``__init__.py`` file
The ``__init__.py`` file can be very versatile and serves different purposes depending on the needs of the package. Let's explore several use cases with practical examples:
#### 1. Basic ``__init__.py`` as a Marker
In its simplest form, ``__init__.py`` is just an empty file that marks a directory as a Python package. This is all you need to allow importing modules from the directory.

**Structure:**
```markdown
mypackage/
    __init__.py
    module1.py
```
**Example:**
With this in place, you can import from the package:
```python
import mypackage.module1
```
#### 2. Defining Package-Wide Constants
You can use ``__init__.py`` to define package-wide variables, constants, or even basic configuration.
**Example:**
```python
# mypackage/__init__.py
PACKAGE_NAME = "mypackage"
VERSION = "1.0"
```
In your code:

```python
import mypackage
print(mypackage.PACKAGE_NAME)  # Output: "mypackage"
print(mypackage.VERSION)       # Output: "1.0"
```
#### 3. Package Initialization Code
You can place logic inside ``__init__.py`` that runs when the package is first imported. This is useful for setting up initial states, loading resources, or preparing something at package level.
**Example:**
```python
# mypackage/__init__.py
print("Initializing the package!")

def package_setup():
    print("Setting up the package!")

package_setup()
```
-> Output when the package is imported:
```bash
$ python
>>> import mypackage
Initializing the package!
Setting up the package!
```
#### 4. Importing Submodules into the Package Namespace
You can import certain submodules or specific objects (classes, functions, etc.) into the package namespace, making them directly available when you import the package.

**Structure:**
```markdown
mypackage/
    __init__.py
    module1.py
    module2.py
```
**Example:**
```python
# mypackage/__init__.py
from .module1 import MyClass
from .module2 import my_function
```

-> Now you can access ``MyClass`` and ``my_function`` directly when importing the package:
```python
from mypackage import MyClass, my_function

# Instead of:
from mypackage.module1 import MyClass
from mypackage.module2 import my_function
```
#### 5. Defining Public API with ``__all__``
You can control what gets imported when users do from mypackage import * by defining the ``__all__`` variable in ``__init__.py``. This is useful for defining the public API of your package.

**Example:**
```python
# mypackage/__init__.py
__all__ = ['module1', 'MyClass']
```
Now, when users do ``from mypackage import *``, only the members specified in ``__all__`` will be imported.

#### 6. Aggregating Multiple Submodules
If a package consists of several modules that need to work together, you can use ``__init__.py`` to bring them under a unified interface.

**Structure:**
```markdown
mypackage/
    __init__.py
    db.py
    utils.py
```
**Example:**
```python
# mypackage/__init__.py
from .db import Database
from .utils import helper_function
```
By doing this, users can access ``Database`` and ``helper_function`` directly through mypackage:
```python
from mypackage import Database, helper_function
```
#### 7. Conditional Logic in ``__init__.py``
You can also have conditional logic to modify the package behavior based on some conditions.

**Example:**

```python
# mypackage/__init__.py
import sys

if sys.version_info < (3, 8):
    print("Warning: Python 3.8 or higher is required!")
```
This could print a warning if someone is using a lower version of Python.

#### 8. Dynamic Package Creation or Importing External Modules
In more advanced cases, you can dynamically generate package members, import third-party modules, or handle configuration dynamically.

**Example:**
```python
# mypackage/__init__.py
import os

# Dynamically add module based on environment
if os.getenv("ENV") == "development":
    from .dev_module import *
else:
    from .prod_module import *
```
This allows you to load different modules based on the environment (for example, development vs. production).

#### 9. Creating Namespaces with ``__init__.py``
In some cases, you can use ``__init__.py`` to create namespaces for shared functionality between different sub-packages.

**Structure:**
```markdown
mypackage/
    __init__.py
    subpackage1/
        __init__.py
        module1.py
    subpackage2/
        __init__.py
        module2.py
```
**Example in mypackage/``__init__.py``:**
```python
from .subpackage1.module1 import function1
from .subpackage2.module2 import function2
```
Users can now access functions from both sub-packages directly from ``mypackage``:
```python
from mypackage import function1, function2
```
#### 10. Empty ``__init__.py`` in Modern Python (Optional)
Since Python 3.3, the ``__init__.py`` file is no longer strictly required for marking a directory as a package (due to the introduction of implicit namespaces). However, having an empty ``__init__.py`` is still common for backward compatibility and clarity.

**Example:**
```bash
# mypackage/__init__.py (empty)
```
</details>

## Tasks
### 0. If it's not tested it doesn't work
All your files, classes and methods must be unit tested and be PEP 8 validated.
```bash
$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
```
*Note that this is just an example. The number of tests you create can be different from the above example.*

### 1. Base class
Write the first class ``Base``:
Create a folder named ``models`` with an empty file ``__init__.py`` inside - with this file, the folder will become a Python package
Create a file named ``models/base.py``:
- Class ``Base``:
    + private class attribute ``__nb_objects = 0``
    + class constructor: ``def __init__(self, id=None):``:
        - if ``id`` is not ``None``, assign the public instance attribute ``id`` with this argument value - you can assume ``id`` is an integer and you don’t need to test the type of it
        - otherwise, increment ``__nb_objects`` and assign the new value to the public instance attribute ``id``
This class will be the “base” of all other classes in this project. The goal of it is to manage ``id`` attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)
```bash
$ cat 0-main.py
#!/usr/bin/python3
""" 0-main """
from models.base import Base

if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)

$ ./0-main.py
1
2
3
12
4
```
### 2. First Rectangle
Write the class ``Rectangle`` that inherits from ``Base``:
- In the file ``models/rectangle.py``
- Class ``Rectangle`` inherits from ``Base``
- Private instance attributes, each with its own public getter and setter:
    + ``__width`` -> ``width``
    + ``__height`` -> ``height``
    + ``__x`` -> ``x``
    + ``__y`` -> ``y``
- Class constructor: ``def __init__(self, width, height, x=0, y=0, id=None):``
    + Call the super class with ``id`` - this super call with use the logic of the ``__init__`` of the ``Base`` class
    + Assign each argument ``width``, ``height``, ``x`` and ``y`` to the right attribute
Why private attributes with getter/setter? Why not directly public attribute?
Because we want to protect attributes of our class. With a setter, you are able to validate what a developer is trying to assign to a variable. So after, in your class you can “trust” these attributes.
```bash
$ cat 1-main.py
#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)

$ ./1-main.py
1
2
12
```
### 3. Validate attributes
Update the class ``Rectangle`` by adding validation of all setter methods and instantiation (``id`` excluded):
- If the input is not an integer, raise the ``TypeError`` exception with the message: ``<name of the attribute> must be an integer``. Example: ``width must be an integer``
- If ``width`` or ``height`` is under or equals ``0``, raise the ``ValueError`` exception with the message: ``<name of the attribute> must be > 0``. Example: ``width must be > 0``
- If ``x`` or ``y`` is under ``0``, raise the ``ValueError`` exception with the message: ``<name of the attribute> must be >= 0``. Example: ``x must be >= 0``
```bash
$ cat 2-main.py
#!/usr/bin/python3
""" 2-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    try:
        Rectangle(10, "2")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.width = -10
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.x = {}
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        Rectangle(10, 2, 3, -1)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

$ ./2-main.py
[TypeError] height must be an integer
[ValueError] width must be > 0
[TypeError] x must be an integer
[ValueError] y must be >= 0
```
### 4. Area first
Update the class ``Rectangle`` by adding the public method ``def area(self):`` that returns the area value of the ``Rectangle`` instance.
```python
$ cat 3-main.py
#!/usr/bin/python3
""" 3-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(3, 2)
    print(r1.area())

    r2 = Rectangle(2, 10)
    print(r2.area())

    r3 = Rectangle(8, 7, 0, 0, 12)
    print(r3.area())

$ ./3-main.py
6
20
56
```
### 5. Display #0
Update the class ``Rectangle`` by adding the public method ``def display(self):`` that prints in stdout the Rectangle instance with the character ``#`` - you don’t need to handle ``x`` and ``y`` here.
```bash
$ cat 4-main.py
#!/usr/bin/python3
""" 4-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(4, 6)
    r1.display()

    print("---")

    r1 = Rectangle(2, 2)
    r1.display()

$ ./4-main.py
####
####
####
####
####
####
---
##
##
```
### 6. __str__
Update the class ``Rectangle`` by overriding the ``__str__`` method so that it returns ``[Rectangle] (<id>) <x>/<y> - <width>/<height>``
```bash
$ cat 5-main.py
#!/usr/bin/python3
""" 5-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(4, 6, 2, 1, 12)
    print(r1)

    r2 = Rectangle(5, 5, 1)
    print(r2)

$ ./5-main.py
[Rectangle] (12) 2/1 - 4/6
[Rectangle] (1) 1/0 - 5/5
```
### 7. Display #1
Update the class ``Rectangle`` by improving the public method ``def display(self):`` to print in stdout the ``Rectangle`` instance with the character ``#`` by taking care of ``x`` and ``y``
```bash
$ cat 6-main.py
#!/usr/bin/python3
""" 6-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(2, 3, 2, 2)
    r1.display()

    print("---")

    r2 = Rectangle(3, 2, 1, 0)
    r2.display()

$ ./6-main.py | cat -e
$
$
  ##$
  ##$
  ##$
---$
 ###$
 ###$
```
### 8. Update #0
Update the class ``Rectangle`` by adding the public method ``def update(self, *args):`` that assigns an argument to each attribute:
- 1st argument should be the ``id`` attribute
- 2nd argument should be the ``width`` attribute
- 3rd argument should be the ``height`` attribute
- 4th argument should be the ``x`` attribute
- 5th argument should be the ``y`` attribute
This type of argument is called a “no-keyword argument” - Argument order is super important.
```bash
$ cat 7-main.py
#!/usr/bin/python3
""" Doc """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(89)
    print(r1)

    r1.update(89, 2)
    print(r1)

    r1.update(89, 2, 3)
    print(r1)

    r1.update(89, 2, 3, 4)
    print(r1)

    r1.update(89, 2, 3, 4, 5)
    print(r1)

$ ./7-main.py
[Rectangle] (1) 10/10 - 10/10
[Rectangle] (89) 10/10 - 10/10
[Rectangle] (89) 10/10 - 2/10
[Rectangle] (89) 10/10 - 2/3
[Rectangle] (89) 4/10 - 2/3
[Rectangle] (89) 4/5 - 2/3
```
### 9. Update #1
Update the class ``Rectangle`` by updating the public method ``def update(self, *args):`` by changing the prototype to ``update(self, *args, **kwargs)`` that assigns a key/value argument to attributes:
- ``**kwargs`` can be thought of as a double pointer to a dictionary: key/value
    + As Python doesn’t have pointers, ``**kwargs`` is not literally a double pointer – describing it as such is just a way of explaining its behavior in terms you’re already familiar with
- ``**kwargs`` must be skipped if ``*args`` exists and is not empty
- Each key in this dictionary represents an attribute to the instance

This type of argument is called a “key-worded argument”. Argument order is not important.
```bash
$ cat 8-main.py
#!/usr/bin/python3
""" 8-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(height=1)
    print(r1)

    r1.update(width=1, x=2)
    print(r1)

    r1.update(y=1, width=2, x=3, id=89)
    print(r1)

    r1.update(x=1, height=2, y=3, width=4)
    print(r1)

$ ./8-main.py
[Rectangle] (1) 10/10 - 10/10
[Rectangle] (1) 10/10 - 10/1
[Rectangle] (1) 2/10 - 1/1
[Rectangle] (89) 3/1 - 2/1
[Rectangle] (89) 1/3 - 4/2
```
### 10. And now, the Square!
Write the class ``Square`` that inherits from ``Rectangle``:
- In the file ``models/square.py``
- Class ``Square`` inherits from ``Rectangle``
- Class constructor: ``def __init__(self, size, x=0, y=0, id=None):``:
    + Call the super class with ``id``, ``x``, ``y``, ``width`` and ``height`` - this super call will use the logic of the ``__init__`` of the ``Rectangle`` class. The ``width`` and ``height`` must be assigned to the value of ``size``
    + You must not create new attributes for this class, use all attributes of ``Rectangle`` - As reminder: a Square is a Rectangle with the same width and height
    + All ``width``, ``height``, ``x`` and ``y`` validation must inherit from ``Rectangle`` - same behavior in case of wrong data
- The overloading ``__str__`` method should return ``[Square] (<id>) <x>/<y> - <size>`` - in our case, ``width`` or ``height``

As you know, a Square is a special Rectangle, so it makes sense this class Square inherits from Rectangle. Now you have a Square class who has the same attributes and same methods.
```bash
$ cat 9-main.py
#!/usr/bin/python3
""" 9-main """
from models.square import Square

if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.area())
    s1.display()

    print("---")

    s2 = Square(2, 2)
    print(s2)
    print(s2.area())
    s2.display()

    print("---")

    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display()

$ ./9-main.py
[Square] (1) 0/0 - 5
25
#####
#####
#####
#####
#####
---
[Square] (2) 2/0 - 2
4
  ##
  ##
---
[Square] (3) 1/3 - 3
9



 ###
 ###
 ###
```
### 11. Square size
Update the class ``Square`` by adding the public getter and setter ``size``
- The setter should assign (in this order) the ``width`` and the ``height`` - with the same value
- The setter should have the same value validation as the ``Rectangle`` for ``width`` and ``height`` - No need to change the exception error message (It should be the one from ``width``)
```bash
$ cat 10-main.py
#!/usr/bin/python3
""" 10-main """
from models.square import Square

if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.size)
    s1.size = 10
    print(s1)

    try:
        s1.size = "9"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

$ ./10-main.py
[Square] (1) 0/0 - 5
5
[Square] (1) 0/0 - 10
[TypeError] width must be an integer
```
### 12. Square update
Update the class ``Square`` by adding the public method ``def update(self, *args, **kwargs)`` that assigns attributes:
- ``*args`` is the list of arguments - no-keyworded arguments
    + 1st argument should be the ``id`` attribute
    + 2nd argument should be the ``size`` attribute
    + 3rd argument should be the ``x`` attribute
    + 4th argument should be the ``y`` attribute
- ``**kwargs`` can be thought of as a double pointer to a dictionary: key/value (keyworded arguments)
- ``**kwargs`` must be skipped if *args exists and is not empty
- Each key in this dictionary represents an attribute to the instance
```bash
$ cat 11-main.py
#!/usr/bin/python3
""" 11-main """
from models.square import Square

if __name__ == "__main__":

    s1 = Square(5)
    print(s1)

    s1.update(10)
    print(s1)

    s1.update(1, 2)
    print(s1)

    s1.update(1, 2, 3)
    print(s1)

    s1.update(1, 2, 3, 4)
    print(s1)

    s1.update(x=12)
    print(s1)

    s1.update(size=7, y=1)
    print(s1)

    s1.update(size=7, id=89, y=1)
    print(s1)

$ ./11-main.py
[Square] (1) 0/0 - 5
[Square] (10) 0/0 - 5
[Square] (1) 0/0 - 2
[Square] (1) 3/0 - 2
[Square] (1) 3/4 - 2
[Square] (1) 12/4 - 2
[Square] (1) 12/1 - 7
[Square] (89) 12/1 - 7
```
### 13. Rectangle instance to dictionary representation
Update the class ``Rectangle`` by adding the public method ``def to_dictionary(self):`` that returns the dictionary representation of a ``Rectangle``:
This dictionary must contain:
- ``id``
- ``width``
- ``height``
- ``x``
- ``y``
```bash
$ cat 12-main.py
#!/usr/bin/python3
""" 12-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2, 1, 9)
    print(r1)
    r1_dictionary = r1.to_dictionary()
    print(r1_dictionary)
    print(type(r1_dictionary))

    r2 = Rectangle(1, 1)
    print(r2)
    r2.update(**r1_dictionary)
    print(r2)
    print(r1 == r2)

$ ./12-main.py
[Rectangle] (1) 1/9 - 10/2
{'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
<class 'dict'>
[Rectangle] (2) 0/0 - 1/1
[Rectangle] (1) 1/9 - 10/2
False
```
### 14. Square instance to dictionary representation
Update the class ``Square`` by adding the public method ``def to_dictionary(self):`` that returns the dictionary representation of a ``Square``:
This dictionary must contain:
- ``id``
- ``size``
- ``x``
- ``y``
```bash
$ cat 13-main.py
#!/usr/bin/python3
""" 13-main """
from models.square import Square

if __name__ == "__main__":

    s1 = Square(10, 2, 1)
    print(s1)
    s1_dictionary = s1.to_dictionary()
    print(s1_dictionary)
    print(type(s1_dictionary))

    s2 = Square(1, 1)
    print(s2)
    s2.update(**s1_dictionary)
    print(s2)
    print(s1 == s2)

$ ./13-main.py
[Square] (1) 2/1 - 10
{'id': 1, 'x': 2, 'size': 10, 'y': 1}
<class 'dict'>
[Square] (2) 1/0 - 1
[Square] (1) 2/1 - 10
False
```
### 15. Dictionary to JSON string
JSON is one of the standard formats for sharing data representation.
Update the class ``Base`` by adding the static method ``def to_json_string(list_dictionaries):`` that returns the JSON string representation of ``list_dictionaries``:
- ``list_dictionaries`` is a list of dictionaries
- If ``list_dictionaries`` is ``None`` or empty, return the string: ``"[]"``
- Otherwise, return the JSON string representation of ``list_dictionaries``
```bash
$ cat 14-main.py
#!/usr/bin/python3
""" 14-main """
from models.base import Base
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    json_dictionary = Base.to_json_string([dictionary])
    print(dictionary)
    print(type(dictionary))
    print(json_dictionary)
    print(type(json_dictionary))

$ ./14-main.py
{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
<class 'dict'>
[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]
<class 'str'>
```
### 16. JSON string to file
Update the class ``Base`` by adding the class method ``def save_to_file(cls, list_objs):`` that writes the JSON string representation of ``list_objs`` to a file:
- ``list_objs`` is a list of instances who inherits of ``Base`` - example: list of ``Rectangle`` or list of ``Square`` instances
- If ``list_objs`` is ``None``, save an empty list
- The filename must be: ``<Class name>.json`` - example: ``Rectangle.json``
- You must use the static method ``to_json_string`` (created before)
- You must overwrite the file if it already exists
```bash
$ cat 15-main.py
#!/usr/bin/python3
""" 15-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    Rectangle.save_to_file([r1, r2])

    with open("Rectangle.json", "r") as file:
        print(file.read())

$ ./15-main.py
[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]
```
### 17. JSON string to dictionary
Update the class ``Base`` by adding the static method ``def from_json_string(json_string):`` that returns the list of the JSON string representation ``json_string``:
- ``json_string`` is a string representing a list of dictionaries
- If ``json_string`` is None or empty, return an empty list
- Otherwise, return the list represented by ``json_string``
```bash
$ cat 16-main.py
#!/usr/bin/python3
""" 16-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    list_input = [
        {'id': 89, 'width': 10, 'height': 4}, 
        {'id': 7, 'width': 1, 'height': 7}
    ]
    json_list_input = Rectangle.to_json_string(list_input)
    list_output = Rectangle.from_json_string(json_list_input)
    print("[{}] {}".format(type(list_input), list_input))
    print("[{}] {}".format(type(json_list_input), json_list_input))
    print("[{}] {}".format(type(list_output), list_output))

$ ./16-main.py
[<class 'list'>] [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}]
[<class 'str'>] [{"height": 4, "width": 10, "id": 89}, {"height": 7, "width": 1, "id": 7}]
[<class 'list'>] [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}]
```
### 18. Dictionary to Instance
Update the class ``Base`` by adding the class method ``def create(cls, **dictionary):`` that returns an instance with all attributes already set:
- ``**dictionary`` can be thought of as a double pointer to a dictionary
- To use the ``update`` method to assign all attributes, you must create a “dummy” instance before:
    + Create a ``Rectangle`` or ``Square`` instance with “dummy” mandatory attributes (width, height, size, etc.)
    + Call ``update`` instance method to this “dummy” instance to apply your real values
- You must use the method ``def update(self, *args, **kwargs)``
- ``**dictionary`` must be used as ``**kwargs`` of the method ``update``
- You are not allowed to use ``eval``
```bash
$ cat 17-main.py
#!/usr/bin/python3
""" 17-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(3, 5, 1)
    r1_dictionary = r1.to_dictionary()
    r2 = Rectangle.create(**r1_dictionary)
    print(r1)
    print(r2)
    print(r1 is r2)
    print(r1 == r2)

$ ./17-main.py
[Rectangle] (1) 1/0 - 3/5
[Rectangle] (1) 1/0 - 3/5
False
False
```
### 19. File to instances
Update the class ``Base`` by adding the class method ``def load_from_file(cls):`` that returns a list of instances:
- The filename must be: ``<Class name>.json`` - example: ``Rectangle.json``
- If the file doesn’t exist, return an empty list
- Otherwise, return a list of instances - the type of these instances depends on ``cls`` (current class using this method)
- You must use the ``from_json_string`` and ``create`` methods (implemented previously)
```bash
$ cat 18-main.py
#!/usr/bin/python3
""" 18-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]

    Rectangle.save_to_file(list_rectangles_input)

    list_rectangles_output = Rectangle.load_from_file()

    for rect in list_rectangles_input:
        print("[{}] {}".format(id(rect), rect))

    print("---")

    for rect in list_rectangles_output:
        print("[{}] {}".format(id(rect), rect))

    print("---")
    print("---")

    s1 = Square(5)
    s2 = Square(7, 9, 1)
    list_squares_input = [s1, s2]

    Square.save_to_file(list_squares_input)

    list_squares_output = Square.load_from_file()

    for square in list_squares_input:
        print("[{}] {}".format(id(square), square))

    print("---")

    for square in list_squares_output:
        print("[{}] {}".format(id(square), square))

$ ./18-main.py
[139785912033120] [Rectangle] (1) 2/8 - 10/7
[139785912033176] [Rectangle] (2) 0/0 - 2/4
---
[139785911764752] [Rectangle] (1) 2/8 - 10/7
[139785911764808] [Rectangle] (2) 0/0 - 2/4
---
---
[139785912058040] [Square] (5) 0/0 - 5
[139785912061848] [Square] (6) 9/1 - 7
---
[139785911764976] [Square] (5) 0/0 - 5
[139785911765032] [Square] (6) 9/1 - 7
```
### 20. JSON ok, but CSV?
Update the class ``Base`` by adding the class methods ``def save_to_file_csv(cls, list_objs):`` and ``def load_from_file_csv(cls):`` that serializes and deserializes in CSV:
- The filename must be: ``<Class name>.csv`` - example: ``Rectangle.csv``
- Has the same behavior as the JSON serialization/deserialization
- Format of the CSV:
    + Rectangle: ``<id>,<width>,<height>,<x>,<y>``
    + Square: ``<id>,<size>,<x>,<y>``
```bash
$ cat 100-main.py
#!/usr/bin/python3
""" 100-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]

    Rectangle.save_to_file_csv(list_rectangles_input)

    list_rectangles_output = Rectangle.load_from_file_csv()

    for rect in list_rectangles_input:
        print("[{}] {}".format(id(rect), rect))

    print("---")

    for rect in list_rectangles_output:
        print("[{}] {}".format(id(rect), rect))

    print("---")
    print("---")

    s1 = Square(5)
    s2 = Square(7, 9, 1)
    list_squares_input = [s1, s2]

    Square.save_to_file_csv(list_squares_input)

    list_squares_output = Square.load_from_file_csv()

    for square in list_squares_input:
        print("[{}] {}".format(id(square), square))

    print("---")

    for square in list_squares_output:
        print("[{}] {}".format(id(square), square))

$ ./100-main.py
[140268695797600] [Rectangle] (1) 2/8 - 10/7
[140268695797656] [Rectangle] (2) 0/0 - 2/4
---
[140268695529008] [Rectangle] (1) 2/8 - 10/7
[140268695528952] [Rectangle] (2) 0/0 - 2/4
---
---
[140268695822520] [Square] (5) 0/0 - 5
[140268695826328] [Square] (6) 9/1 - 7
---
[140268695529232] [Square] (5) 0/0 - 5
[140268695529176] [Square] (6) 9/1 - 7
```
### 21. Let's draw it
Update the class ``Base`` by adding the static method ``def draw(list_rectangles, list_squares):`` that opens a window and draws all the ``Rectangles`` and ``Squares``:
- You must use the [Turtle graphics module](https://docs.python.org/3.0/library/turtle.html)
- To install it: ``sudo apt-get install python3-tk``
- To make the GUI available outside your vagrant machine, add this line in your Vagrantfile: ``config.ssh.forward_x11 = true``
- No constraints for color, shape etc… be creative!
```bash
$ cat 101-main.py
#!/usr/bin/python3
""" 101-main """
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    list_rectangles = [Rectangle(100, 40), Rectangle(90, 110, 30, 10), Rectangle(20, 25, 110, 80)]
    list_squares = [Square(35), Square(15, 70, 50), Square(80, 30, 70)]

    Base.draw(list_rectangles, list_squares)

$ ./101-main.py
....
```
- Uncommented line in ``/etc/ssh/ssh_config`` that said ``# ForwardX11`` no and change ``no`` to ``yes``.
- Then added line ``config.ssh.forward_agent = true`` to my Vagrantfile in addition to ``config.ssh.forward_x11 = true``.
- Halted my vm with ``vagrant halt`` and started it back up with ``vagrant up --provision`` then ``vagrant ssh``.
- If you get an error that looks like ``/usr/bin/xauth: timeout in locking authority file /home/vagrant/.Xauthority``, then enter ``rm .Xauthority`` (you may have to ``sudo``).
- Logout and restart the vm with ``vagrant up --provision``.
- Test with ``xeyes``. If Xquartz is installed on the Mac OS it should open in an Xquartz window.
