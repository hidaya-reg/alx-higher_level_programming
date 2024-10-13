# 0x04-python-more_data_structures
## Resources
[Data structures](https://docs.python.org/3/tutorial/datastructures.html)
[Lambda, filter, reduce and map](https://python-course.eu/advanced-python/lambda-filter-reduce-map.php)
[Learn to Program 12 Lambda Map Filter Reduce](https://www.youtube.com/watch?v=1GAC6KQUPeg&ab_channel=DerekBanas)
## Learning Objectives
<details>
<summary>What are sets and how to use them</summary>

### Sets in Python
Sets in Python are a built-in data type that represents an unordered collection of unique elements. They are commonly used for membership testing, eliminating duplicate entries, and performing mathematical set operations like union, intersection, and difference.

#### Characteristics of Sets
- **Unordered:** The elements in a set do not have a defined order, and they cannot be accessed by index.
- **Unique Elements:** A set cannot contain duplicate elements. If you try to add a duplicate, it will be ignored.
- **Mutable:** Sets are mutable, meaning you can add or remove elements after the set has been created.
- **Dynamic:** You can modify a set at any time, and its size can change.

#### Creating Sets
You can create a set using curly braces ``{}`` or the ``set()`` function.
```python
# Creating a set using curly braces
my_set = {1, 2, 3, 4}

# Creating a set using the set() function
my_set2 = set([1, 2, 3, 4])
```

#### Basic Set Operations
- **Adding Elements: **using the add() method.
```python
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}
```

- **Removing Elements: ** using the ``remove()`` or ``discard()`` methods.
The ``remove()`` method raises a KeyError if the element is not found, while ``discard()`` does not.
```python
my_set = {1, 2, 3, 4}

# Using remove()
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4}

# Using discard()
my_set.discard(5)  # Does not raise an error
print(my_set)  # Output: {1, 3, 4}
```
#### Set Operations
**1. Union:** Combines elements from both sets.
```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# or using the | operator:
union_set = set1 | set2
```
**2. Intersection:** Retrieves common elements from both sets.
```python
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}

# or using the & operator:
intersection_set = set1 & set2
```
**3. Difference:** Retrieves elements present in the first set but not in the second.
```python
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}

#or using the - operator:
difference_set = set1 - set2
```
**4. Symmetric Difference:** Retrieves elements present in either of the sets but not in both.
```python
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}

#or using the ^ operator:
symmetric_difference_set = set1 ^ set2
```
**5. Membership Testing**
You can check if an element exists in a set using the in keyword.
```python
my_set = {1, 2, 3}
print(2 in my_set)  # Output: True
print(5 in my_set)  # Output: False
```
</details>
<details>
<summary>What are the most common methods of set and how to use them</summary>

### Common Set Methods in Python

| **Method**                             | **Description**                                          | **Example**                                       | **Output**                |
|----------------------------------------|----------------------------------------------------------|---------------------------------------------------|---------------------------|
| `add(elem)`                            | Adds an element to the set.                             | `s = {1, 2, 3}`<br>`s.add(4)`                    | `{1, 2, 3, 4}`            |
| `remove(elem)`                         | Removes an element from the set; raises KeyError if not found. | `s = {1, 2, 3}`<br>`s.remove(2)`                 | `{1, 3}`                 |
| `discard(elem)`                        | Removes an element from the set; does not raise an error if not found. | `s = {1, 2, 3}`<br>`s.discard(4)`                | `{1, 2, 3}`              |
| `pop()`                                | Removes and returns an arbitrary element from the set; raises KeyError if empty. | `s = {1, 2, 3}`<br>`s.pop()`                      | `1` (or 2 or 3)          |
| `clear()`                              | Removes all elements from the set.                      | `s = {1, 2, 3}`<br>`s.clear()`                    | `set()`                  |
| `union(other_set)`                    | Returns a new set with elements from the set and `other_set`. | `s1 = {1, 2}`<br>`s2 = {2, 3}`<br>`s1.union(s2)` | `{1, 2, 3}`              |
| `intersection(other_set)`              | Returns a new set with elements common to the set and `other_set`. | `s1 = {1, 2}`<br>`s2 = {2, 3}`<br>`s1.intersection(s2)` | `{2}`                   |
| `difference(other_set)`                | Returns a new set with elements in the set that are not in `other_set`. | `s1 = {1, 2}`<br>`s2 = {2, 3}`<br>`s1.difference(s2)` | `{1}`                   |
| `symmetric_difference(other_set)`      | Returns a new set with elements in either the set or `other_set` but not in both. | `s1 = {1, 2}`<br>`s2 = {2, 3}`<br>`s1.symmetric_difference(s2)` | `{1, 3}`              |
| `copy()`                               | Returns a shallow copy of the set.                     | `s = {1, 2, 3}`<br>`s_copy = s.copy()`            | `{1, 2, 3}`              |
| `issubset(other_set)`                  | Returns `True` if the set is a subset of `other_set`. | `s1 = {1}`<br>`s2 = {1, 2, 3}`<br>`s1.issubset(s2)` | `True`                  |
| `issuperset(other_set)`                | Returns `True` if the set is a superset of `other_set`. | `s1 = {1, 2, 3}`<br>`s2 = {1}`<br>`s1.issuperset(s2)` | `True`                  |
| `isdisjoint(other_set)`                | Returns `True` if the set has no elements in common with `other_set`. | `s1 = {1, 2}`<br>`s2 = {3, 4}`<br>`s1.isdisjoint(s2)` | `True`                  |

#### Summary of Common Set Methods
- **Adding and Removing Elements**: Use `add()`, `remove()`, and `discard()` to manage the contents of a set.
- **Set Operations**: Use methods like `union()`, `intersection()`, `difference()`, and `symmetric_difference()` to perform mathematical set operations.
- **Membership and Relationships**: Use `issubset()`, `issuperset()`, and `isdisjoint()` to check relationships between sets.
- **Copying**: Use `copy()` to create a shallow copy of the set.

</details>
<details>
<summary>When to use sets versus lists</summary>

### Sets vs. Lists

| **Feature**                   | **Use Sets**                                           | **Use Lists**                                     |
|-------------------------------|-------------------------------------------------------|---------------------------------------------------|
| **Uniqueness**                | When you need to ensure all elements are unique.     | When duplicates are allowed and relevant.         |
| **Order**                     | When the order of elements does not matter.          | When the order of elements is important.          |
| **Membership Testing**        | When you need fast membership testing (`in` operator). | When membership testing is less frequent.         |
| **Mathematical Operations**   | When you need to perform set operations (union, intersection, etc.). | When you need to maintain a sequence of items.   |
| **Performance**               | When you require faster performance for lookups and deletions (average O(1)). | When you need to maintain a list for ordered iterations. |
| **Mutable Collections**       | When you need a mutable collection of unique items.  | When you need a mutable collection of ordered items. |
| **Use Cases**                 | Use sets for mathematical problems, unique collections, and membership tests. | Use lists for collections of items that need to be maintained in order or have duplicates. |

#### Summary
- **Use Sets** when you need unique elements, fast membership testing, or to perform set operations.
- **Use Lists** when you need to maintain order, allow duplicates, or perform operations that require sequence indexing.

</details>
<details>
<summary>How to iterate into a set</summary>

### Iterating Over a Set in Python

In Python, you can iterate over a set using a `for` loop. Since sets are unordered collections of unique elements, the order of iteration may vary.

#### Example of Iterating Over a Set

```python
# Create a set
my_set = {1, 2, 3, 4, 5}

# Iterate over the set
for element in my_set:
    print(element)
```
#### Using ``enumerate()`` with Sets
If you need the index of each element while iterating, you can use the ``enumerate()`` function:
```python
# Create a set
my_set = {'apple', 'banana', 'cherry'}

# Iterate with index
for index, fruit in enumerate(my_set):
    print(f"Index {index}: {fruit}")
```
**Note**
- The ``enumerate()`` function returns both the index and the value.
- The order of the elements may still vary because sets are unordered.

#### Converting to a List for Ordered Iteration
If you need to maintain a specific order during iteration, consider converting the set to a list:
```python
# Create a set
my_set = {3, 1, 2}

# Convert to a list and sort
sorted_list = sorted(my_set)

# Iterate over the sorted list
for element in sorted_list:
    print(element)
```
**Output**
The output will display the elements in ascending order:
```
1
2
3
```
</details>
<details>
<summary>What are dictionaries and how to use them</summary>

### What Are Dictionaries in Python?

Dictionaries are built-in data types in Python that store data in key-value pairs. They are unordered, mutable, and indexed collections that allow for fast lookups, modifications, and deletions.

#### Key Features of Dictionaries

- **Unordered**: The items in a dictionary are not stored in any particular order.
- **Mutable**: You can change, add, or remove items after the dictionary is created.
- **Indexed**: Each value in a dictionary is accessed using its corresponding key.

#### Creating a Dictionary

You can create a dictionary using curly braces `{}` or the `dict()` constructor.
```python
# Creating a dictionary using curly braces
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
# Creating a dictionary using the dict() constructor
my_dict = dict(name="Alice", age=30, city="New York")
```

#### Common Dictionary Methods

| **Method**               | **Description**                                                             | **Example**                     |
|--------------------------|-----------------------------------------------------------------------------|---------------------------------|
| `keys()`                 | Returns a view object of all keys in the dictionary.                       | `my_dict.keys()`               |
| `values()`               | Returns a view object of all values in the dictionary.                     | `my_dict.values()`             |
| `items()`                | Returns a view object of all key-value pairs in the dictionary.            | `my_dict.items()`              |
| `get(key)`               | Returns the value for the specified key; returns `None` if not found.     | `my_dict.get("name")`         |
| `update(other_dict)`     | Updates the dictionary with key-value pairs from another dictionary.       | `my_dict.update({"age": 31})`  |
| `clear()`                | Removes all items from the dictionary.                                     | `my_dict.clear()`              |

</details>
<details>
<summary>When to use dictionaries versus lists or sets</summary>

### Dictionaries vs. Lists and Sets

| **Feature**                   | **Use Dictionaries**                                         | **Use Lists**                                           | **Use Sets**                                           |
|-------------------------------|-------------------------------------------------------------|-------------------------------------------------------|-------------------------------------------------------|
| **Data Structure**            | Key-value pairs                                             | Ordered collection of items                           | Unordered collection of unique items                   |
| **Uniqueness**                | Keys must be unique; values can be duplicated              | Duplicates are allowed                                 | All elements are unique                                |
| **Order**                     | Unordered (Python 3.7+ maintains insertion order)          | Ordered (maintains the sequence of elements)          | Unordered                                             |
| **Access Method**             | Access values by keys (fast lookups)                       | Access elements by index                              | Membership testing (fast with `in` operator)         |
| **Performance**               | Fast for lookups and updates (average O(1))               | Slower for lookups (O(n) for membership testing)      | Fast for membership testing (average O(1))            |
| **Use Cases**                 | Use when you need to associate values with unique keys, like storing user information. | Use for ordered collections, where duplicates matter, like a list of items. | Use for mathematical operations, unique collections, and membership tests. |
| **Mutability**                | Mutable (you can add, remove, or change items)            | Mutable (you can add, remove, or change items)       | Mutable (you can add or remove items, but not change them) |

#### Summary
- **Use Dictionaries** when you need to map unique keys to specific values and require fast access to those values.
- **Use Lists** when you need to maintain an ordered collection of items, especially when duplicates are allowed or relevant.
- **Use Sets** when you need to ensure all elements are unique, perform mathematical operations, or require fast membership testing.

</details>
<details>
<summary>How to iterate over a dictionary</summary>

### How to Iterate Over a Dictionary in Python

| **Iteration Method**                   | **Description**                                               | **Example**                                                                                               | **Output**                                      |
|----------------------------------------|--------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| **Iterate Over Keys**                 | Use a `for` loop directly on the dictionary or `keys()`.    | ```python<br>for key in person:<br>    print(key)```                                               | name<br>age<br>city                            |
| **Iterate Over Values**               | Use the `values()` method.                                   | ```python<br>for value in person.values():<br>    print(value)```                                   | Alice<br>30<br>New York                        |
| **Iterate Over Key-Value Pairs**     | Use the `items()` method.                                   | ```python<br>for key, value in person.items():<br>    print(f"{key}: {value}")```                   | name: Alice<br>age: 30<br>city: New York     |

#### Summary

- Use `for key in my_dict:` to iterate over keys.
- Use `for value in my_dict.values():` to iterate over values.
- Use `for key, value in my_dict.items():` to iterate over key-value pairs.

</details>
<details>
<summary>What is a lambda function</summary>

### Lambda function
A lambda function in Python is a small anonymous function defined with the ``lambda`` keyword. Unlike regular functions defined using the ``def`` keyword, lambda functions are limited to a single expression. They can take any number of arguments but can only have one expression, which is evaluated and returned.

#### Characteristics of Lambda Functions
- **Anonymous:** Lambda functions do not have a name.
- **Single Expression:** They can only contain a single expression, which means they are not suitable for complex operations.
- **Inline Definition:** They can be defined inline where they are needed, often as an argument to higher-order functions (functions that take other functions as arguments).
- **Return Value:** The result of the expression is automatically returned.

**Syntax: ** ``lambda arguments: expression``
#### Example Usage
**1. Basic Example:**
```python
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5
```
**2. Using with Higher-Order Functions:**
Lambda functions are commonly used with functions like`` map()``, ``filter()``, and ``sorted()``.
```python
# Using map():
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # Output: [1, 4, 9, 16]

# Using filter():
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

# Using sorted():
points = [(2, 3), (1, 2), (4, 1)]
sorted_points = sorted(points, key=lambda point: point[1])
print(sorted_points)  # Output: [(4, 1), (1, 2), (2, 3)]
```
#### When to Use Lambda Functions
- When you need a simple function for a short period and do not want to formally define it with ``def``.
- When passing a simple function as an argument to higher-order functions.

#### Limitations
- **Readability:** Lambda functions can reduce code readability, especially if they are too complex or used excessively.
- **Single Expression:** They cannot contain multiple expressions or statements, which limits their use for more complex functionality.
</details>
<details>
<summary>What are the map, reduce and filter functions</summary>

### ``map``, ``reduce`` and ``filter`` functions
``map``, ``reduce``, and ``filter`` are higher-order functions in Python that allow you to process iterables (like lists or tuples) in a functional programming style. 
#### 1. ``map()``
- **Definition:** The ``map()`` function applies a given function to all items in an iterable (like a list) and returns a map object (which is an iterator). You can convert it to a list or another iterable type if needed.
- **Syntax:** ``map(function, iterable)``
```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16]
```
#### 2. ``filter()``
- **Definition:** The ``filter()`` function filters elements from an iterable based on a function that returns ``True`` or ``False``. It returns a filter object, which can also be converted to a list or other iterable types.
- **Syntax:** ``filter(function, iterable)``
```python
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]
```
#### 3. ``reduce()``
**Definition:** The ``reduce()`` function, available in the ``functools`` module, applies a rolling computation to sequential pairs of values in an iterable. It reduces the iterable to a single cumulative value.
**Syntax:** ``reduce(function, iterable[, initializer])``
``initializer`` is an optional parameter that specifies a value to be used as the initial input to the function. If an initializer is provided, it is used as the first argument to the function in the first call. If it is not provided, the first two items of the iterable are used.
```python
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 24 (1 * 2 * 3 * 4)

numbers = [2, 3, 4]
# Using 1 as the initializer
result = reduce(lambda x, y: x + y, numbers, 1)
print(result)  # Output: 10 (1 + 2 + 3 + 4)
```

#### Differences

| Function   | Purpose                                                   | Input                             | Output                             |
|------------|-----------------------------------------------------------|-----------------------------------|------------------------------------|
| `map()`    | Apply a function to all items in an iterable              | Function, Iterable                | Map object (iterator)             |
| `filter()` | Filter items in an iterable based on a function          | Function, Iterable                | Filter object (iterator)          |
| `reduce()` | Reduce an iterable to a single cumulative value           | Function, Iterable                | Single cumulative value            |

</details>

## Tasks
### 0. Squared simple
Write a function that computes the square value of all integers of a matrix.

**Prototype:** ``def square_matrix_simple(matrix=[]):``
- ``matrix`` is a 2 dimensional array
- Returns a new matrix:
    + Same size as matrix
    + Each value should be the square of the value of the input
- Initial matrix should not be modified
- You are not allowed to import any module
- You are allowed to use regular loops, ``map``, etc.
```bash
$ cat 0-main.py
#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

$ ./0-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
``` 
### 1. Search and replace
Write a function that replaces all occurrences of an element by another in a new list.
**Prototype:** ``def search_replace(my_list, search, replace):``
- ``my_list`` is the initial list
- ``search`` is the element to replace in the list
- ``replace`` is the new element
- You are not allowed to import any module
```bash
$ cat 1-main.py
#!/usr/bin/python3
search_replace = __import__('1-search_replace').search_replace

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)

$ ./1-main.py
[1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
[1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
```
### 2. Unique addition
Write a function that adds all unique integers in a list (only once for each integer).
**Prototype:** ``def uniq_add(my_list=[]):``
You are not allowed to import any module
```bash
$ cat 2-main.py
#!/usr/bin/python3
uniq_add = __import__('2-uniq_add').uniq_add

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))

$ ./2-main.py
Result: 15
```
### 3. Present in both
Write a function that returns a set of common elements in two sets.
**Prototype:** ``def common_elements(set_1, set_2):``
You are not allowed to import any module
```bash
$ cat 3-main.py
#!/usr/bin/python3
common_elements = __import__('3-common_elements').common_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
c_set = common_elements(set_1, set_2)
print(sorted(list(c_set)))

$ ./3-main.py
['C']
``` 
### 4. Only differents
Write a function that returns a set of all elements present in only one set.
**Prototype:** ``def only_diff_elements(set_1, set_2):``
You are not allowed to import any module
```bash
$ cat 4-main.py
#!/usr/bin/python3
only_diff_elements = __import__('4-only_diff_elements').only_diff_elements

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
od_set = only_diff_elements(set_1, set_2)
print(sorted(list(od_set)))

$ ./4-main.py
['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']
```
### 5. Number of keys
Write a function that returns the number of keys in a dictionary.
**Prototype:** ``def number_keys(a_dictionary):``
You are not allowed to import any module
```bash
$ cat 5-main.py
#!/usr/bin/python3
number_keys = __import__('5-number_keys').number_keys

a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
nb_keys = number_keys(a_dictionary)
print("Number of keys: {:d}".format(nb_keys))

$ ./5-main.py
Number of keys: 3
```
### 6. Print sorted dictionary
Write a function that prints a dictionary by ordered keys.
**Prototype:** ``def print_sorted_dictionary(a_dictionary):``
- You can assume that all keys are strings
- Keys should be sorted by alphabetic order
- Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
- Dictionary values can have any type
- You are not allowed to import any module
```bash
$ cat 6-main.py
#!/usr/bin/python3
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)

$ ./6-main.py
Number: 89
ids: [1, 2, 3]
language: C
track: Low level
```
### 7. Update dictionary
Write a function that replaces or adds key/value in a dictionary.
**Prototype:** ``def update_dictionary(a_dictionary, key, value):``
- ``key`` argument will be always a string
- ``value`` argument will be any type
- If a key exists in the dictionary, the value will be replaced
- If a key doesn’t exist in the dictionary, it will be created
- You are not allowed to import any module
```bash
$ cat 7-main.py
#!/usr/bin/python3
update_dictionary = __import__('7-update_dictionary').update_dictionary
print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
new_dict = update_dictionary(a_dictionary, 'language', "Python")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

print("--")
print("--")

new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)

$ ./7-main.py
language: Python
number: 89
track: Low level
--
language: Python
number: 89
track: Low level
--
--
city: San Francisco
language: Python
number: 89
track: Low level
--
city: San Francisco
language: Python
number: 89
track: Low level
```
### 8. Simple delete by key
Write a function that deletes a key in a dictionary.
**Prototype:** ``def simple_delete(a_dictionary, key=""):``
- ``key`` argument will be always a string
- If a key doesn’t exist, the dictionary won’t change
- You are not allowed to import any module
```bash
$ cat 8-main.py
#!/usr/bin/python3
simple_delete = __import__('8-simple_delete').simple_delete
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }
new_dict = simple_delete(a_dictionary, 'track')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

print("--")
print("--")
new_dict = simple_delete(a_dictionary, 'c_is_fun')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

$ ./8-main.py
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
--
--
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
```
### 9. Multiply by 2
Write a function that returns a new dictionary with all values multiplied by 2
**Prototype:** ``def multiply_by_2(a_dictionary):``
- You can assume that all values are only integers
- Returns a new dictionary
- You are not allowed to import any module
```bash
$ cat 9-main.py
#!/usr/bin/python3
multiply_by_2 = __import__('9-multiply_by_2').multiply_by_2
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

$ ./9-main.py
Alex: 8
Bob: 14
John: 12
Mike: 14
Molly: 16
--
Alex: 16
Bob: 28
John: 24
Mike: 28
Molly: 32
```
### 10. Best score
Write a function that returns a key with the biggest integer value.
**Prototype:** def best_score(a_dictionary):
- You can assume that all values are only integers
- If no score found, return ``None``
- You can assume all students have a different score
- You are not allowed to import any module
```bash
$ cat 10-main.py
#!/usr/bin/python3
best_score = __import__('10-best_score').best_score

a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))

$ ./10-main.py
Best score: Molly
Best score: None
```
### 11. Multiply by using map
Write a function that returns a list with all values multiplied by a number without using any loops.
**Prototype:** ``def multiply_list_map(my_list=[], number=0):``
- Returns a new list:
    + Same length as ``my_list``
    + Each value should be multiplied by ``number``
- Initial list should not be modified
- You are not allowed to import any module
- You have to use ``map``
- Your file should be max 3 lines
```bash
$ cat 11-main.py
#!/usr/bin/python3
multiply_list_map = __import__('11-multiply_list_map').multiply_list_map

my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)
print(my_list)

$ ./11-main.py
[4, 8, 12, 16, 24]
[1, 2, 3, 4, 6]
```
### 12. Roman to Integer
**Technical interview preparation:**
Create a function ``def roman_to_int(roman_string):`` that converts a [Roman numeral](https://en.wikipedia.org/wiki/Roman_numerals) to an integer.
- You can assume the number will be between 1 to 3999.
- ``def roman_to_int(roman_string)`` must return an integer
- If the ``roman_string`` is not a string or ``None``, return 0
```bash
$ cat 12-main.py
#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

$ ./12-main.py
X = 10
VII = 7
IX = 9
LXXXVII = 87
DCCVII = 707
```
### 13. Weighted average!
Write a function that returns the weighted average of all integers tuple ``(<score>, <weight>)``
**Prototype:** ``def weight_average(my_list=[]):``
- Returns ``0`` if the list is empty
- You are not allowed to import any module
```bash
$ cat 100-main.py
#!/usr/bin/python3
weight_average = __import__('100-weight_average').weight_average

my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
result = weight_average(my_list)
print("Average: {:0.2f}".format(result))

$ ./100-main.py
Average: 2.80
```
### 14. Squared by using map
Write a function that computes the square value of all integers of a matrix using ``map``
**Prototype:** ``def square_matrix_map(matrix=[]):``
- ``matrix`` is a 2 dimensional array
- Returns a new matrix:
    + Same size as ``matrix``
    + Each value should be the square of the value of the input
- Initial matrix should not be modified
- You are not allowed to import any module
- You have to use ``map``
- You are not allowed to use ``for`` or ``while``
- Your file should be max 3 lines
```bash
$ cat 101-main.py
#!/usr/bin/python3
square_matrix_map = \
    __import__('101-square_matrix_map').square_matrix_map

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_map(matrix)
print(new_matrix)
print(matrix)

$ ./101-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
### 15. Delete by value
Write a function that deletes keys with a specific value in a dictionary.
**Prototype:** ``def complex_delete(a_dictionary, value):``
- If the value doesn’t exist, the dictionary won’t change
- All keys having the searched value have to be deleted
- You are not allowed to import any module
```bash
$ cat 102-main.py
#!/usr/bin/python3
complex_delete = __import__('102-complex_delete').complex_delete
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
new_dict = complex_delete(a_dictionary, 'C')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

print("--")
print("--")
new_dict = complex_delete(a_dictionary, 'c_is_fun')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)

$ ./102-main.py
ids: [1, 2, 3]
track: Low
--
ids: [1, 2, 3]
track: Low
--
--
ids: [1, 2, 3]
track: Low
--
ids: [1, 2, 3]
track: Low
```
### 16. CPython #1: PyBytesObject
Create two C functions that print some basic info about Python lists and Python bytes objects.
Python lists:
- **Prototype:** ``void print_python_list(PyObject *p);``
- Format: see example

Python bytes:
- **Prototype:** ``void print_python_bytes(PyObject *p);``
- Format: see example
- Line “first X bytes”: print a maximum of 10 bytes
- If ``p`` is not a valid ``PyBytesObject``, print an error message (see example)
- Read ``/usr/include/python3.4/bytesobject.h``

About:
- Python version: 3.4
- Your shared library will be compiled with this command line: ``gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c``
- You are not allowed to use the following macros/functions:
    + ``Py_SIZE``
    + ``Py_TYPE``
    + ``PyList_GetItem``
    + ``PyBytes_AS_STRING``
    + ``PyBytes_GET_SIZE``
```bash
$ python3 --version
Python 3.4.3
$ gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c
$ cat 103-tests.py 
import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_list.argtypes = [ctypes.py_object]
lib.print_python_bytes.argtypes = [ctypes.py_object]
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
l = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], b"Holberton", "Betty"]
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
l = ["Holberton"]
lib.print_python_list(l)
lib.print_python_bytes(l);
$ python3 103-tests.py 
[.] bytes object info
  size: 5
  trying string: Hello
  first 6 bytes: 48 65 6c 6c 6f 00
[.] bytes object info
  size: 8
  trying string: �
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
Element 4: tuple
Element 5: list
Element 6: bytes
[.] bytes object info
  size: 9
  trying string: Holberton
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
```