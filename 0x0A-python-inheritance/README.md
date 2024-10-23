# 0x0A. Python - Inheritance
## Resources
- [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [Multiple inheritance](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)
- [Inheritance in Python](https://www.geeksforgeeks.org/inheritance-in-python/)
- [Learn to Program 10 : Inheritance Magic Methods](https://www.youtube.com/watch?v=d8kCdLCi6Lk&ab_channel=DerekBanas)

## Learning Objectives
<details>
<summary>How to list all attributes and methods of a class or instance</summary>

### Attributes and Methods of a class
In Python, you can use the built-in function ``dir()`` to list all the attributes and methods of a class or an instance. The dir() function returns a list of the object's properties, including both attributes and methods (as well as special methods, often called "magic methods" like`` __init__``, ``__str__``, etc.).
```python
class MyClass:
    class_attribute = "I am a class attribute"

    def __init__(self, value):
        self.instance_attribute = value

    def my_method(self):
        return "I am a method"

# Create an instance of MyClass
my_instance = MyClass("Instance value")

# List attributes and methods of the class
print(dir(MyClass))

# List attributes and methods of the instance
print(dir(my_instance))
```
**Output:**
```bash
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'class_attribute', 'my_method']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'class_attribute', 'instance_attribute', 'my_method']
```

**Explanation:**
- ``dir(MyClass)`` lists all the attributes and methods of the class MyClass, including its class-level attributes and methods.
- ``dir(my_instance)`` lists all the attributes and methods of the instance my_instance, including instance-level attributes, class attributes, and methods.

#### ``dir()`` vs ``__dict__``
#### 1. ``dir()``:
**- Purpose:** Returns a list of all attributes and methods (including special methods, inherited methods, and attributes) that an object has access to.
**- Scope:** It shows more than just the user-defined attributes. It includes built-in methods and attributes, like magic methods (``__init__``, ``__str__``, etc.), methods from parent classes (if any), and other properties from the object's class.
**- Output:** A comprehensive list of all accessible names for the object, including instance variables, methods, class variables, and special attributes.
#### 2. ``__dict__``:

**- Purpose:** Returns a dictionary representing the instance's (or class's) namespace, i.e., a mapping of all the instance's attributes (or class attributes if applied to a class).
**- Scope:** It only contains the attributes that are explicitly set on the instance (or class), not inherited methods or special methods.
**- Output:** A dictionary where the keys are the attribute names and the values are the corresponding attribute values.

```python
class MyClass:
    class_var = "class attribute"

    def __init__(self, value):
        self.instance_var = value

    def my_method(self):
        pass

# Create an instance of MyClass
my_instance = MyClass("instance attribute")

# Using dir() on the instance
print(dir(my_instance))

# Using __dict__ on the instance
print(my_instance.__dict__)

# Using __dict__ on the class
print(MyClass.__dict__)
```
**Output:**
```bash
# Output of dir(my_instance)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'class_var', 'instance_var', 'my_method']

# Output of my_instance.__dict__
{'instance_var': 'instance attribute'}

# Output of MyClass.__dict__
{'__module__': '__main__', 'class_var': 'class attribute', '__init__': <function MyClass.__init__ at 0x7fbba0>, 'my_method': <function MyClass.my_method at 0x7fbba0>, '__dict__': <attribute '__dict__' of 'MyClass' objects>, '__weakref__': <attribute '__weakref__' of 'MyClass' objects>, '__doc__': None}
```
Key Points:
- ``dir()``:
    + Provides a **full list** of all attributes and methods, including inherited ones and special methods.
    + Output includes everything an object has access to, such as class variables and methods, magic methods, and instance variables.
- __dict__:
    + **Only shows the attributes** (and methods, if any) that are stored in the instance or class itself.
    + For an **instance**: ``__dict__`` will show the instance-specific attributes (e.g., instance_var).
    + For a **class**: __dict__ will show class-level attributes and methods defined in that class.
</details>
<details>
<summary>When can an instance have new attributes</summary>

### When an instance can have new attributes
#### 1. Inside the Class Definition (e.g., in ``__init__``):
Instance attributes are often added in the class's __init__ method when the object is initialized.
```python
class MyClass:
    def __init__(self, name):
        self.name = name  # Instance attribute added in __init__

obj = MyClass("Alice")
print(obj.name)  # Output: Alice
```
#### 2. Dynamically After Instantiation:
You can add new attributes to an instance dynamically, outside of the class, at runtime by directly assigning them new values.
```python
class MyClass:
    def __init__(self, name):
        self.name = name

obj = MyClass("Alice")
obj.age = 25  # New attribute 'age' added dynamically
print(obj.age)  # Output: 25
```
#### 3. In a Method:
You can also add new attributes to an instance inside any method of the class.
```python
class MyClass:
    def __init__(self, name):
        self.name = name

    def add_attribute(self, attr_name, value):
        setattr(self, attr_name, value)  # Adds a new attribute

obj = MyClass("Alice")
obj.add_attribute("age", 25)  # Add 'age' attribute via method
print(obj.age)  # Output: 25
```
#### 4. Using ``setattr()`` Function:
The built-in ``setattr()`` function allows you to add or modify an attribute dynamically.
```python
class MyClass:
    pass

obj = MyClass()
setattr(obj, 'color', 'blue')  # Adds 'color' attribute dynamically
print(obj.color)  # Output: blue
```
#### Key Points:
**- Flexibility:** Python allows adding new attributes to instances dynamically, making the language flexible for handling additional data without modifying the class definition.
**- Class Attributes vs. Instance Attributes:** New attributes added this way are **instance-specific**. Other instances of the same class won’t have these dynamically added attributes unless they are also added individually.
#### Example of different instances having different attributes:
```python
class MyClass:
    def __init__(self, name):
        self.name = name

obj1 = MyClass("Alice")
obj2 = MyClass("Bob")

obj1.age = 30  # Only obj1 has the 'age' attribute
print(obj1.name, obj1.age)  # Output: Alice 30
print(obj2.name)            # Output: Bob
# print(obj2.age)  # This will raise an AttributeError since obj2 has no 'age' attribute
```
</details>
<details>
<summary>How to inherit class from another</summary>

### Inheritance
#### Basic Syntax:
```python
class ParentClass:
    # Parent class definition
    def __init__(self, value):
        self.value = value

    def display(self):
        return f"Value: {self.value}"

# Subclass definition
class ChildClass(ParentClass):
    def __init__(self, value, additional_value):
        super().__init__(value)  # Call the constructor of the parent class
        self.additional_value = additional_value

    def show_additional(self):
        return f"Additional Value: {self.additional_value}"
```
#### Key Points:
**1. Inheritance:** The ``ChildClass`` inherits from ``ParentClass``. This means ``ChildClass`` can access attributes and methods defined in ``ParentClass``.
**2. Calling the Parent's Constructor:** In the ``__init__`` method of the subclass, you can call the parent's constructor using ``super().__init__(value)``. This initializes the attributes defined in the parent class.
**3. Adding New Methods:** You can also define additional methods in the subclass that are not present in the parent class.
#### ``ParentClass.__init__(self)`` vs. ``super().__init__()``:
Using ``ParentClass.__init__(self)`` directly and ``super().__init__()`` both serve to call the constructor of the parent class in Python, but there are important differences between the two approaches. 
##### 1. Using ``super()``:
```python
class ParentClass:
    def __init__(self, value):
        self.value = value

class ChildClass(ParentClass):
    def __init__(self, value, additional_value):
        super().__init__(value)  # Calls the ParentClass's __init__
        self.additional_value = additional_value
```
**Advantages of Using ``super()``:**
- **Support for Multiple Inheritance:** When using multiple inheritance, ``super()`` follows the **Method Resolution Order (MRO)**. This means it correctly identifies which class's method to call based on the inheritance hierarchy, preventing issues that can arise from direct parent calls.
- **Cleaner Code:** ``super()`` automatically references the next class in the MRO, so it can make the code cleaner and less prone to errors if the class hierarchy changes in the future.
- **Avoiding Hardcoding:** By using ``super()``, you avoid hardcoding the parent class name. This can make your code more maintainable, especially if you decide to change the parent class later.

##### 2. Using ``ParentClass.__init__(self)``:
```python
class ChildClass(ParentClass):
    def __init__(self, value, additional_value):
        ParentClass.__init__(self, value)  # Calls ParentClass's __init__
        self.additional_value = additional_value
```
**Disadvantages of Using Direct Parent Calls:**
**- Not Ideal for Multiple Inheritance:** If ``ChildClass`` inherits from multiple parent classes, using ``ParentClass.__init__(self)`` may lead to problems, as it does not account for the MRO. This can cause issues if other parent classes also have an ``__init__`` method that needs to be called.
**- Coupling to the Parent Class Name:** This approach is more tightly coupled to the specific parent class name. If you change the inheritance or rename the parent class, you would need to update every direct call.

##### Summary of Differences:
- Flexibility: ``super()`` is more flexible, especially with multiple inheritance scenarios. It allows for dynamic method resolution based on the inheritance hierarchy.
- Maintainability: ``super()`` avoids hardcoding the parent class name, making your code easier to maintain.
- MRO Handling: ``super()`` correctly handles MRO, which is crucial in complex inheritance structures.

##### Conclusion:
While both approaches work for single inheritance scenarios, using ``super()`` is generally the preferred method in Python for its flexibility, maintainability, and compatibility with multiple inheritance. It helps you write more robust and adaptable code.
</details>
<details>
<summary>How to define a class with multiple base classes</summary>

### Multiple Inheritance
To define a class with multiple base classes in Python, you can simply list the base classes in parentheses after the class name. This creates a class that inherits from all specified base classes, allowing it to access their methods and attributes.
#### Syntax:
```python
class ChildClass(BaseClass1, BaseClass2, BaseClass3):
    # Class body
```
#### Example:
```python
class Animal:
    def speak(self):
        return "Animal makes a sound."

class Canine:
    def bark(self):
        return "Woof!"

class Feline:
    def meow(self):
        return "Meow!"

# Child class inheriting from Animal, Canine, and Feline
class Dog(Animal, Canine):
    def speak(self):  # Overriding the speak method
        return "Dog barks."

class Cat(Animal, Feline):
    def speak(self):  # Overriding the speak method
        return "Cat meows."

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Call methods from base classes
print(dog.speak())  # Output: Dog barks.
print(dog.bark())   # Output: Woof!
print(cat.speak())  # Output: Cat meows.
print(cat.meow())   # Output: Meow!
```

#### Key Points:
**- Multiple Inheritance:** You can inherit from multiple classes by listing them in parentheses, which allows the child class to access methods and attributes from all specified base classes.
**- Method Resolution Order (MRO):** When using multiple inheritance, be aware of how Python resolves method calls, especially if multiple base classes define the same method. The MRO determines the order in which classes are searched for methods.
**- Overriding Methods:** You can override methods in child classes to provide specific behavior while still being able to access the base class methods.
</details>
<details>
<summary>What is the default class every class inherit from</summary>

### ``object`` class
In Python, every class implicitly inherits from a base class called ``object`` if no other base class is explicitly specified. This means that all classes in Python are part of a hierarchy that ultimately leads back to ``object``.

#### Key Points about the ``object`` Class:
**1. Universal Base Class:** The object class is the most basic built-in class in Python and serves as the foundation for all classes. Whether you create a class without explicitly inheriting from another class or you inherit from another class, all classes derive from ``object``.
**2. New-Style Classes:** In Python 2, there were two types of classes: old-style and new-style. Old-style classes were defined without explicitly inheriting from object, while new-style classes did. In Python 3, all classes are new-style classes, and they automatically inherit from ``object``.
**3. Common Methods:** The ``object`` class provides several built-in methods that all classes inherit, including:
- ``__init__(self, ...):`` The constructor method.
- ``__str__(self):`` Defines the string representation of an object.
- ``__repr__(self):`` Defines the official string representation of an object.
- ``__eq__(self, other):`` Defines equality comparison.
- ``__hash__(self):`` Defines a hash value for instances of the class.

Example:
Here's a simple example demonstrating the inheritance from object:
```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"MyClass with value: {self.value}"

# Create an instance of MyClass
obj = MyClass(10)

# Check the type of the class
print(type(obj))          # Output: <class '__main__.MyClass'>
print(isinstance(obj, object))  # Output: True

# Output the string representation
print(obj)  # Output: MyClass with value: 10
```
</details>
<details>
<summary>How to override a method or attribute inherited from the base class</summary>

### Override a method or attribute inherited from the base class
To override a method or attribute inherited from a base class in Python, you define a method or attribute with the same name in the child (subclass) that you want to customize or replace. When you create an instance of the subclass and call the overridden method or access the overridden attribute, the version in the subclass will be executed instead of the one in the base class.
#### Overriding Methods
**1. Define a Base Class with a Method:** Define a method in the base class that you want to override in the subclass.
**2. Create a Subclass:** In the subclass, define a method with the same name. This will replace the base class's method.
```python
class Animal:
    def speak(self):
        return "Animal makes a sound."

class Dog(Animal):
    def speak(self):  # Overriding the speak method
        return "Dog barks."

class Cat(Animal):
    def speak(self):  # Overriding the speak method
        return "Cat meows."

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Call the overridden methods
print(dog.speak())  # Output: Dog barks.
print(cat.speak())  # Output: Cat meows.
```
#### Overriding Attributes
You can also override attributes inherited from a base class. You do this by defining the attribute in the subclass:
```python
class Vehicle:
    def __init__(self, color):
        self.color = color  # Attribute in the base class

class Car(Vehicle):
    def __init__(self, color, model):
        super().__init__(color)  # Call the parent constructor
        self.model = model       # New attribute for Car
        self.color = "Red"      # Override the inherited color attribute

# Create an instance of Car
my_car = Car("Blue", "Toyota")

# Access attributes
print(my_car.color)  # Output: Red (overridden)
print(my_car.model)  # Output: Toyota
```
#### Important Notes:
**1. Calling the Parent Method:** If you want to use the base class's implementation of the method, you can call it using ``super()``.
```python
class Dog(Animal):
    def speak(self):
        base_sound = super().speak()  # Call the base class method
        return f"{base_sound} but also barks."
```
**2. Using the Same Name:** Ensure that the method or attribute in the subclass has the exact same name as in the base class. This will ensure that the subclass method or attribute overrides the one in the base class.
**3. Accessing Overridden Attributes:** If you override an attribute in the subclass and want to keep the base class's version, you can store it in a different name or access it through the parent class methods.
</details>
<details>
<summary>Which attributes or methods are available by heritage to subclasses</summary>

### Attributes or methods available by heritage to subclasses
In Python, subclasses inherit all **public** and **protected** attributes and methods from their parent (base) classes. However, they do not inherit **private** attributes and methods in the same way.

#### 1. Public Attributes and Methods
- Public attributes and methods are accessible from anywhere, including outside the class and its subclasses.
- These are defined without any leading underscores (``_`` or`` __``).
```python
class Parent:
    def __init__(self):
        self.public_attr = "I am public"

    def public_method(self):
        return "This is a public method"

class Child(Parent):
    def display(self):
        print(self.public_attr)  # Accessible
        print(self.public_method())  # Accessible

child_instance = Child()
child_instance.display()
```
#### 2. Protected Attributes and Methods
- **Protected attributes and methods** are intended to be accessible within the class and its subclasses but are not intended for public access. They are defined with a single leading underscore (``_``).
- While these are accessible from subclasses, the convention is to treat them as non-public.
```python
class Parent:
    def __init__(self):
        self._protected_attr = "I am protected"

    def _protected_method(self):
        return "This is a protected method"

class Child(Parent):
    def display(self):
        print(self._protected_attr)  # Accessible
        print(self._protected_method())  # Accessible

child_instance = Child()
child_instance.display()
```
#### 3. Private Attributes and Methods
- **Private attributes and methods** are intended to be inaccessible from outside the class, including subclasses. They are defined with a double leading underscore (``__``).
- Python uses name mangling to make these attributes and methods private, meaning they cannot be accessed directly from subclasses using the original name. However, they can still be accessed indirectly through their mangled names.
```python
class Parent:
    def __init__(self):
        self.__private_attr = "I am private"

    def __private_method(self):
        return "This is a private method"

class Child(Parent):
    def display(self):
        # print(self.__private_attr)  # This will raise an AttributeError
        print(self._Parent__private_attr)  # Accessing via name mangling

child_instance = Child()
child_instance.display()  # Access private attribute indirectly
```
</details>
<details>
<summary>What are, when and how to use isinstance, issubclass, type and super built-in functions</summary>

### built-in functions ``isinstance()``, ``issubclass()``, ``type()``, and ``super()``
#### 1. ``isinstance()``
``isinstance()`` checks if an object is an instance of a specified class or a tuple of classes.

**How to Use:**
```python
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

# Check if 'dog' is an instance of Dog
print(isinstance(dog, Dog))        # Output: True
# Check if 'dog' is an instance of Animal
print(isinstance(dog, Animal))     # Output: True
# Check if 'dog' is an instance of a tuple of classes
print(isinstance(dog, (Animal, str)))  # Output: True
```
#### 2. ``issubclass()``
``issubclass()`` checks if a class is a subclass of another class or a tuple of classes.

**How to Use:**
```python
class Animal:
    pass

class Dog(Animal):
    pass

# Check if Dog is a subclass of Animal
print(issubclass(Dog, Animal))     # Output: True
# Check if Animal is a subclass of Dog
print(issubclass(Animal, Dog))     # Output: False
# Check against a tuple of classes
print(issubclass(Dog, (Animal, str)))  # Output: True
```
#### 3. ``type()``
``type()`` returns the type of an object. When used with two arguments, it can create a new class dynamically.

``type()`` to check the type of an object. However, be cautious, as using ``type()`` for type checking can be less flexible compared to ``isinstance()`` since it does not consider inheritance.

**How to Use:**
```python
# Check the type of an object
num = 10
print(type(num))                    # Output: <class 'int'>
text = "Hello"
print(type(text))                   # Output: <class 'str'>

# Create a new class dynamically
MyClass = type('MyClass', (object,), {'attr': 42})
instance = MyClass()
print(instance.attr)                # Output: 42
```
#### 4. ``super()``
``super()`` returns a temporary object of the superclass that allows you to call its methods.

Use super() when you want to access methods of a superclass in a subclass, especially during method overriding to ensure that the parent class’s behavior is retained.

**How to Use:**
```python
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return super().speak() + " Woof!"  # Calls the speak method of Animal

# Create an instance of Dog
dog = Dog()
print(dog.speak())  # Output: Animal sound Woof!
```
#### Summary
- ``isinstance(obj, classinfo)``: Use to check if obj is an instance of classinfo or any of its subclasses.
- ``issubclass(subclass, classinfo)``: Use to check if subclass is a subclass of classinfo or any of its superclasses.
- ``type(obj)``: Use to get the type of obj. For dynamic class creation, use ``type(name, bases, dict)``.
- ``super()``: Use to call methods from a superclass in a subclass, particularly when overriding methods to maintain inherited behavior.
</details>

## Tasks
### 0. Lookup
Write a function that returns the list of available attributes and methods of an object:
- Prototype: ``def lookup(obj):``
- Returns a ``list`` object
- You are not allowed to import any module
```bash
$ cat 0-main.py
#!/usr/bin/python3
lookup = __import__('0-lookup').lookup

class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))

$ ./0-main.py
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'my_attr1', 'my_meth']
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
```
**No test cases needed**
 
### 1. My list
Write a class ``MyList`` that inherits from ``list``:
- Public instance method: ``def print_sorted(self):`` that prints the list, but sorted (ascending sort)
- You can assume that all the elements of the list will be of type ``int``
- You are not allowed to import any module
```bash
$ cat 1-main.py
#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)

$ ./1-main.py
[1, 4, 2, 3, 5]
[1, 2, 3, 4, 5]
[1, 4, 2, 3, 5]
```

### 2. Exact same object
Write a function that returns ``True`` if the object is exactly an instance of the specified class ; otherwise ``False``.
- Prototype: ``def is_same_class(obj, a_class):``
- You are not allowed to import any module
```bash
$ cat 2-main.py
#!/usr/bin/python3
is_same_class = __import__('2-is_same_class').is_same_class

a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))

$ ./2-main.py
1 is an instance of the class int
```
**No test cases needed**
 
### 3. Same class or inherit from
Write a function that returns ``True`` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise ``False``.
- Prototype: ``def is_kind_of_class(obj, a_class):``
- You are not allowed to import any module
```bash
$ cat 3-main.py
#!/usr/bin/python3
is_kind_of_class = __import__('3-is_kind_of_class').is_kind_of_class

a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, float.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))

$ ./3-main.py
1 comes from int
1 comes from object
```
**No test cases needed**
 
### 4. Only sub class of
Write a function that returns ``True`` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise ``False``.
- Prototype: ``def inherits_from(obj, a_class):``
- You are not allowed to import any module
```bash
$ cat 4-main.py
#!/usr/bin/python3
inherits_from = __import__('4-inherits_from').inherits_from

a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))

$ ./4-main.py
True inherited from class int
True inherited from class object
```
**No test cases needed**

### 5. Geometry module
Write an empty class ``BaseGeometry``.
You are not allowed to import any module
```bash
$ cat 5-main.py
#!/usr/bin/python3
BaseGeometry = __import__('5-base_geometry').BaseGeometry

bg = BaseGeometry()

print(bg)
print(dir(bg))
print(dir(BaseGeometry))

$ ./5-main.py
<5-base_geometry.BaseGeometry object at 0x7f2050c69208>
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
```
**No test cases needed**

### 6. Improve Geometry
Write a class ``BaseGeometry`` (based on ``5-base_geometry.py``).
- Public instance method: ``def area(self):`` that raises an Exception with the message ``area() is not implemented``
- You are not allowed to import any module
```bash
$ cat 6-main.py
#!/usr/bin/python3
BaseGeometry = __import__('6-base_geometry').BaseGeometry

bg = BaseGeometry()

try:
    print(bg.area())
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

$ ./6-main.py
[Exception] area() is not implemented
```
**No test cases needed**

### 7. Integer validator
Write a class ``BaseGeometry`` (based on ``6-base_geometry.py``).
- Public instance method: ``def area(self):`` that raises an ``Exception`` with the message ``area() is not implemented``
- Public instance method: ``def integer_validator(self, name, value):`` that validates ``value``:
    + you can assume ``name`` is always a string
    + if ``value`` is not an integer: raise a ``TypeError`` exception, with the message ``<name> must be an integer``
    + if ``value`` is less or equal to 0: raise a ``ValueError`` exception with the message ``<name> must be greater than 0``
- You are not allowed to import any module
```bash
$ cat 7-main.py
#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

bg.integer_validator("my_int", 12)
bg.integer_validator("width", 89)

try:
    bg.integer_validator("name", "John")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("age", 0)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    bg.integer_validator("distance", -4)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

$ ./7-main.py
[TypeError] name must be an integer
[ValueError] age must be greater than 0
[ValueError] distance must be greater than 0
```

### 8. Rectangle
Write a class ``Rectangle`` that inherits from ``BaseGeometry`` (``7-base_geometry.py``).
- Instantiation with ``width`` and ``height``: ``def __init__(self, width, height):``
    + ``width`` and ``height`` must be private. No getter or setter
    + ``width`` and ``height`` must be positive integers, validated by ``integer_validator``
```bash
$ cat 8-main.py
#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(dir(r))

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

$ ./8-main.py
<8-rectangle.Rectangle object at 0x7f6f488f7eb8>
['_Rectangle__height', '_Rectangle__width', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'integer_validator']
[AttributeError] 'Rectangle' object has no attribute 'width'
[TypeError] height must be an integer
```
**No test cases needed**

### 9. Full rectangle
Write a class ``Rectangle`` that inherits from ``BaseGeometry`` (``7-base_geometry.py``). (task based on ``8-rectangle.py``)
- Instantiation with width and height: ``def __init__(self, width, height):``:
    + ``width`` and ``height`` must be private. No getter or setter
    + ``width`` and ``height`` must be positive integers validated by ``integer_validator``
- the ``area()`` method must be implemented
- ``print()`` should print, and ``str()`` should return, the following rectangle description: ``[Rectangle] <width>/<height>``
```bash
$ cat 9-main.py
#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(r.area())

$ ./9-main.py
[Rectangle] 3/5
15
```
**No test cases needed**

### 10. Square #1
Write a class ``Square`` that inherits from ``Rectangle`` (``9-rectangle.py``):
- Instantiation with size: ``def __init__(self, size):``:
    + ``size`` must be private. No getter or setter
    + ``size`` must be a positive integer, validated by ``integer_validator``
- the ``area()`` method must be implemented
```bash
$ cat 10-main.py
#!/usr/bin/python3
Square = __import__('10-square').Square

s = Square(13)

print(s)
print(s.area())

$ ./10-main.py
[Rectangle] 13/13
169
```
**No test cases needed**

### 11. Square #2
Write a class ``Square`` that inherits from ``Rectangle`` (``9-rectangle.py``). (task based on ``10-square.py``).
- Instantiation with size: ``def __init__(self, size):``:
    + ``size`` must be private. No getter or setter
    + ``size`` must be a positive integer, validated by ``integer_validator``
- the ``area()`` method must be implemented
- ``print()`` should print, and ``str()`` should return, the square description: ``[Square] <width>/<height>``
```bash
$ cat 11-main.py
#!/usr/bin/python3
Square = __import__('11-square').Square

s = Square(13)

print(s)
print(s.area())

$ ./11-main.py
[Square] 13/13
169
```

### 12. My integer
Write a class ``MyInt`` that inherits from ``int``:
- ``MyInt`` is a rebel. ``MyInt`` has ``== ``and ``!=`` operators inverted
- You are not allowed to import any module
```bash
$ cat 100-main.py
#!/usr/bin/python3
MyInt = __import__('100-my_int').MyInt

my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)

$ ./100-main.py
3
False
True
```
### 13. Can I?
Write a function that adds a new attribute to an object if it’s possible:
- Raise a ``TypeError`` exception, with the message ``can't add new attribute`` if the object can’t have new attribute
- You are not allowed to use ``try/except``
- You are not allowed to import any module
```bash
$ cat 101-main.py
#!/usr/bin/python3
add_attribute = __import__('101-add_attribute').add_attribute

class MyClass():
    pass

mc = MyClass()
add_attribute(mc, "name", "John")
print(mc.name)

try:
    a = "My String"
    add_attribute(a, "name", "Bob")
    print(a.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

$ ./101-main.py
John
[TypeError] can't add new attribute
```