# 0x09. Python - Everything is object
## Resources
- [9.10. Objects and values](https://www.openbookproject.net/thinkcs/python/english2e/ch09.html#objects-and-values)
- [9.11. Aliasing](https://www.openbookproject.net/thinkcs/python/english2e/ch09.html#aliasing)
- [Immutable vs mutable types](https://stackoverflow.com/questions/8056130/immutable-vs-mutable-types)
- [Mutation](https://www.composingprograms.com/pages/24-mutable-data.html) (Only this chapter)
- [9.12. Cloning lists](https://www.openbookproject.net/thinkcs/python/english2e/ch09.html#cloning-lists)
- [Python tuples: immutable but potentially changing](https://www.oreilly.com/radar/)

## Learning Objectives
<details>
<summary>What is the difference between immutable object and mutable object</summary>

### Immutable vs. Mutable
In Python, the main difference between **mutable** and **immutable** objects lies in whether or not their internal state (data) can be changed after they are created.

#### Mutable Objects
**Mutable objects** can be changed after their creation. This means that elements or values within the object can be updated, added, or removed.
Common examples of mutable objects include:
- ``list``
- ``dict``
- ``set``
- ``bytearray``
```python
my_list = [1, 2, 3]
my_list[0] = 10  # Modifying the first element
print(my_list)   # Output: [10, 2, 3]
```
In this case, the list is modified **in place** without creating a new object.

#### Immutable Objects
Immutable objects cannot be changed after their creation. If you want to "change" an immutable object, you need to create a new object.
Common examples of immutable objects include:
- ``int``
- ``float``
- ``str``
- ``tuple``
- ``frozenset``
- ``bytes``
```python
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # This would raise a TypeError, since tuples are immutable
new_tuple = (10, 2, 3)  # Creating a new tuple instead
```
#### Key Differences:
##### 1. Internal state:
- Mutable objects: Can change their state or contents without creating a new object.
- Immutable objects: Cannot change their state or contents; if you want to "change" them, you need to create a new object.
##### 2. Memory allocation:
- Mutable objects: When changed, they retain their original memory address.
- Immutable objects: When you try to change them, a new object with a different memory address is created.
##### 3. Efficiency:
- Mutable objects: More efficient for frequent changes because they avoid creating new objects.
- Immutable objects: More stable, especially in concurrent programming, because they don't change unexpectedly.

**Example: Memory Address**
```python
a = 10  # Immutable (int)
b = a
a += 1  # a is now 11, and a new object is created

print(id(a))  # New memory address
print(id(b))  # Original memory address

my_list = [1, 2, 3]  # Mutable (list)
my_list_copy = my_list
my_list[0] = 10

print(id(my_list))  # Same memory address, modified in place
print(id(my_list_copy))  # Same memory address as my_list
```
In the case of ``int`` (immutable), modifying ``a`` creates a new object. For ``list`` (mutable), modifying ``my_list`` changes the object in place.
</details>
<details>
<summary>What is a reference</summary>

### Reference
In programming, a *reference* is a way to access an object stored in memory without directly interacting with the object's data. Instead of working with the actual data itself, you work with a reference that points to the location where the data is stored. Here are some key points about references:

#### Key Points about References:
##### 1. Memory Address:
A reference essentially acts like a pointer to the memory address of an object. When you create a reference to an object, you're not duplicating the object; you're creating a new variable that points to the same memory location.
##### 2. Mutability:
If the object is mutable (like lists, dictionaries, or sets in Python), modifying the object through one reference will reflect in all other references pointing to that object.
##### 3. Immutable Objects:
If the object is immutable (like strings or tuples in Python), you cannot change the object itself, but you can create new objects. Therefore, a reference to an immutable object will always point to the same object unless a new object is created and assigned to that reference.
```python
a = [1, 2, 3]       # 'a' refers to a list object
b = a               # 'b' is now a reference to the same list object as 'a'

b[0] = 10           # Modify the list through 'b'
print(a)           # Output: [10, 2, 3] - 'a' reflects the change
print(b)           # Output: [10, 2, 3]

a = [4, 5, 6]      # Now 'a' refers to a new list object
print(b)           # Output: [10, 2, 3] - 'b' still refers to the original list
```
##### 4. References vs. Values:

In languages like Python, variables do not store the actual data; they store references to the data. This is different from languages like C or C++ where you can explicitly manage memory and use pointers.
</details>
<details>
<summary>Shallow Copy vs. Deep Copy</summary>

### Shallow Copy
**- Definition:** A shallow copy creates a new object, but does not recursively copy objects contained within the original object. Instead, it copies references to the nested objects.
**- Behavior:**
    + The new object is a separate instance but shares references to the original nested objects.
    + Changes made to nested objects in the shallow copy will reflect in the original object, and vice versa.
**- How to Create:** In Python, you can create a shallow copy using the ``copy`` module:
```python
import copy

original_list = [[1, 2, 3], [4, 5, 6]]
shallow_copied_list = copy.copy(original_list)

shallow_copied_list[0][0] = 'X'  # Modify a nested object in the shallow copy
print(original_list)              # Output: [['X', 2, 3], [4, 5, 6]]
print(shallow_copied_list)        # Output: [['X', 2, 3], [4, 5, 6]]
```
### Deep Copy
**- Definition:** A deep copy creates a new object and recursively copies all objects contained within the original object. This means that all nested objects are duplicated.
**- Behavior:** The new object is entirely independent of the original object. Changes made to the deep copy do not affect the original object and vice versa.
**- How to Create:** In Python, you can create a deep copy using the copy module:
```python
import copy

original_list = [[1, 2, 3], [4, 5, 6]]
deep_copied_list = copy.deepcopy(original_list)

deep_copied_list[0][0] = 'X'  # Modify a nested object in the deep copy
print(original_list)           # Output: [[1, 2, 3], [4, 5, 6]]
print(deep_copied_list)       # Output: [['X', 2, 3], [4, 5, 6]]
```
or using slicing
```python
original_list = [1, 2, 3]
shallow_copied_list = original_list[:]
```

</details>
<details>
<summary>What is an alias</summary>

### alias
In programming, an **alias** refers to a secondary name that points to the same object in memory as another variable. When you create an alias for a variable, both the original variable and the alias refer to the same data. This means that changes made through one variable will also reflect in the other because they both point to the same underlying object.
#### 1. Creating an Alias:
An alias is created simply by assigning one variable to another.
```python
original_list = [1, 2, 3]
alias_list = original_list  # alias_list is now an alias for original_list
```
#### 2. Mutability:
If the object being aliased is mutable (like lists or dictionaries), changes made through either variable will affect the same underlying object.
```python
alias_list.append(4)
print(original_list)  # Output: [1, 2, 3, 4] (original_list is affected)
```
#### 3. Immutability:
If the object is immutable (like integers or strings), any operation that changes the value will result in a new object being created, leaving the original object unchanged.
```python
x = 10
y = x  # y is an alias for x
y += 5  # This creates a new integer object, and x remains 10
print(x)  # Output: 10
print(y)  # Output: 15
```
#### 4. Reference Semantics:
- Aliases exemplify reference semantics in programming. Both variables reference the same memory location, leading to shared data.
- This can sometimes lead to unintended side effects if you're not careful about how you manipulate aliased objects.
#### 5. Use Cases:
- Aliases can be useful for creating shorthand references to long or complex variable names.
- In function arguments, mutable types can be aliased to allow functions to modify data structures directly.
</details>
<details>
<summary>How to know if two variables are identical</summary>

### Verify if two variables are identical
In Python, you can check if two variables are identical (i.e., they refer to the same object in memory) using the ``is`` operator. This operator returns ``True`` if both variables point to the same object and ``False`` otherwise.
```python
# Creating two identical lists
list1 = [1, 2, 3]
list2 = list1  # list2 is an alias for list1

# Check if they are identical
print(list1 is list2)  # Output: True

# Creating a new list with the same contents
list3 = [1, 2, 3]

# Check if they are identical
print(list1 is list3)  # Output: False (different objects)

# Check if they are equal in value
print(list1 == list3)  # Output: True (same contents)
```
#### Summary
Use ``is`` to check if two variables are identical (i.e., refer to the same object).
Use ``==`` to check if two variables are equal in value, which does not require them to be the same object in memory.
</details>
<details>
<summary>How does Python pass variables to functions</summary>

### How does Python pass variables to functions
In Python, variables are passed to functions using a mechanism known as **pass-by-object-reference** (or sometimes referred to as **pass-by-assignment**). 
#### 1. Object References
- When you pass a variable to a function, you are passing a reference to the object, not the actual object itself.
- This means that if you modify the object within the function, the changes will be reflected outside the function as well.
#### 2. Mutable vs. Immutable Types
**- Mutable Objects:** If the object is mutable (like lists, dictionaries, sets, etc.), modifications made to the object inside the function will affect the original object outside the function.
```python
def modify_list(lst):
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 4]
```
**- Immutable Objects:** If the object is immutable (like integers, strings, tuples, etc.), any modifications will create a new object instead of changing the original. Therefore, the original object remains unchanged outside the function.
```python
def modify_integer(n):
    n += 1

my_number = 5
modify_integer(my_number)
print(my_number)  # Output: 5
```
#### 3. Function Parameters
Function parameters can accept positional arguments, keyword arguments, and default values, but all are treated in the same manner regarding how references are passed.
#### Summary
Python uses pass-by-object-reference, meaning it passes references to the objects, allowing changes to mutable objects but creating new objects for immutable ones.
</details>

## Tasks
### 0. Who am I?
What function would you use to get the type of an object?
Write the name of the function in the file, without ``()``.

### 1. Where are you?
How do you get the variable identifier (which is the memory address in the CPython implementation)?
Write the name of the function in the file, without ``()``.

### 2. Right count
In the following code, do ``a`` and ``b`` point to the same object? Answer with ``Yes`` or ``No``.
```python
>>> a = 89
>>> b = 100
```

### 3. Right count =
In the following code, do ``a`` and ``b`` point to the same object? Answer with ``Yes`` or ``No``.
```python
>>> a = 89
>>> b = 89
```

### 4. Right count =
In the following code, do ``a`` and ``b`` point to the same object? Answer with ``Yes`` or ``No``.
```python
>>> a = 89
>>> b = a
```

### 5. Right count =+
In the following code, do ``a`` and ``b`` point to the same object? Answer with ``Yes`` or ``No``.
```python
>>> a = 89
>>> b = a + 1
```
 
### 6. Is equal
What do these 3 lines print?
```python
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```

### 7. Is the same
What do these 3 lines print?
```python
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```

### 8. Is really equal
What do these 3 lines print?
```python
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```
 
### 9. Is really the same
What do these 3 lines print?
```python
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```
### 10. And with a list, is it equal
What do these 3 lines print?
```python
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```
### 11. And with a list, is it the same
What do these 3 lines print?
```python
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```
### 12. And with a list, is it really equal
What do these 3 lines print?
```python
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```
### 13. And with a list, is it really the same
What do these 3 lines print?
```python
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```
### 14. List append
What does this script print?
```python
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```
### 15. List add
What does this script print?
```python
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```
### 16. Integer incrementation
What does this script print?
```python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```
### 17. List incrementation
What does this script print?
```python
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```
### 18. List assignation
What does this script print?
```python
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```
### 19. Copy a list object
Write a function ``def copy_list(l):`` that returns a **copy** of a list.
- The input list can contain any type of objects
- Your file should be maximum 3-line long (no documentation needed)
- You are not allowed to import any module
```bash
$ cat 19-main.py
#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)

$ ./19-main.py
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
True
False
$ wc -l 19-copy_list.py 
3 19-copy_list.py
```
**No test cases needed**
### 20. Tuple or not?
``a = ()``
Is ``a`` a tuple? Answer with ``Yes`` or ``No``.
### 21. Tuple or not?
``a = (1, 2)``
Is ``a`` a tuple? Answer with ``Yes`` or ``No``.
### 22. Tuple or not?
``a = (1)``
Is ``a`` a tuple? Answer with ``Yes`` or ``No``.
### 23. Tuple or not?
``a = (1, )``
Is ``a`` a tuple? Answer with ``Yes`` or ``No``.

### 24. Who I am?
What does this script print?
```python
a = (1)
b = (1)
a is b
```
### 25. Tuple or not
What does this script print?
```python
a = (1, 2)
b = (1, 2)
a is b
```
### 26. Empty is not empty
What does this script print?
```python
a = ()
b = ()
a is b
```
### 27. Still the same?
```python
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```
Will the last line of this script print ``139926795932424``? Answer with ``Yes`` or ``No``.
### 28. Same or not?
```python
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```
Will the last line of this script print ``139926795932424``? Answer with ``Yes`` or ``No``.
### 29. #pythonic
Write a function ``magic_string()`` that returns a string “BestSchool” n times the number of the iteration (see code):
- Format: see example
- Your file should be maximum 4-line long (no documentation needed)
- You are not allowed to import any module
```bash
$ cat 100-main.py
#!/usr/bin/python3
magic_string = __import__('100-magic_string').magic_string

for i in range(10):
    print(magic_string())

$ ./100-main.py | cat -e
BestSchool$
BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool, BestSchool$
$ wc -l 100-magic_string.py 
4 100-magic_string.py
```
**No test cases needed**
### 30. Low memory cost
Write a class ``LockedClass`` with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called ``first_name``.
You are not allowed to import any module
```bash
$ cat 101-main.py
#!/usr/bin/python3
LockedClass = __import__('101-locked_class').LockedClass

lc = LockedClass()
lc.first_name = "John"
try:
    lc.last_name = "Snow"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

$ ./101-main.py
[AttributeError] 'LockedClass' object has no attribute 'last_name'
```
**No test cases needed**
### 31. int 1/3
```bash
julien@ubuntu:/python3$ cat int.py 
a = 1
b = 1
```
Assuming we are using a CPython implementation of Python3 with default options/configuration:
- How many int objects are created by the execution of the first line of the script? (``103-line1.txt``)
- How many int objects are created by the execution of the second line of the script (``103-line2.txt``)
### 32. int 2/3
```bash
julien@ubuntu:/python3$ cat int.py 
a = 1024
b = 1024
del a
del b
c = 1024
```
Assuming we are using a CPython implementation of Python3 with default options/configuration:
- How many int objects are created by the execution of the first line of the script? (``104-line1.txt``)
- How many int objects are created by the execution of the second line of the script (``104-line2.txt``)
- After the execution of line 3, is the int object pointed by ``a`` deleted? Answer with ``Yes`` or ``No`` (``104-line3.txt``)
- After the execution of line 4, is the int object pointed by ``b`` deleted? Answer with ``Yes`` or ``No`` (``104-line4.txt``)
- How many int objects are created by the execution of the last line of the script (``104-line5.txt``)
### 33. int 3/3
```bash
julien@twix:/tmp/so$ cat int.py 
print("I")
print("Love")
print("Python")
```
Assuming we are using a CPython implementation of Python3 with default options/configuration:
- Before the execution of line 2 (``print("Love")``), how many int objects have been created and are still in memory? (``105-line1.txt``)
- Why? (optional blog post :))
Hint: ``NSMALLPOSINTS``, ``NSMALLNEGINTS``
### 34. Clear strings
```bash
guillaume@ubuntu:/python3$ cat string.py 
a = "SCHL"
b = "SCHL"
del a
del b
c = "SCHL"
```
Assuming we are using a CPython implementation of Python3 with default options/configuration (For answers with numbers use integers, don’t spell out the word):
- How many string objects are created by the execution of the first line of the script? (``106-line1.txt``)
- How many string objects are created by the execution of the second line of the script (``106-line2.txt``)
- After the execution of line 3, is the string object pointed by ``a`` deleted? Answer with ``Yes`` or ``No`` (``106-line3.txt``)
- After the execution of line 4, is the string object pointed by ``b`` deleted? Answer with ``Yes`` or ``No`` (``106-line4.txt``)
- How many string objects are created by the execution of the last line of the script (``106-line5.txt``)