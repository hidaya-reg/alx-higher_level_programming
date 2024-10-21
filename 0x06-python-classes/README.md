# 0x06-python-classes 
## Resources
- [Object Oriented Programming](https://python.swaroopch.com/oop.html) (Read everything until the paragraph “Inheritance” excluded. You do NOT have to learn about class attributes, ``classmethod`` and ``staticmethod`` yet)
- [Object-Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php) (Please *be careful*: in most of the following paragraphs, the author shows things the way you should not use or write a class in order to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON’T have to learn about class attributes), Methods, The ``__init__`` Method, “Data Abstraction, Data Encapsulation, and Information Hiding,” “Public, Protected, and Private Attributes”)
- [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
- [Learn to Program 9 : Object Oriented Programming](https://www.youtube.com/watch?v=1AGyBuVCTeE&ab_channel=DerekBanas)
- [Python Classes and Objects](https://www.youtube.com/watch?v=apACNr7DC_s&ab_channel=Socratica)
- [Object Oriented Programming](https://www.youtube.com/watch?v=-DP1i2ZU9gk&ab_channel=MITOpenCourseWare)
## Learning Objectives
<details>
<summary>What is OOP</summary>

### OOP
Object-Oriented Programming (OOP) is a programming paradigm centered around the concept of **objects**. These objects can represent real-world entities or abstract data, and they are defined by **classes** that encapsulate both data (attributes) and functions (methods) that operate on the data.

#### 1. Objects
Objects are instances of classes and represent real-world entities. For example, a ``Car`` object may have attributes like ``color``, ``model``, and methods like ``start()`` or ``drive()``.
#### 2. Classes
A class is a blueprint for creating objects. It defines the properties (attributes) and behaviors (methods) that the objects created from the class will have.
```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"The {self.make} {self.model} is driving.")
```
#### 3. Encapsulation
Encapsulation means bundling the data (attributes) and the methods that operate on the data into a single unit (class). It also restricts direct access to some of the object's components to prevent unwanted modification, typically through the use of access modifiers like private or protected attributes.
```python
class Car:
    def __init__(self, make, model):
        self._make = make  # _make is protected (convention in Python)
        self.__model = model  # __model is private

    def get_model(self):
        return self.__model
```
#### 4. Inheritance
Inheritance allows one class (child/subclass) to inherit the attributes and methods of another class (parent/superclass). It promotes code reuse and a hierarchical relationship between classes.
```python
class ElectricCar(Car):  # Inheriting from Car
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity
    
    def charge(self):
        print(f"Charging {self.make} {self.model} with {self.battery_capacity} kWh battery.")
```
#### 5. Polymorphism
Polymorphism allows objects of different classes to be treated as objects of a common superclass. It also enables the same method to behave differently based on the object that calls it.
```python
class Car:
    def drive(self):
        print("The car is driving.")

class ElectricCar(Car):
    def drive(self):
        print("The electric car is driving silently.")

my_car = Car()
my_electric_car = ElectricCar()

for vehicle in (my_car, my_electric_car):
    vehicle.drive()  # Output depends on the object type
```
#### 6. Abstraction
Abstraction is the concept of hiding the complex implementation details and showing only the essential features of the object. It allows focusing on what an object does rather than how it does it.
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
```
#### Key Benefits of OOP:
- **Code reusability** through inheritance.
- **Modularity** by encapsulating functionality in objects.
- **Maintainability** by organizing code into objects that mirror real-world concepts.
- **Flexibility** via polymorphism and the ability to modify object behavior.

</details>
<details>
<summary>“first-class everything”</summary>

### First-Class Everything
The term **“first-class everything”** is often associated with programming languages that treat most or all of their fundamental entities (functions, data types, etc.) as **first-class citizens**. In a first-class everything language, many elements (like functions, objects, modules) can be used, passed, and manipulated just like data. This concept enhances the flexibility and expressiveness of the language.

#### What Does "First-Class" Mean?
A first-class citizen (or first-class object) in programming refers to an entity that has the following capabilities:
- Can be assigned to a variable.
- Can be passed as an argument to a function.
- Can be returned from a function.
- Can be stored in data structures like arrays or lists.
#### Example in Languages Like Python (First-Class Everything)
In a language like Python, almost everything is first-class, including:

##### 1. Functions:
You can assign functions to variables, pass them as arguments to other functions, and return them from functions.
```python
def greet(name):
    return f"Hello, {name}!"

# Assigning a function to a variable
say_hello = greet
print(say_hello("Alice"))  # Hello, Alice!

# Passing function as argument
def execute_func(func, value):
    return func(value)

print(execute_func(greet, "Bob"))  # Hello, Bob!
```
##### 2. Classes and Objects:
Classes themselves are first-class objects. They can be assigned to variables, passed around, and even dynamically created or modified.
```python
class Dog:
    def __init__(self, name):
        self.name = name

MyDog = Dog  # Assigning class to a variable
dog = MyDog("Fido")
print(dog.name)  # Fido
```
##### 3. Modules:
Modules are also first-class citizens and can be passed around and imported dynamically.
```python
import math

def use_module(module, func_name, value):
    func = getattr(module, func_name)
    return func(value)

print(use_module(math, "sqrt", 16))  # 4.0
```
##### 4. Everything is an Object:
In Python, numbers, strings, functions, classes, and even modules are all treated as objects. This makes Python a first-class everything language.
```python
print(type(5))  # <class 'int'>
print(type("hello"))  # <class 'str'>
print(type(greet))  # <class 'function'>
```
#### Benefits of First-Class Everything
**- Higher Flexibility:** You can treat functions, classes, and modules like any other data type, making code more modular and expressive.
**- Functional Programming Paradigm:** Languages with first-class functions often support functional programming features like higher-order functions and closures.
**- Dynamic Programming:** In dynamic languages like Python, the ability to pass around and manipulate entities like functions or classes on-the-fly allows for more flexible and reusable code.
#### Languages with "First-Class Everything"
- **Python** and **JavaScript** are often seen as "first-class everything" languages due to their ability to treat most entities as first-class objects.
- **Lisp** and **Scheme** are also considered examples of first-class everything languages, as they treat functions and data structures uniformly.
In short, "first-class everything" means that nearly every element of a language can be manipulated with the same level of flexibility as data, allowing a more fluid and dynamic coding style.
</details>

<details>
<summary>What is an attribute</summary>

### Attributes
An attribute in Object-Oriented Programming (OOP) refers to a characteristic or property of an object or a class. It is essentially a variable that holds data or state associated with a class or an object. Attributes define the properties of an object, which can be different for each instance of the class.

#### Types of Attributes
##### 1. Class Attributes (Class Variables):
- These are attributes that are shared among all instances of a class.
- They are defined within the class but outside any methods.
- Class attributes are the same for every object created from the class.
##### 2. Instance Attributes (Instance Variables):
- These are attributes that belong to individual objects (instances) of a class.
- They are defined within the class’s constructor method (typically ``__init__`` in Python) and are unique to each instance.
- Each object can have different values for its instance attributes.
```python
class Dog:
    # Class attribute
    species = "Canis lupus familiaris"  # Shared by all instances

    def __init__(self, name, age):
        # Instance attributes
        self.name = name  # Each object has its own name
        self.age = age    # Each object has its own age

# Creating two objects (instances) of the Dog class
dog1 = Dog("Buddy", 5)
dog2 = Dog("Max", 3)

# Accessing instance attributes
print(dog1.name)  # Output: Buddy
print(dog2.age)   # Output: 3

# Accessing class attribute
print(dog1.species)  # Output: Canis lupus familiaris
print(dog2.species)  # Output: Canis lupus familiaris
```
</details>

<details>
<summary>What are and how to use public, protected and private attributes</summary>

### Public, Protected and Private Attributes

In object-oriented programming (OOP), public, protected, and private attributes define the level of access control for variables and methods within a class. These access modifiers help enforce encapsulation, a key OOP principle that restricts direct access to an object's internal data.

#### 1. Public Attributes:
**- Access:** Accessible from both inside and outside the class.
**- Usage:** By default, all attributes in Python are public. This means they can be accessed and modified by any code that has access to the instance of the class.
**- Naming convention:** No special notation is required.
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Public attribute
        self.model = model  # Public attribute

# Accessing public attributes
my_car = Car("Toyota", "Corolla")
print(my_car.brand)  # Output: Toyota
my_car.model = "Camry"  # Can modify directly
print(my_car.model)  # Output: Camry
```
#### 2. Protected Attributes:
**- Access:** Should not be accessed directly from outside the class, but can be accessed from subclasses. Python does not enforce this rule strictly, but it is a convention.
**- Usage:** Use a single underscore ``_`` before the attribute name to indicate it is protected.
**- Naming convention:** A single underscore (``_attribute``).
```python
class Animal:
    def __init__(self, name, species):
        self._species = species  # Protected attribute

class Dog(Animal):
    def print_species(self):
        print(self._species)  # Accessing protected attribute in subclass

dog = Dog("Buddy", "Canine")
dog.print_species()  # Output: Canine
print(dog._species)  # Technically possible, but discouraged
```
Note: In Python, you can technically still access protected attributes from outside the class, but it is against the convention.

#### 3. Private Attributes:
**- Access:** Only accessible from within the class where they are defined, and cannot be accessed or modified directly from outside the class.
**- Usage:** Use a double underscore ``__`` before the attribute name to indicate it is private.
**- Naming convention:** A double underscore (``__attribute``).
**- Name Mangling:** Python "mangles" private attribute names to make them harder to access. The name of the attribute is modified internally (e.g., __attribute becomes _ClassName__attribute).
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount  # Accessing private attribute within class

    def get_balance(self):
        return self.__balance  # Providing controlled access via a method

account = BankAccount("Alice", 1000)
print(account.get_balance())  # Output: 1000

# Accessing private attribute directly will raise an error:
# print(account.__balance)  # AttributeError

# You can still access it via name mangling (discouraged):
print(account._BankAccount__balance)  # Output: 1000
```

| Attribute Type | Syntax       | Accessible Outside Class | Accessible in Subclasses | Notes                                           |
|----------------|--------------|--------------------------|--------------------------|-------------------------------------------------|
| **Public**     | `attribute`  | Yes                      | Yes                      | Default in Python, no access control             |
| **Protected**  | `_attribute` | Yes (but discouraged)     | Yes                      | Convention only; no strict enforcement           |
| **Private**    | `__attribute`| No (name-mangled)         | No (except via name mangling) | Enforced by Python with name mangling             |

</details>
<details>
<summary>What is ``self``</summary>

### ``self``
In Python, ``self`` is a reference to the instance of the class being operated on. It is used within class methods to access the instance’s attributes and methods. The ``self`` parameter is a way for instance methods to refer to the specific object that invoked the method.

#### Key Points:
**- Instance Reference:** ``self`` allows access to the instance's own data (attributes) and methods.
**- Explicit in Python:** Unlike some other languages (like Java or C++), where ``this`` is implicit, Python requires you to explicitly define and use ``self``.
**- Convention:** ``self`` is not a keyword in Python; it's just a convention. You could technically name it anything, but using ``self`` is the standard and makes the code readable.
```python
class MyClass:
    def __init__(self, value):
        self.value = value  # 'self.value' is the instance's attribute

    def print_value(self):
        print(self.value)  # 'self' refers to the current instance

# Creating an instance of MyClass
obj = MyClass(10)
obj.print_value()  # Output: 10
```
</details>
<details>
<summary>What is a method</summary>

### A Method
A **method** in Python is a function that is defined inside a class and is associated with an instance of that class. Methods allow objects (instances of a class) to perform actions or behaviors that are specific to their type.

#### Types of Methods:
##### 1. Instance Methods:
These are the most common methods. They operate on the instance of the class, and ``self`` refers to the specific instance calling the method.
```python
class Dog:
    def bark(self):  # Instance method
        print("Woof!")

my_dog = Dog()
my_dog.bark()  # Output: Woof!
```
##### 2.Class Methods:
Defined with the ``@classmethod`` decorator, these methods operate on the class itself, not on instances of the class. They take ``cls`` as the first parameter, which refers to the class.
```python
class Dog:
    species = "Canine"
    
    @classmethod
    def print_species(cls):  # Class method
        print(cls.species)

Dog.print_species()  # Output: Canine
```
##### 3. Static Methods:
Defined with the ``@staticmethod`` decorator, these methods do not operate on the instance or the class. They don’t take ``self`` or ``cls`` as a parameter. They are utility methods related to the class.
```python
class Math:
    @staticmethod
    def add(a, b):  # Static method
        return a + b

result = Math.add(5, 3)  # Output: 8
```
#### Key Points:
**- Instance Methods:** Can modify the object’s state (its attributes) and have access to both the instance (self) and the class.
**- Class Methods:** Can modify class-level attributes, but not the instance-level ones.
**- Static Methods:** Cannot modify class or instance attributes; they are standalone methods within a class.
</details>
<details>
<summary>What is the special ``__init__`` method and how to use it</summary>

### `__init__` method

The special ``__init__`` method in Python is a constructor method that is automatically called when a new instance of a class is created. It initializes the attributes of the object and sets up any necessary state. The __init__ method allows you to pass arguments during the creation of an object to customize its initial state.

#### Key Points:
- The ``__init__`` method is used to initialize an object's attributes when it is created.
- It is not technically a constructor, but it behaves like one by setting up an object’s initial state.
- The first argument of ``__init__`` is always self, which refers to the instance being created.
- It does not return anything (it should not return any value).
#### How to Use the ``__init__`` Method:
```python
class Car:
    def __init__(self, make, model, year):  # __init__ method to initialize the object
        self.make = make  # Initializing the 'make' attribute
        self.model = model  # Initializing the 'model' attribute
        self.year = year  # Initializing the 'year' attribute

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

# Creating an object (instance) of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Accessing object's attributes and methods
my_car.display_info()  # Output: 2020 Toyota Corolla
```

</details>
<details>
<summary>What is Data Abstraction, Data Encapsulation, and Information Hiding</summary>

### Data Abstraction, Data Encapsulation, and Information Hiding
#### 1. Data Abstraction:
Data Abstraction refers to the concept of simplifying complex reality by modeling classes based on essential properties and behaviors, while hiding unnecessary details. It focuses on **what** an object does, rather than **how** it achieves it.

**Purpose:** It allows users to interact with an object at a high level without needing to understand its internal workings.
Example: A car has methods like drive(), stop(), and accelerate(). The user doesn’t need to know how the engine, fuel system, or transmission works to drive the car.
```python
class Car:
    def drive(self):
        print("Car is driving")

my_car = Car()
my_car.drive()  # Abstracted method, no need to know how the car drives internally
```
#### 2. Data Encapsulation:
Data Encapsulation is the technique of bundling the data (attributes) and the methods (functions) that operate on the data into a single unit or class. It also restricts direct access to some of the object’s components to protect its integrity.

**Purpose:** To prevent external interference and misuse of data, and to control how data is accessed or modified.
Example: In a class, data is encapsulated, meaning the internal state (attributes) can only be changed through methods.
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Encapsulated access to balance
```
#### 3. Information Hiding:
Information Hiding is a key principle of encapsulation where the internal implementation details of a class (such as attributes or helper methods) are hidden from the outside world. It ensures that certain parts of an object are inaccessible, providing only necessary interfaces to interact with it.

**Purpose:** To hide implementation complexity and prevent external code from depending on internal details that might change.
Example: Using private or protected attributes in a class to hide data from being accessed directly.
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Hidden information (private)

    def get_salary(self):
        return self.__salary  # Public method to access hidden information

emp = Employee("John", 50000)
print(emp.get_salary())  # Only accessible through the public method
# print(emp.__salary)  # This would raise an error due to information hiding
```
#### Summary:
**- Data Abstraction:** Focuses on exposing only essential features and hiding unnecessary details. It defines what an object does.
**- Data Encapsulation:** Combines data and methods into a class and restricts access to modify internal state directly. It ensures data protection.
**- Information Hiding:** Hides internal implementation details from the outside world, exposing only what is necessary for interaction.
</details>
<details>
<summary>What is a property</summary>

### Property
In Python, a **property** is a special kind of attribute that allows you to control access to instance variables (attributes) using getter, setter, and deleter methods, while still allowing you to use them as if they were simple attributes. The ``property`` function or decorator enables you to create managed attributes, so you can add logic (e.g., validation) when getting or setting values.

#### Key Concepts of Properties:
**- Getter:** Allows you to retrieve the value of an attribute.
**- Setter:** Allows you to modify the value of an attribute, with the option to add validation or other logic.
**- Deleter:** Allows you to delete an attribute, if necessary.

Properties are a way to encapsulate data and control how an attribute is accessed or modified without changing the way the attribute is accessed by users of your class (they still access it like a regular attribute).

#### Creating a Property
There are two main ways to create properties:
1. Using the ``property()`` function.
2. Using the ``@property`` decorator (recommended and more common).
**Example using @property:**
```python
class Person:
    def __init__(self, name):
        self._name = name  # The leading underscore indicates a "protected" variable

    # Getter method
    @property
    def name(self):
        return self._name

    # Setter method
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value

    # Deleter method (optional)
    @name.deleter
    def name(self):
        print("Deleting name...")
        del self._name

# Using the class
person = Person("Alice")
print(person.name)  # Accesses the name via the getter

person.name = "Bob"  # Sets the name via the setter
print(person.name)

# Trying to set an invalid value
# person.name = 123  # Raises ValueError: Name must be a string

del person.name  # Deletes the name attribute via the deleter
```
**Output:**
```
Alice
Bob
Deleting name...
```
#### Benefits of Properties:
**- Encapsulation:** You can control how an attribute is accessed or modified.
**- Flexibility:** You can change internal implementation details (like adding validation) without changing the public interface of your class.
**- Cleaner Code:** Users of your class can still use attributes as if they were accessing them directly (without having to call explicit getter/setter methods).

#### ``property()`` function
The ``property()`` function in Python is a built-in way to create properties in classes. It allows you to define a managed attribute with getter, setter, and deleter methods.

The basic syntax of property() is: `property(fget=None, fset=None, fdel=None, doc=None)`
- fget: Function for getting the value (getter).
- fset: Function for setting the value (setter).
- fdel: Function for deleting the value (deleter).
- doc: Optional documentation string (docstring).

##### Example Using property()
```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Getter for age
    def get_age(self):
        return self._age

    # Setter for age
    def set_age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative.")
        self._age = value

    # Deleter for age
    def del_age(self):
        del self._age

    # Create property object
    age = property(get_age, set_age, del_age, "Person's age")

# Example usage
person = Person("Alice", 30)
print(person.age)    # Calls get_age() -> Output: 30

person.age = 35      # Calls set_age() -> Sets age to 35
print(person.age)    # Output: 35

del person.age       # Calls del_age() -> Deletes the _age attribute
```

``property()``: Combines these three methods (``get_age``, ``set_age``, ``del_age``) into a single property called ``age``.
The ``age`` property behaves like an attribute but internally uses getter, setter, and deleter functions.

**Output:**
```
30
35
```
##### Equivalent Example Using Decorators:
This can also be written more concisely using decorators:
```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative.")
        self._age = value

    @age.deleter
    def age(self):
        del self._age
```
</details>
<details>
<summary>How to dynamically create arbitrary new attributes for existing instances of a class</summary>

### Dynamically Adding New Attributes
In Python, you can dynamically create new attributes for existing instances of a class by directly assigning values to those attributes using dot notation. Python allows you to add new attributes to objects at runtime because it is highly dynamic.

#### Example of Dynamically Adding New Attributes:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an instance of Person
person = Person("Alice", 30)

# Dynamically add a new attribute 'gender' to the existing 'person' instance
person.gender = "Female"

# Dynamically add a new attribute 'email'
person.email = "alice@example.com"

# Access the newly added attributes
print(person.name)   # Output: Alice
print(person.age)    # Output: 30
print(person.gender) # Output: Female
print(person.email)  # Output: alice@example.com
```
##### Explanation:
- After creating the ``person`` instance of the ``Person`` class, we dynamically added two new attributes ``gender`` and ``email``.
- These attributes didn’t exist in the class definition but were added at runtime.

#### Using ``setattr`` Function to Dynamically Add Attributes:
In addition to dot notation, you can use Python’s built-in ``setattr()`` function to dynamically assign attributes. This function takes three arguments: the object, the name of the attribute (as a string), and the value to assign.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an instance of Person
person = Person("Bob", 25)

# Dynamically add new attributes using setattr()
setattr(person, 'country', 'USA')
setattr(person, 'phone', '123-456-7890')

# Access the dynamically added attributes
print(person.country)  # Output: USA
print(person.phone)    # Output: 123-456-7890
```
**Explanation:**
``setattr(object, attribute_name, value)``: This function is a more flexible way to add or modify attributes dynamically, especially when the attribute name is stored in a variable.
**Use Case:**
Dynamically adding attributes is useful when you don’t know beforehand what attributes an object will need, such as when dealing with data that might vary in structure or external inputs where additional fields may be added at runtime.

**Important Note:**
This behavior is true for objects that have a ``__dict__`` attribute, meaning instances of user-defined classes can accept dynamic attributes. However, if a class defines ``__slots__``, it restricts adding arbitrary new attributes.
#### Key difference between Dot Notation and `setattr()` function

| Feature                | Dot Notation                     | `setattr()` Function            |
|------------------------|----------------------------------|----------------------------------|
| **Syntax**             | `object.attribute = value`       | `setattr(object, 'attribute', value)` |
| **Use Case**           | Directly assigning a value to an attribute | Dynamically assigning an attribute using a string |
| **Error Handling**     | Raises `AttributeError` if the attribute does not exist (when accessed) | Raises `AttributeError` if the attribute name is invalid or if the object does not have a `__dict__` |
| **Readability**        | Generally more readable and concise | Can be less readable, especially with many attributes |
| **Dynamic Attributes** | Can add or modify existing attributes | Primarily used for adding or modifying attributes dynamically using strings |
| **Example**            | `person.name = "Alice"`         | `setattr(person, 'name', "Alice")` |

**Summary:**
- **Dot notation** is straightforward and preferred for accessing or modifying attributes when the attribute names are known.
- ``setattr()`` is useful when you need to dynamically set attributes, especially when attribute names are generated or stored as strings.
</details>
<details>
<summary>How to bind attributes to object and classes</summary>

### Binding attributes to objects and classes

#### 1. Binding Attributes to an Object (Instance)
**1.2. Using the Constructor (``__init__`` method):** You can bind attributes to an instance of a class when the object is created by defining them in the ``__init__`` method.
```python
class Person:
    def __init__(self, name, age):
        self.name = name  # Bind 'name' attribute
        self.age = age    # Bind 'age' attribute

person = Person("Alice", 30)
print(person.name)  # Output: Alice
```
**1.2. Direct Assignment:** You can bind attributes to an instance after it has been created.
```python
person.gender = "Female"  # Bind 'gender' attribute
print(person.gender)  # Output: Female
```
**1.3. Using ``setattr()``:** You can use the ``setattr()`` function to bind attributes dynamically.
```python
setattr(person, 'city', 'New York')  # Bind 'city' attribute
print(person.city)  # Output: New York
```
#### 2. Binding Attributes to a Class
**2.1. Class Attributes:** You can define attributes that are shared by all instances of a class by assigning them directly within the class body.
```python
class Person:
    species = "Homo sapiens"  # Class attribute

print(Person.species)  # Output: Homo sapiens
```
**2.2. Using Class Methods:** You can bind attributes through class methods, allowing you to modify class-level data.
```python
class Person:
    species = "Homo sapiens"

    @classmethod
    def set_species(cls, new_species):
        cls.species = new_species

Person.set_species("Homo neanderthalensis")
print(Person.species)  # Output: Homo neanderthalensis
```
**2.3. Using ``setattr()``:** You can also use ``setattr()`` to dynamically bind attributes to a class.
```python
setattr(Person, 'age_limit', 120)  # Bind 'age_limit' class attribute
print(Person.age_limit)  # Output: 120
```
#### Summary
**- Instance Attributes:** Use the ``__init__`` method for initialization, direct assignment, or ``setattr() ``for dynamic binding.
**- Class Attributes:** Define them directly in the class body, use class methods for modification, or ``setattr()`` for dynamic binding.
</details>
<details>
<summary>What is the ``__dict__`` of a class and/or instance of a class and what does it contain</summary>

### The ``__dict__`` of a class and/or instance of a class
In Python, the ``__dict__`` attribute is a special attribute that stores the writable attributes of an object (both instances and classes) in a dictionary format.
#### ``__dict__`` of an Instance
**Definition:** For an instance of a class, ``__dict__`` is a dictionary that contains all the instance attributes and their corresponding values.
**Contents:** It includes attributes that have been defined in the ``__init__`` method, as well as any attributes added to the instance after its creation.
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)
person.city = "New York"  # Adding an attribute dynamically

print(person.__dict__)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}
```
#### ``__dict__`` of a Class
**Definition:** For a class, ``__dict__`` is a dictionary that contains the class attributes and methods.
**Contents:** It includes all the attributes defined in the class body, including class-level attributes, methods, and any other elements associated with the class.
```python
class Person:
    species = "Homo sapiens"

    def greet(self):
        print("Hello!")

print(Person.__dict__)
```
**Output:**
```python
{'__module__': '__main__', 'species': 'Homo sapiens', 'greet': <function Person.greet at 0x...>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}
```
</details>
<details>
<summary>How does Python find the attributes of an object or class</summary>

### Attribute Lookup Process
#### 1. Instance Dictionary (``__dict__``):
Python first checks if the attribute is present in the instance's ``__dict__``. If the attribute is found, its value is returned.
#### 2. Class Dictionary (``__dict__``):
If the attribute is not found in the instance, Python then checks the class of the instance. It looks in the class's ``__dict__`` for the attribute.
#### 3. Base Classes:
If the attribute is still not found, Python continues to check the base classes (parent classes) in the order they are defined (this is known as the Method Resolution Order or MRO). It searches each base class's ``__dict__`` for the attribute.
#### 4. Stop Lookup:
The search continues up the inheritance hierarchy until the attribute is found or until there are no more classes to check. If the attribute is not found in the entire hierarchy, Python raises an ``AttributeError``.
**Example**
```python
class Parent:
    def __init__(self):
        self.parent_attr = "I am a parent attribute"

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child_attr = "I am a child attribute"

child_instance = Child()

# Accessing attributes
print(child_instance.child_attr)  # Found in instance's __dict__
print(child_instance.parent_attr)  # Found in Parent's __dict__
```
**Summary**
- **Order of Lookup:**
    1. Instance’s ``__dict__``
    2. Class’s ``__dict__``
    3. Base classes (in MRO order)
- **Result:** If the attribute is found, its value is returned; if not, an ``AttributeError`` is raised. This lookup mechanism allows for a flexible and dynamic attribute access in Python.
</details>
<details>
<summary>How to use the getattr function</summary>

### ``getattr()`` function
The ``getattr()`` function in Python is used to retrieve the value of an attribute from an object dynamically. It allows you to access an attribute using its name as a string. This can be especially useful when you want to access attributes whose names may not be known until runtime.

**Syntax :** `getattr(object, name[, default])`
    **- object:** The object from which you want to retrieve the attribute.
    **- name:** A string that represents the name of the attribute you want to access.
    **- default** (optional): A value to return if the attribute does not exist. If this argument is not provided and the attribute is not found, an ``AttributeError`` is raised.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)

# Accessing attributes using getattr
name = getattr(person, "name")
age = getattr(person, "age")

print(name)  # Output: Alice
print(age)   # Output: 30

# Using Default Value
# If you try to access an attribute that doesn't exist, getattr() can return a default value instead of raising an error:

# Attempting to access a non-existing attribute
hobby = getattr(person, "hobby", "No hobby defined")
print(hobby)  # Output: No hobby defined
```
#### Error Handling
You can also use ``getattr()`` without a default value and handle the potential ``AttributeError``:
```python
try:
    hobby = getattr(person, "hobby")  # This will raise an error
except AttributeError:
    hobby = "No hobby defined"

print(hobby)  # Output: No hobby defined
```
</details>

## Tasks
### 0. My first square
Write an empty class ``Square`` that defines a square:
You are not allowed to import any module
```bash
$ cat 0-main.py
#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

$ ./0-main.py
<class '0-square.Square'>
{}
```
### 1. Square with size
Write a class ``Square`` that defines a square by: (based on ``0-square.py``)
- Private instance attribute: ``size``
- Instantiation with ``size`` (no type/value verification)
- You are not allowed to import any module

*Why ``size`` is private attribute?*
The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. One way to have the control is to keep it privately. You will see in next tasks how to get, update and validate the size value.
```bash
$ cat 1-main.py
#!/usr/bin/python3
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)

$ ./1-main.py
<class '1-square.Square'>
{'_Square__size': 3}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
```
### 2. Size validation
Write a class ``Square`` that defines a square by: (based on ``1-square.py``)
- Private instance attribute: ``size``
- Instantiation with optional ``size``: ``def __init__(self, size=0):``
    + ``size`` must be an integer, otherwise raise a ``TypeError`` exception with the message ``size must be an integer``
    + if ``size`` is less than ``0``, raise a ``ValueError`` exception with the message ``size must be >= 0``
- You are not allowed to import any module
```bash
$ cat 2-main.py
#!/usr/bin/python3
Square = __import__('2-square').Square

my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)

$ ./2-main.py
<class '2-square.Square'>
{'_Square__size': 3}
<class '2-square.Square'>
{'_Square__size': 0}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
size must be an integer
size must be >= 0
```
### 3. Area of a square
Write a class ``Square`` that defines a square by: (based on ``2-square.py``)
- Private instance attribute: ``size``
- Instantiation with optional ``size``: ``def __init__(self, size=0):``
    + ``size`` must be an integer, otherwise raise a ``TypeError`` exception with the message ``size must be an integer``
    + if ``size`` is less than ``0``, raise a ``ValueError`` exception with the message ``size must be >= 0``
- Public instance method: ``def area(self):`` that returns the current square area
- You are not allowed to import any module
```bash
$ cat 3-main.py
#!/usr/bin/python3
Square = __import__('3-square').Square

my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))

$ ./3-main.py
Area: 9
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
Area: 25
```
### 4. Access and update private attribute
Write a class ``Square`` that defines a square by: (based on ``3-square.py``)
- Private instance attribute: ``size``:
    + property ``def size(self):`` to retrieve it
    + property setter ``def size(self, value):`` to set it:
        - ``size`` must be an integer, otherwise raise a ``TypeError`` exception with the message ``size must be an integer``
        - if ``size`` is less than ``0``, raise a ``ValueError`` exception with the message ``size must be >= 0``
- Instantiation with optional ``size``: ``def __init__(self, size=0):``
- Public instance method: ``def area(self):`` that returns the current square area
- You are not allowed to import any module

*Why a getter and setter?*

Reminder: ``size`` is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc. Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.
```bash
$ cat 4-main.py
#!/usr/bin/python3
Square = __import__('4-square').Square

my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)

$ ./4-main.py
Area: 7921 for size: 89
Area: 9 for size: 3
size must be an integer
```
### 5. Printing a square
Write a class ``Square`` that defines a square by: (based on ``4-square.py``)
- Private instance attribute: ``size``:
    + property ``def size(self):`` to retrieve it
    + property setter ``def size(self, value):`` to set it:
        - ``size`` must be an integer, otherwise raise a ``TypeError`` exception with the message ``size must be an integer``
        - if ``size`` is less than ``0``, raise a ``ValueError`` exception with the message ``size must be >= 0``
- Instantiation with optional ``size``: ``def __init__(self, size=0):``
- Public instance method: ``def area(self):`` that returns the current square area
- Public instance method: ``def my_print(self):`` that prints in stdout the square with the character ``#``:
    + if ``size`` is equal to ``0``, print an empty line
- You are not allowed to import any module
```bash
$ cat 5-main.py
#!/usr/bin/python3
Square = __import__('5-square').Square

my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")

$ ./5-main.py
###
###
###
--
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
--

--
```
### 6. Coordinates of a square
Write a class ``Square`` that defines a square by: (based on ``5-square.py``)
- Private instance attribute: ``size``:
    + property ``def size(self):`` to retrieve it
    + property setter ``def size(self, value):`` to set it:
        - ``size`` must be an integer, otherwise raise a ``TypeError`` exception with the message ``size must be an integer``
        - if ``size`` is less than ``0``, raise a ``ValueError`` exception with the ``message size must be >= 0``
- Private instance attribute: ``position``:
    + property ``def position(self):`` to retrieve it
    + property setter ``def position(self, value):`` to set it:
        - ``position`` must be a tuple of 2 positive integers, otherwise raise a ``TypeError`` exception with the message ``position must be a tuple of 2 positive integers``
- Instantiation with optional ``size`` and optional ``position``: ``def __init__(self, size=0, position=(0, 0)):``
- Public instance method: ``def area(self):`` that returns the current square area
- Public instance method: ``def my_print(self):`` that prints in stdout the square with the character ``#``:
    + if ``size`` is equal to ``0``, print an empty line
    + ``position`` should be use by using space - **Don’t fill lines by spaces** when ``position[1] > 0``
- You are not allowed to import any module
```bash
$ cat 6-main.py
#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")

$ ./6-main.py | tr " " "_" | cat -e
###$
###$
###$
--$
$
_###$
_###$
_###$
--$
___###$
___###$
___###$
--$
```
### 7. Singly linked list
Write a class ``Node`` that defines a node of a singly linked list by:
- Private instance attribute: ``data``:
    + property ``def data(self):`` to retrieve it
    + property setter ``def data(self, value):`` to set it:
        - ``data`` must be an integer, otherwise raise a ``TypeError`` exception with the message ``data must be an integer``
- Private instance attribute: ``next_node``:
    + property ``def next_node(self):`` to retrieve it
    + property setter ``def next_node(self, value):`` to set it:
        - ``next_node`` can be ``None`` or must be a ``Node``, otherwise raise a ``TypeError`` exception with the message ``next_node must be a Node object``
- Instantiation with ``data`` and ``next_node``: ``def __init__(self, data, next_node=None):``

And, write a class ``SinglyLinkedList`` that defines a singly linked list by:
- Private instance attribute: ``head`` (no setter or getter)
- Simple instantiation: ``def __init__(self):``
- Should be printable:
    + print the entire list in stdout
    + one node number by line
- Public instance method: ``def sorted_insert(self, value):`` that inserts a new ``Node`` into the correct sorted position in the list (increasing order)
- You are not allowed to import any module
```bash
$ cat 100-main.py
#!/usr/bin/python3
SinglyLinkedList = __import__('100-singly_linked_list').SinglyLinkedList

sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)

$ ./100-main.py
-4
-3
1
2
3
3
4
5
5
10
12
```
### 8. Print Square instance
Write a class ``Square`` that defines a square by: (based on ``6-square.py``)
- Private instance attribute: ``size``:
    + property ``def size(self):`` to retrieve it
    + property setter ``def size(self, value):`` to set it:
        - ``size`` must be an integer, otherwise raise a ``TypeError`` exception with the message ``size must be an integer``
        - if ``size`` is less than ``0``, raise a ``ValueError`` exception with the message ``size must be >= 0``
- Private instance attribute: ``position``:
    + property ``def position(self):`` to retrieve it
    + property setter ``def position(self, value):`` to set it:
        - ``position`` must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message `position must be a tuple of 2 positive integer`
- Instantiation with optional ``size`` and optional ``position``: ``def __init__(self, size=0, position=(0, 0)):``
- Public instance method: ``def area(self):`` that returns the current square area
- Public instance method: ``def my_print(self):`` that prints in stdout the square with the character ``#``:
    + if ``size`` is equal to ``0``, print an empty line
    + ``position`` should be use by using space
- Printing a ``Square`` instance should have the same behavior as ``my_print()``
- You are not allowed to import any module
```bash
$ cat 101-main.py
#!/usr/bin/python3
Square = __import__('101-square').Square

my_square = Square(5, (0, 0))
print(my_square)

print("--")

my_square = Square(5, (4, 1))
print(my_square)

$ ./101-main.py | tr " " "_" | cat -e
#####$
#####$
#####$
#####$
#####$
--$
$
____#####$
____#####$
____#####$
____#####$
____#####$
```
### 9. Compare 2 squares
Write a class ``Square`` that defines a square by: (based on ``4-square.py``)
- Private instance attribute: ``size``:
    + property ``def size(self):`` to retrieve it
    + property setter ``def size(self, value):`` to set it:
        - ``size`` must be a number (float or integer), otherwise raise a ``TypeError`` exception with the message ``size must be a number``
        - if ``size`` is less than ``0``, raise a ``ValueError`` exception with the message ``size must be >= 0``
- Instantiation with ``size``: ``def __init__(self, size=0):``
- Public instance method: ``def area(self):`` that returns the current square area
- ``Square`` instance can answer to comparators: ``==``, ``!=``, ``>``, ``>=``, ``<`` and ``<=`` based on the square area
- You are not allowed to import any module
```bash
$ cat 102-main.py
#!/usr/bin/python3
Square = __import__('102-square').Square

s_5 = Square(5)
s_6 = Square(6)

if s_5 < s_6:
    print("Square 5 < Square 6")
if s_5 <= s_6:
    print("Square 5 <= Square 6")
if s_5 == s_6:
    print("Square 5 == Square 6")
if s_5 != s_6:
    print("Square 5 != Square 6")
if s_5 > s_6:
    print("Square 5 > Square 6")
if s_5 >= s_6:
    print("Square 5 >= Square 6")

$ ./102-main.py
Square 5 < Square 6
Square 5 <= Square 6
Square 5 != Square 6
```
### 10. ByteCode -> Python #5
Write the Python class ``MagicClass`` that does exactly the same as the following Python bytecode:
```
Disassembly of __init__:
 10           0 LOAD_CONST               1 (0)
              3 LOAD_FAST                0 (self)
              6 STORE_ATTR               0 (_MagicClass__radius)

 11           9 LOAD_GLOBAL              1 (type)
             12 LOAD_FAST                1 (radius)
             15 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             18 LOAD_GLOBAL              2 (int)
             21 COMPARE_OP               9 (is not)
             24 POP_JUMP_IF_FALSE       60
             27 LOAD_GLOBAL              1 (type)
             30 LOAD_FAST                1 (radius)
             33 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             36 LOAD_GLOBAL              3 (float)
             39 COMPARE_OP               9 (is not)
             42 POP_JUMP_IF_FALSE       60

 12          45 LOAD_GLOBAL              4 (TypeError)
             48 LOAD_CONST               2 ('radius must be a number')
             51 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             54 RAISE_VARARGS            1
             57 JUMP_FORWARD             0 (to 60)

 13     >>   60 LOAD_FAST                1 (radius)
             63 LOAD_FAST                0 (self)
             66 STORE_ATTR               0 (_MagicClass__radius)
             69 LOAD_CONST               3 (None)
             72 RETURN_VALUE

Disassembly of area:
 17           0 LOAD_FAST                0 (self)
              3 LOAD_ATTR                0 (_MagicClass__radius)
              6 LOAD_CONST               1 (2)
              9 BINARY_POWER
             10 LOAD_GLOBAL              1 (math)
             13 LOAD_ATTR                2 (pi)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE

Disassembly of circumference:
 21           0 LOAD_CONST               1 (2)
              3 LOAD_GLOBAL              0 (math)
              6 LOAD_ATTR                1 (pi)
              9 BINARY_MULTIPLY
             10 LOAD_FAST                0 (self)
             13 LOAD_ATTR                2 (_MagicClass__radius)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE
```
Tip: [Python bytecode](https://docs.python.org/3.4/library/dis.html)