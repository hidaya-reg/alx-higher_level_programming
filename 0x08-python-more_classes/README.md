# 0x08-python-more_classes
## Resources
- [Object Oriented Programming](https://python.swaroopch.com/oop.html) (Read everything until the paragraph “Inheritance” (excluded))
- [Object-Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php) (Please be careful: in most of the following paragraphs, the author shows the way you should not use or write a class, in order to help you better understand - some concepts and how everything works in Python 3. Make sure you read only the following paragraphs: “General Introduction,” “First-class Everything,” “A Minimal Class in Python,” “Attributes,” “Methods,” “The ``__init__`` Method,” “Data Abstraction, Data Encapsulation, and Information Hiding,” “``__str__``- and ``__repr__``-Methods,” “Public- Protected- and Private Attributes,” & “Destructor”)
- [Class and Instance Attributes](https://python-course.eu/oop/class-instance-attributes.php)
- [classmethods and staticmethods](https://www.youtube.com/watch?v=rq8cL2XMM5M&ab_channel=CoreySchafer)
- [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php) (Mainly the last part “Public instead of Private Attributes”)
- [str vs repr](https://shipit.dev/posts/python-str-vs-repr.html)

## Learning Objectives
<details>
<summary>What are the special ``__str__`` and ``__repr__`` methods and how to use them</summary>

### ``__str__`` and ``__repr__`` methods
They are special methods used to define how objects of a class are represented as strings. They serve different purposes and are used in different contexts.
#### ``__str__`` Method
**- Purpose:** The ``__str__`` method is intended to provide a "nice" or user-friendly string representation of an object. It's used when you want to create a readable output for end users.
**- Usage:** It is called by the built-in ``str()`` function and by the ``print()`` function.
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, {self.age} years old"

person = Person("Alice", 30)
print(person)  # Output: Alice, 30 years old
```
#### ``__repr__`` Method
**- Purpose:** The`` __repr__`` method is intended to provide a more detailed and unambiguous string representation of an object, which is mainly useful for debugging and development. Ideally, the output should be a valid Python expression that could be used to recreate the object.
**- Usage:** It is called by the built-in ``repr()`` function and is also used when you inspect objects in an interactive session (like in a Python shell).
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

person = Person("Alice", 30)
print(repr(person))  # Output: Person(name='Alice', age=30)
```
#### Default Implementations
- If you do not define ``__str__``, Python will fall back to using ``__repr__ ``for string representation.
- If you do not define either, Python will provide a default implementation that includes the object's memory address.
#### When to Use Them
- Use ``__str__`` when you want to define a string representation for end-user output, focusing on readability and clarity.
- Use ``__repr__`` when you want to define a string representation that is useful for developers and debugging, focusing on providing enough detail to recreate the object.

</details>

<details>
<summary>What's `eval()` and how to use it</summary>

### `eval()` function
``eval()`` is a built-in Python function that parses the expression provided as a string and evaluates it as a Python expression. It can be used to execute dynamically created code or expressions, allowing you to run Python code that is constructed as a string at runtime.
**Syntax:** `eval(expression, globals=None, locals=None)`
- *expression*: A string containing a Python expression (like mathematical operations or variable assignments).
- *globals* (optional): A dictionary to specify the global namespace in which the expression will be evaluated.
- *locals* (optional): A dictionary to specify the local namespace in which the expression will be evaluated.
#### Basic Usage
**1. Simple Expressions**
```python
result = eval("3 + 5")
print(result)  # Output: 8
```
**2. Using Variables**
```python
x = 10
y = 5
result = eval("x * y")  # Using the variables x and y
print(result)  # Output: 50
```
**3. Complex Expressions**
```python
result = eval("2 * (3 + 4) - 5 / 5")
print(result)  # Output: 14.0
```
**4. Using Global and Local Contexts**
```python
def evaluate_expression(expr):
    x = 2
    return eval(expr, {"__builtins__": None}, {"x": x})

result = evaluate_expression("x + 5")
print(result)  # Output: 7
```
**5. To recreate an object from its ``__repr__``**
The string returned by ``__repr__`` should ideally be a valid Python expression that can be evaluated to produce an equivalent object. This means that the ``__repr__`` method should return a string that resembles a call to the class constructor with the appropriate arguments.
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, {self.age} years old"
    
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"  # Recreate using constructor

# Create a Person instance
person = Person("Alice", 30)

# Get the repr representation
person_repr = repr(person)
print(person_repr)  # Output: Person(name='Alice', age=30)

# Use eval to recreate the object
# Note: Using eval can be risky if you are dealing with untrusted input.
recreated_person = eval(person_repr)
print(recreated_person)  # Output: Person(name='Alice', age=30)
print(recreated_person.name)  # Output: Alice
print(recreated_person.age)   # Output: 30
```
**Important Notes**
- Security Risk: Using ``eval()`` can execute arbitrary code and poses security risks, especially if the input string is not from a trusted source. Be cautious when using ``eval()``.
- Constructor Arguments: Ensure that the arguments passed in the ``__repr__`` string are sufficient to recreate the object. If the constructor requires complex types or additional processing, you might need to implement more logic to handle those cases.
- Alternatives to ``eval()``: If you're concerned about the security of using ``eval()``, consider implementing a factory method or using ``ast.literal_eval()`` for safer evaluation of strings representing Python literals (though this is limited to certain types).

Here’s how you could implement a safer factory method instead of relying on eval():
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, {self.age} years old"
    
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

    @classmethod
    def from_repr(cls, repr_str):
        # Parse the string to recreate the object (requires a specific format)
        # Note: This example assumes a specific format; you may need to adjust parsing logic for general cases.
        import re
        match = re.match(r"Person\(name='([^']+)', age=(\d+)\)", repr_str)
        if match:
            name, age = match.groups()
            return cls(name, int(age))
        raise ValueError("Invalid representation string")

# Create a Person instance
person = Person("Alice", 30)

# Get the repr representation
person_repr = repr(person)
print(person_repr)  # Output: Person(name='Alice', age=30)

# Use the factory method to recreate the object
recreated_person = Person.from_repr(person_repr)
print(recreated_person)  # Output: Person(name='Alice', age=30)
```
This approach avoids the risks associated with ``eval()`` by implementing controlled parsing logic.
**Dangerous use of eval**
```python
# Dangerous use of eval
user_input = "__import__('os').system('ls')"
eval(user_input)  # This could execute any command on the system
```
#### Alternatives
``ast.literal_eval()``: This function can safely evaluate strings containing Python literals (like strings, numbers, tuples, lists, dicts, booleans, and ``None``) without executing arbitrary code.
```python
import ast

safe_string = "[1, 2, 3]"
result = ast.literal_eval(safe_string)
print(result)  # Output: [1, 2, 3]
```
</details>

<details>
<summary>What is the difference between a object attribute and a class attribute</summary>

### Object ttribute vs. Class Attribute

| Feature               | Object Attribute                        | Class Attribute                           |
|-----------------------|----------------------------------------|------------------------------------------|
| **Definition**        | Defined inside methods and specific to an instance. | Defined directly in the class body.     |
| **Scope**             | Unique to each instance of the class. | Shared among all instances of the class. |
| **Storage**           | Stored in the instance's `__dict__`. | Stored in the class's `__dict__`.      |
| **Access**            | Accessed using the instance (e.g., `instance.attribute`). | Accessed using the class name or an instance (e.g., `ClassName.attribute` or `instance.attribute`). |
| **Overriding**        | Can be overridden by instance attributes with the same name. | Can be overridden by instance attributes, but changes to the class attribute will reflect across all instances unless overridden. |
| **Usage**             | Typically used to store data specific to each object. | Typically used for constants or data that should be shared across all objects of the class. |


#### Example
```python
class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Object attributes
        self.name = name
        self.age = age

# Creating instances of Dog
dog1 = Dog("Buddy", 5)
dog2 = Dog("Max", 3)

# Accessing object attributes
print(dog1.name)  # Output: Buddy
print(dog2.age)   # Output: 3

# Accessing class attribute
print(dog1.species)  # Output: Canis familiaris
print(dog2.species)  # Output: Canis familiaris

# Modifying object attribute
dog1.age = 6
print(dog1.age)  # Output: 6 (unique to dog1)

# Modifying class attribute
Dog.species = "Canis lupus familiaris"
print(dog1.species)  # Output: Canis lupus familiaris
print(dog2.species)  # Output: Canis lupus familiaris
```
</details>

<details>
<summary>What is a class method</summary>

### Class method
A **class method** is a method that is bound to the class rather than its instances. It can access class attributes and other class methods but not instance attributes or methods. Class methods are defined using the ``@classmethod`` decorator and take the class itself as the first parameter, conventionally named ``cls``.
#### Key Characteristics of Class Methods:
**1. Access to Class State:** Class methods can modify the state of the class (class variables) and can also create new instances of the class.
**2. Calling Convention:** They are called on the class itself rather than on instances of the class. However, they can also be called on instances.
**3. Use Cases:** Class methods are often used for factory methods, which instantiate instances of the class using different parameters or for alternate initialization logic.
```python
class MyClass:
    class_variable = 0

    def __init__(self, value):
        self.instance_variable = value

    @classmethod
    def increment_class_variable(cls):
        cls.class_variable += 1

    @classmethod
    def create_instance(cls, value):
        return cls(value)

# Using the class method to increment the class variable
MyClass.increment_class_variable()
print(MyClass.class_variable)  # Output: 1

# Using the class method to create an instance
instance = MyClass.create_instance(10)
print(instance.instance_variable)  # Output: 10
```
</details>

<details>
<summary>What is a static method</summary>

### Static method
A **static method** is a method that belongs to a class rather than an instance of the class. It does not access or modify the class or instance state. Static methods are defined using the ``@staticmethod`` decorator and do not take a special first parameter like ``self`` (for instance methods) or ``cls`` (for class methods).
#### Key Characteristics of Static Methods:
**1. No Access to Class or Instance State:** Static methods cannot access or modify class variables or instance variables. They are self-contained and operate independently.
**2. Utility Functions:** Static methods are often used for utility functions that perform a task in isolation, where the behavior does not depend on class or instance state.
**3. Calling Convention:** They can be called on the class itself or on instances of the class.
```python
class MathUtils:
    
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

# Calling static methods without creating an instance
result_add = MathUtils.add(5, 3)
result_multiply = MathUtils.multiply(4, 2)

print(result_add)       # Output: 8
print(result_multiply)  # Output: 8
```
</details>

## Tasks
### 0. Simple rectangle
Write an empty class ``Rectangle`` that defines a rectangle:
You are not allowed to import any module
```bash
$ cat 0-main.py
#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)

$ ./0-main.py
<class '0-rectangle.Rectangle'>
{}
```
**No test cases needed**
### 1. Real definition of a rectangle
Write a class ``Rectangle`` that defines a rectangle by: (based on ``0-rectangle.py``)
- Private instance attribute: ``width``:
    + property ``def width(self):`` to retrieve it
    + property setter ``def width(self, value):`` to set it:
        - ``width`` must be an integer, otherwise raise a ``TypeError`` exception with the message ``width must be an integer``
        - if ``width`` is less than ``0``, raise a ``ValueError`` exception ``with the message width must be >= 0``
- Private instance attribute: ``height``:
    + property ``def height(self):`` to retrieve it
    + property setter ``def height(self, value):`` to set it:
        - ``height`` must be an integer, otherwise raise a ``TypeError`` exception with the message ``height must be an integer``
        - if ``height`` is less than ``0``, raise a ``ValueError`` exception with the message ``height must be >= 0``
- Instantiation with optional ``width`` and ``height``: ``def __init__(self, width=0, height=0):``
- You are not allowed to import any module
```bash
$ cat 1-main.py
#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)

$ ./1-main.py
{'_Rectangle__height': 4, '_Rectangle__width': 2}
{'_Rectangle__height': 3, '_Rectangle__width': 10}
```
**No test cases needed**
### 2. Area and Perimeter
Write a class ``Rectangle`` that defines a rectangle by: (based on ``1-rectangle.py``)
- Private instance attribute: ``width``:
    + property ``def width(self):`` to retrieve it
    + property setter ``def width(self, value):`` to set it:
        - ``width`` must be an integer, otherwise raise a ``TypeError`` exception with the message ``width must be an integer``
        - if ``width`` is less than ``0``, raise a ``ValueError`` exception ``with the message width must be >= 0``
- Private instance attribute: ``height``:
    + property ``def height(self):`` to retrieve it
    + property setter ``def height(self, value):`` to set it:
        - ``height`` must be an integer, otherwise raise a ``TypeError`` exception with the message ``height must be an integer``
        - if ``height`` is less than ``0``, raise a ``ValueError`` exception with the message ``height must be >= 0``
- Instantiation with optional ``width`` and ``height``: ``def __init__(self, width=0, height=0):``
- Public instance method: ``def area(self):`` that returns the rectangle area
- Public instance method: ``def perimeter(self):`` that returns the rectangle perimeter:
    + if ``width`` or ``height`` is equal to ``0``, perimeter is equal to ``0``
- You are not allowed to import any module
```bash
$ cat 2-main.py
#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

$ ./2-main.py
Area: 8 - Perimeter: 12
--
Area: 30 - Perimeter: 26
```
**No test cases needed**
### 3. String representation
Write a class ``Rectangle`` that defines a rectangle by: (based on ``2-rectangle.py``)
- Private instance attribute: ``width``:
    + property ``def width(self):`` to retrieve it
    + property setter ``def width(self, value):`` to set it:
        - ``width`` must be an integer, otherwise raise a ``TypeError`` exception with the message ``width must be an integer``
        - if ``width`` is less than ``0``, raise a ``ValueError`` exception ``with the message width must be >= 0``
- Private instance attribute: ``height``:
    + property ``def height(self):`` to retrieve it
    + property setter ``def height(self, value):`` to set it:
        - ``height`` must be an integer, otherwise raise a ``TypeError`` exception with the message ``height must be an integer``
        - if ``height`` is less than ``0``, raise a ``ValueError`` exception with the message ``height must be >= 0``
- Instantiation with optional ``width`` and ``height``: ``def __init__(self, width=0, height=0):``
- Public instance method: ``def area(self):`` that returns the rectangle area
- Public instance method: ``def perimeter(self):`` that returns the rectangle perimeter:
    + if ``width`` or ``height`` is equal to ``0``, perimeter is equal to ``0``
- ``print()`` and ``str()`` should print the rectangle with the character ``#``: (see example below)
    + if ``width`` or ``height`` is equal to ``0``, return an empty string
- You are not allowed to import any module
```bash
$ cat 3-main.py
#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))

$ ./3-main.py
Area: 8 - Perimeter: 12
##
##
##
##
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
--
##########
##########
##########
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
```
**Object address can be different**
**No test cases needed**
### 4. Eval is magic
Write a class ``Rectangle`` that defines a rectangle by: (based on ``3-rectangle.py``)
- Private instance attribute: ``width``:
    + property ``def width(self):`` to retrieve it
    + property setter ``def width(self, value):`` to set it:
        - ``width`` must be an integer, otherwise raise a ``TypeError`` exception with the message ``width must be an integer``
        - if ``width`` is less than ``0``, raise a ``ValueError`` exception ``with the message width must be >= 0``
- Private instance attribute: ``height``:
    + property ``def height(self):`` to retrieve it
    + property setter ``def height(self, value):`` to set it:
        - ``height`` must be an integer, otherwise raise a ``TypeError`` exception with the message ``height must be an integer``
        - if ``height`` is less than ``0``, raise a ``ValueError`` exception with the message ``height must be >= 0``
- Instantiation with optional ``width`` and ``height``: ``def __init__(self, width=0, height=0):``
- Public instance method: ``def area(self):`` that returns the rectangle area
- Public instance method: ``def perimeter(self):`` that returns the rectangle perimeter:
    + if ``width`` or ``height`` is equal to ``0``, perimeter is equal to ``0``
- ``print()`` and ``str()`` should print the rectangle with the character ``#``: (see example below)
    + if ``width`` or ``height`` is equal to ``0``, return an empty string
- ``repr()`` should return a string representation of the rectangle to be able to recreate a new instance by using ``eval()`` (see example below)
- You are not allowed to import any module
```bash
$ cat 4-main.py
#!/usr/bin/python3
Rectangle = __import__('4-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print("--")
print(my_rectangle)
print("--")
print(repr(my_rectangle))
print("--")
print(hex(id(my_rectangle)))
print("--")

# create new instance based on representation
new_rectangle = eval(repr(my_rectangle))
print(str(new_rectangle))
print("--")
print(new_rectangle)
print("--")
print(repr(new_rectangle))
print("--")
print(hex(id(new_rectangle)))
print("--")

print(new_rectangle is my_rectangle)
print(type(new_rectangle) is type(my_rectangle))

$ ./4-main.py
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7cc88
--
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7ccc0
--
False
True
```
**No test cases needed**
### 5. Detect instance deletion
Write a class ``Rectangle`` that defines a rectangle by: (based on ``4-rectangle.py``)
- Private instance attribute: ``width``:
    + property ``def width(self):`` to retrieve it
    + property setter ``def width(self, value):`` to set it:
        - ``width`` must be an integer, otherwise raise a ``TypeError`` exception with the message ``width must be an integer``
        - if ``width`` is less than ``0``, raise a ``ValueError`` exception ``with the message width must be >= 0``
- Private instance attribute: ``height``:
    + property ``def height(self):`` to retrieve it
    + property setter ``def height(self, value):`` to set it:
        - ``height`` must be an integer, otherwise raise a ``TypeError`` exception with the message ``height must be an integer``
        - if ``height`` is less than ``0``, raise a ``ValueError`` exception with the message ``height must be >= 0``
- Instantiation with optional ``width`` and ``height``: ``def __init__(self, width=0, height=0):``
- Public instance method: ``def area(self):`` that returns the rectangle area
- Public instance method: ``def perimeter(self):`` that returns the rectangle perimeter:
    + if ``width`` or ``height`` is equal to ``0``, perimeter is equal to ``0``
- ``print()`` and ``str()`` should print the rectangle with the character ``#``: (see example below)
    + if ``width`` or ``height`` is equal to ``0``, return an empty string
- ``repr()`` should return a string representation of the rectangle to be able to recreate a new instance by using ``eval()``
- Print the message ``Bye rectangle...`` (``...`` being 3 dots not ellipsis) when an instance of ``Rectangle`` is deleted
- You are not allowed to import any module
```bash
$ cat 5-main.py
#!/usr/bin/python3
Rectangle = __import__('5-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

del my_rectangle

try:
    print(my_rectangle)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

$ ./5-main.py
Area: 8 - Perimeter: 12
Bye rectangle...
[NameError] name 'my_rectangle' is not defined
```
**No test cases needed**
### 6. How many instances
Write a class ``Rectangle`` that defines a rectangle by: (based on ``5-rectangle.py``)
- Private instance attribute: ``width``:
    + property ``def width(self):`` to retrieve it
    + property setter ``def width(self, value):`` to set it:
        - ``width`` must be an integer, otherwise raise a ``TypeError`` exception with the message ``width must be an integer``
        - if ``width`` is less than ``0``, raise a ``ValueError`` exception ``with the message width must be >= 0``
- Private instance attribute: ``height``:
    + property ``def height(self):`` to retrieve it
    + property setter ``def height(self, value):`` to set it:
        - ``height`` must be an integer, otherwise raise a ``TypeError`` exception with the message ``height must be an integer``
        - if ``height`` is less than ``0``, raise a ``ValueError`` exception with the message ``height must be >= 0``
- Public class attribute ``number_of_instances``:
    + Initialized to ``0``
    + Incremented during each new instance instantiation
    + Decremented during each instance deletion
- Instantiation with optional ``width`` and ``height``: ``def __init__(self, width=0, height=0):``
- Public instance method: ``def area(self):`` that returns the rectangle area
- Public instance method: ``def perimeter(self):`` that returns the rectangle perimeter:
    + if ``width`` or ``height`` is equal to ``0``, perimeter is equal to ``0``
- ``print()`` and ``str()`` should print the rectangle with the character ``#``:
    + if ``width`` or ``height`` is equal to ``0``, return an empty string
- ``repr()`` should return a string representation of the rectangle to be able to recreate a new instance by using ``eval()``
- Print the message ``Bye rectangle...`` (``...`` being 3 dots not ellipsis) when an instance of ``Rectangle`` is deleted
- You are not allowed to import any module
```bash
$ cat 6-main.py
#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle

my_rectangle_1 = Rectangle(2, 4)
my_rectangle_2 = Rectangle(2, 4)
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_1
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_2
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

$ ./6-main.py
2 instances of Rectangle
Bye rectangle...
1 instances of Rectangle
Bye rectangle...
0 instances of Rectangle
```
**No test cases needed**
### 7. Change representation
Write a class ``Rectangle`` that defines a rectangle by: (based on ``6-rectangle.py``)
- Private instance attribute: ``width``:
    + property ``def width(self):`` to retrieve it
    + property setter ``def width(self, value):`` to set it:
        - ``width`` must be an integer, otherwise raise a ``TypeError`` exception with the message ``width must be an integer``
        - if ``width`` is less than ``0``, raise a ``ValueError`` exception ``with the message width must be >= 0``
- Private instance attribute: ``height``:
    + property ``def height(self):`` to retrieve it
    + property setter ``def height(self, value):`` to set it:
        - ``height`` must be an integer, otherwise raise a ``TypeError`` exception with the message ``height must be an integer``
        - if ``height`` is less than ``0``, raise a ``ValueError`` exception with the message ``height must be >= 0``
- Public class attribute ``number_of_instances``:
    + Initialized to ``0``
    + Incremented during each new instance instantiation
    + Decremented during each instance deletion
- Public class attribute ``print_symbol``:
    + Initialized to ``#``
    + Used as symbol for string representation
    + Can be any type
- Instantiation with optional ``width`` and ``height``: ``def __init__(self, width=0, height=0):``
- Public instance method: ``def area(self):`` that returns the rectangle area
- Public instance method: ``def perimeter(self):`` that returns the rectangle perimeter:
    + if ``width`` or ``height`` is equal to ``0``, perimeter is equal to ``0``
- ``print()`` and ``str()`` should print the rectangle with the character(s) stored in ``print_symbol``:
    + if ``width`` or ``height`` is equal to ``0``, return an empty string
- ``repr()`` should return a string representation of the rectangle to be able to recreate a new instance by using ``eval()``
- Print the message ``Bye rectangle...`` (``...`` being 3 dots not ellipsis) when an instance of ``Rectangle`` is deleted
- You are not allowed to import any module
```bash
$ cat 7-main.py
#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)
print("--")
my_rectangle_1.print_symbol = "&"
print(my_rectangle_1)
print("--")

my_rectangle_2 = Rectangle(2, 1)
print(my_rectangle_2)
print("--")
Rectangle.print_symbol = "C"
print(my_rectangle_2)
print("--")

my_rectangle_3 = Rectangle(7, 3)
print(my_rectangle_3)

print("--")

my_rectangle_3.print_symbol = ["C", "is", "fun!"]
print(my_rectangle_3)

print("--")

$ ./7-main.py
########
########
########
########
--
&&&&&&&&
&&&&&&&&
&&&&&&&&
&&&&&&&&
--
##
--
CC
--
CCCCCCC
CCCCCCC
CCCCCCC
--
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
--
Bye rectangle...
Bye rectangle...
Bye rectangle...
```
**No test cases needed**
### 8. Compare rectangles
Write a class ``Rectangle`` that defines a rectangle by: (based on ``7-rectangle.py``)
- Private instance attribute: ``width``:
    + property ``def width(self):`` to retrieve it
    + property setter ``def width(self, value):`` to set it:
        - ``width`` must be an integer, otherwise raise a ``TypeError`` exception with the message ``width must be an integer``
        - if ``width`` is less than ``0``, raise a ``ValueError`` exception ``with the message width must be >= 0``
- Private instance attribute: ``height``:
    + property ``def height(self):`` to retrieve it
    + property setter ``def height(self, value):`` to set it:
        - ``height`` must be an integer, otherwise raise a ``TypeError`` exception with the message ``height must be an integer``
        - if ``height`` is less than ``0``, raise a ``ValueError`` exception with the message ``height must be >= 0``
- Public class attribute ``number_of_instances``:
    + Initialized to ``0``
    + Incremented during each new instance instantiation
    + Decremented during each instance deletion
- Public class attribute ``print_symbol``:
    + Initialized to ``#``
    + Used as symbol for string representation
    + Can be any type
- Instantiation with optional ``width`` and ``height``: ``def __init__(self, width=0, height=0):``
- Public instance method: ``def area(self):`` that returns the rectangle area
- Public instance method: ``def perimeter(self):`` that returns the rectangle perimeter:
    + if ``width`` or ``height`` is equal to ``0``, perimeter is equal to ``0``
- ``print()`` and ``str()`` should print the rectangle with the character `#`:
    + if ``width`` or ``height`` is equal to ``0``, return an empty string
- ``repr()`` should return a string representation of the rectangle to be able to recreate a new instance by using ``eval()``
- Print the message ``Bye rectangle...`` (``...`` being 3 dots not ellipsis) when an instance of ``Rectangle`` is deleted
- Static method ``def bigger_or_equal(rect_1, rect_2):`` that returns the biggest rectangle based on the area
    + ``rect_1`` must be an instance of ``Rectangle``, otherwise raise a ``TypeError`` exception with the message ``rect_1 must be an instance of Rectangle``
    + ``rect_2`` must be an instance of ``Rectangle``, otherwise raise a ``TypeError`` exception with the message ``rect_2 must be an instance of Rectangle``
    + Returns ``rect_1`` if both have the same area value
- You are not allowed to import any module
```bash
$ cat 8-main.py
#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")


my_rectangle_2.width = 10
my_rectangle_2.height = 5
if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")

$ ./8-main.py
my_rectangle_1 is bigger or equal to my_rectangle_2
my_rectangle_2 is bigger than my_rectangle_1
Bye rectangle...
Bye rectangle...
```
**No test cases needed**
### 9. A square is a rectangle
Write a class ``Rectangle`` that defines a rectangle by: (based on ``8-rectangle.py``)
- Private instance attribute: ``width``:
    + property ``def width(self):`` to retrieve it
    + property setter ``def width(self, value):`` to set it:
        - ``width`` must be an integer, otherwise raise a ``TypeError`` exception with the message ``width must be an integer``
        - if ``width`` is less than ``0``, raise a ``ValueError`` exception ``with the message width must be >= 0``
- Private instance attribute: ``height``:
    + property ``def height(self):`` to retrieve it
    + property setter ``def height(self, value):`` to set it:
        - ``height`` must be an integer, otherwise raise a ``TypeError`` exception with the message ``height must be an integer``
        - if ``height`` is less than ``0``, raise a ``ValueError`` exception with the message ``height must be >= 0``
- Public class attribute ``number_of_instances``:
    + Initialized to ``0``
    + Incremented during each new instance instantiation
    + Decremented during each instance deletion
- Public class attribute ``print_symbol``:
    + Initialized to ``#``
    + Used as symbol for string representation
    + Can be any type
- Instantiation with optional ``width`` and ``height``: ``def __init__(self, width=0, height=0):``
- Public instance method: ``def area(self):`` that returns the rectangle area
- Public instance method: ``def perimeter(self):`` that returns the rectangle perimeter:
    + if ``width`` or ``height`` is equal to ``0``, perimeter is equal to ``0``
- ``print()`` and ``str()`` should print the rectangle with the character `#`:
    + if ``width`` or ``height`` is equal to ``0``, return an empty string
- ``repr()`` should return a string representation of the rectangle to be able to recreate a new instance by using ``eval()``
- Print the message ``Bye rectangle...`` (``...`` being 3 dots not ellipsis) when an instance of ``Rectangle`` is deleted
- Static method ``def bigger_or_equal(rect_1, rect_2):`` that returns the biggest rectangle based on the area
    + ``rect_1`` must be an instance of ``Rectangle``, otherwise raise a ``TypeError`` exception with the message ``rect_1 must be an instance of Rectangle``
    + ``rect_2`` must be an instance of ``Rectangle``, otherwise raise a ``TypeError`` exception with the message ``rect_2 must be an instance of Rectangle``
    + Returns ``rect_1`` if both have the same area value
- Class method ``def square(cls, size=0):`` that returns a new Rectangle instance with ``width == height == size``
- You are not allowed to import any module
```bash
$ cat 9-main.py
#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)

$ ./9-main.py
Area: 25 - Perimeter: 20
#####
#####
#####
#####
#####
Bye rectangle...
```
**No test cases needed**
### 10. N queens
The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.
- Usage: ``nqueens N``
    + If the user called the program with the wrong number of arguments, print ``Usage: nqueens N``, followed by a new line, and exit with the status ``1``
- where N must be an integer greater or equal to ``4``
    + If N is not an integer, print ``N must be a number``, followed by a new line, and exit with the status ``1``
    + If N is smaller than ``4``, print ``N must be at least 4``, followed by a new line, and exit with the status ``1``
- The program should print every possible solution to the problem
    + One solution per line
    + Format: see example
    + You don’t have to print the solutions in a specific order
- You are only allowed to import the ``sys`` module
Read: [Queen](https://en.wikipedia.org/wiki/Queen_%28chess%29), [Backtracking](https://en.wikipedia.org/wiki/Backtracking)
```bash
julien@ubuntu:~/0x08. N Queens$ ./101-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
julien@ubuntu:~/0x08. N Queens$ ./101-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```