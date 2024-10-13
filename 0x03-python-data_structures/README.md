# 0x03-python-data_structures
## Resources
[3.1.3. Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
[Data structures](https://docs.python.org/3/tutorial/datastructures.html) (until 5.3. Tuples and Sequences included)
[Learn to Program 6 : Lists](https://www.youtube.com/watch?v=A1HUzrvS-Pw&ab_channel=DerekBanas)
## Learning Objectives
<details>
<summary>What are lists and how to use them</summary>

### Lists in Python
A list in Python is an ordered, mutable collection of items. Lists can hold a variety of data types (e.g., integers, strings, other lists), and the items can be changed after the list is created. Lists are one of the most versatile and commonly used data structures in Python.

#### Key Features of Lists
- **Ordered**: Items in a list maintain their order (the order in which they are added).
- **Mutable**: You can modify lists (add, remove, or change items).
- **Heterogeneous**: A list can contain different data types (e.g., strings, numbers, other lists).

#### How to Create Lists
You can create a list by placing items inside square brackets ``[]``, separated by commas.
```python
# An empty list
empty_list = []

# A list of integers
numbers = [1, 2, 3, 4, 5]

# A list with mixed data types
mixed_list = [1, "Hello", 3.14, True]

# A list of lists (nested list)
nested_list = [[1, 2], [3, 4], [5, 6]]
```
#### Accessing Elements in a List
You can access list elements using indexing.
```python
my_list = ['apple', 'banana', 'cherry']

# Accessing elements
print(my_list[0])  # Output: 'apple'
print(my_list[1])  # Output: 'banana'
# Negative indexing
print(my_list[-1])  # Output: 'cherry' (last item)
```
#### Modifying Lists
Lists are mutable, which means you can change their content after creation. 

- **Changing an Item:** `my_list[1] = 'blueberry'  # Replace 'banana' with 'blueberry'`
- **Adding Items:**
    + ``append()``: Adds an item to the end of the list.
    + ``insert()``: Inserts an item at a specific position.
```python
# Append an item to the end
my_list.append('orange')
print(my_list)  # Output: ['apple', 'blueberry', 'cherry', 'orange']

# Insert an item at a specific index
my_list.insert(1, 'grape')  # Insert 'grape' at index 1
print(my_list)  # Output: ['apple', 'grape', 'blueberry', 'cherry', 'orange']
```
- **Removing Items:**
    + ``remove()``: Removes the first occurrence of a value.
    + ``pop()``: Removes and returns an item at a specific index (default is the last item).
    + ``clear()``: Removes all items from the list.
```python
# Remove an item by value
my_list.remove('blueberry')
print(my_list)  # Output: ['apple', 'grape', 'cherry', 'orange']

# Remove and return the last item
popped_item = my_list.pop()
print(popped_item)  # Output: 'orange'
print(my_list)      # Output: ['apple', 'grape', 'cherry']
```
#### List Slicing
Slicing allows you to extract a portion of the list by specifying a start and end index. The slice will include the start index but exclude the end index.
```python
numbers = [10, 20, 30, 40, 50]

# Slicing from index 1 to 3 (excluding index 3)
print(numbers[1:3])  # Output: [20, 30]

# Slicing with a step
print(numbers[::2])  # Output: [10, 30, 50]
```
#### List Comprehensions
List comprehensions provide a concise way to create lists.
**Basic Syntax:** ``[expression for item in iterable if condition]``
- **expression**: The expression (or operation) that generates elements in the new list.
- **item**: Each element from the iterable.
- **iterable**: Any Python iterable (like a list, string, range, etc.).
- **condition**: (Optional) A filtering condition for including elements.

| **Category**                        | **Description**                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| **Benefits of List Comprehensions** | **Concise**: Reduces the need for boilerplate code.                                                  |
|                                     | **Readable**: Often easier to understand than using loops, especially for simple operations.         |
|                                     | **Efficient**: Often faster than traditional `for` loops due to internal optimizations.              |
| **When to Use List Comprehensions** | When creating a new list by transforming an existing iterable.                                       |
|                                     | When applying filtering conditions to generate a new list.                                           |
|                                     | When the logic is simple enough to fit in a single, readable line.                                   |
| **When Not to Use List Comprehensions** | When the logic becomes complex, using nested loops or multiple conditions, which can reduce readability. |
|                                     | In such cases, using a regular `for` loop may be more appropriate.                                   |


```python
# Create a list of squares of numbers from 1 to 5
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]
```

**Example: List Comprehension with else**
You can even combine list comprehensions with if ... else for more complex expressions:
```python
# Create a list of even numbers or 'odd' for odd numbers
even_or_odd = [x if x % 2 == 0 else 'odd' for x in range(5)]
print(even_or_odd)  # Output: [0, 'odd', 2, 'odd', 4]
```
#### Common List Methods

| **Method**         | **Description**                                                | **Example**                                                                                 | **Result**                                        |
|--------------------|----------------------------------------------------------------|---------------------------------------------------------------------------------------------|---------------------------------------------------|
| `append(x)`        | Adds an item `x` to the end of the list.                       | `fruits = ['apple', 'banana']`<br>`fruits.append('cherry')`                                 | `['apple', 'banana', 'cherry']`                   |
| `extend(iterable)` | Extends the list by appending all the items from an iterable (e.g., another list). | `fruits = ['apple', 'banana']`<br>`fruits.extend(['cherry', 'grape'])`                      | `['apple', 'banana', 'cherry', 'grape']`          |
| `insert(i, x)`     | Inserts an item `x` at index `i`.                              | `fruits = ['apple', 'banana']`<br>`fruits.insert(1, 'cherry')`                              | `['apple', 'cherry', 'banana']`                   |
| `remove(x)`        | Removes the first occurrence of item `x` from the list.        | `fruits = ['apple', 'banana', 'cherry']`<br>`fruits.remove('banana')`                       | `['apple', 'cherry']`                             |
| `pop([i])`         | Removes and returns the item at index `i`. If `i` is not provided, removes the last item. | `fruits = ['apple', 'banana', 'cherry']`<br>`item = fruits.pop()`                           | `['apple', 'banana']` (`item` = `'cherry'`)       |
| `clear()`          | Removes all items from the list.                               | `fruits = ['apple', 'banana']`<br>`fruits.clear()`                                          | `[]`                                              |
| `index(x)`         | Returns the index of the first occurrence of item `x`.         | `fruits = ['apple', 'banana', 'cherry']`<br>`index = fruits.index('banana')`                | `1`                                               |
| `count(x)`         | Returns the number of occurrences of item `x`.                 | `fruits = ['apple', 'apple', 'cherry']`<br>`count = fruits.count('apple')`                  | `2`                                               |
| `sort()`           | Sorts the list in ascending order (in place).                  | `numbers = [3, 1, 2]`<br>`numbers.sort()`                                                   | `[1, 2, 3]`                                       |
| `reverse()`        | Reverses the order of the list (in place).                     | `fruits = ['apple', 'banana', 'cherry']`<br>`fruits.reverse()`                              | `['cherry', 'banana', 'apple']`                   |
| `copy()`           | Returns a shallow copy of the list.                            | `fruits = ['apple', 'banana']`<br>`new_list = fruits.copy()`                                | `['apple', 'banana']` (copy of the original list) |
| `len(list)`        | Returns the number of items in the list.                       | `fruits = ['apple', 'banana', 'cherry']`<br>`length = len(fruits)`                          | `3`                                               |

</details>
<details>
<summary>What are the differences and similarities between strings and lists</summary>

### Differences and Similarities Between Strings and Lists in Python

| **Aspect**               | **Strings**                                                  | **Lists**                                                    | **Similarities**                                 |
|--------------------------|--------------------------------------------------------------|--------------------------------------------------------------|-------------------------------------------------|
| **Type**                 | Immutable (cannot be changed after creation).                | Mutable (can be changed after creation).                      | Both are sequences in Python.                   |
| **Indexing**             | Supports indexing.                                           | Supports indexing.                                            | Both use zero-based indexing (i.e., `s[0]`).    |
| **Slicing**              | Supports slicing to access substrings.                       | Supports slicing to access sublists.                          | Slicing works the same way for both.            |
| **Methods**              | Has specific methods like `.upper()`, `.lower()`, `.find()`.  | Has specific methods like `.append()`, `.extend()`, `.pop()`.  | Both have common methods like `.index()`, `.count()`. |
| **Mutability**           | Immutable, modifying a string creates a new one.             | Mutable, can modify individual elements or slices in-place.    | Can be iterated over (looped through).          |
| **Element Type**         | Contains only characters.                                    | Can contain any type of elements (e.g., integers, strings).    | Both are iterable sequences.                    |
| **Concatenation**        | Concatenated using the `+` operator.                         | Concatenated using the `+` operator.                          | Both support concatenation.                     |
| **Repetition**           | Can repeat using the `*` operator.                          | Can repeat using the `*` operator.                            | Both support repetition with `*`.               |
| **Length**               | Measured by the `len()` function.                            | Measured by the `len()` function.                             | Both use `len()` to find the number of elements.|
| **Modifying Elements**   | Cannot modify elements directly (immutable).                 | Can modify, remove, or add elements directly (mutable).        | N/A                                             |

#### Summary:
- **Strings** are immutable and can only contain characters, whereas **lists** are mutable and can contain elements of any type.
- Both strings and lists share characteristics like indexing, slicing, concatenation, and repetition.
- Lists are more flexible since they can be modified after creation, whereas strings cannot.

</details>
<details>
<summary>How to use lists as stacks and queues</summary>

### Lists as stacks and queues
In Python, you can use lists to implement stacks and queues. Lists are versatile data structures, and while Python provides other specialized data structures (like ``deque`` from the ``collections`` module), lists can be used effectively for these purposes.

#### 1. Using Lists as Stacks
A **stack** is a data structure that follows the **Last In, First Out (LIFO)** principle. The last element added is the first one to be removed.
- Push (add) an item to the stack: Use ``append()``.
- Pop (remove) an item from the stack: Use ``pop()``.
```python
# Stack implementation using a list
stack = []

# Push items onto the stack
stack.append(1)
stack.append(2)
stack.append(3)

print(stack)  # Output: [1, 2, 3]

# Pop items from the stack (Last In, First Out)
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 2
print(stack)        # Output: [1]
```
#### 2. Using Lists as Queues
A **queue** is a data structure that follows the **First In, First Out (FIFO)** principle. The first element added is the first one to be removed.
- Enqueue (add) an item to the queue: Use ``append()``.
- Dequeue (remove) an item from the queue: Use ``pop(0)`` (removes the first element).
```python
# Queue implementation using a list
queue = []

# Enqueue items onto the queue
queue.append('a')
queue.append('b')
queue.append('c')

print(queue)  # Output: ['a', 'b', 'c']

# Dequeue items from the queue (First In, First Out)
print(queue.pop(0))  # Output: 'a'
print(queue.pop(0))  # Output: 'b'
print(queue)         # Output: ['c']
```
#### Key Differences Between Stacks and Queues
**Stack:** Uses ``append()`` to add and ``pop()`` to remove (LIFO).
**Queue:** Uses ``append()`` to add and ``pop(0)`` to remove (FIFO).

#### Important Note:
Using ``pop(0)`` on a list can be inefficient for large lists because all elements after the first must be shifted.
If performance is critical, consider using ``collections.deque`` for queues, as it provides efficient ``append()`` and ``popleft()`` operations.
</details>
<details>
<summary>What are tuples and how to use them</summary>

### Tuples
A tuple is a collection data type in Python that is **ordered** and **immutable**. Once a tuple is created, its values cannot be changed (unlike lists). Tuples are typically used to store a collection of related but heterogeneous data, often of fixed size.

Tuples are created by placing elements inside parentheses ``()`` separated by commas, or even without parentheses. However, the use of parentheses makes the tuple's definition clearer.

#### Key Characteristics of Tuples:
- **Ordered**: Tuples maintain the order of elements.
- **Immutable**: Once a tuple is created, you cannot modify, add, or remove elements.
- **Indexed**: You can access individual elements using an index, similar to lists.
- **Heterogeneous**: Tuples can contain elements of different data types (integers, strings, etc.).

#### How to Create Tuples

```python
# Basic Tuple Creation
my_tuple = (1, 2, 3, "apple", "banana")
print(my_tuple)  # Output: (1, 2, 3, 'apple', 'banana')

# Tuple Without Parentheses
my_tuple = 1, 2, 3
print(my_tuple)  # Output: (1, 2, 3)

# Single-element Tuple
# For a tuple with a single element, a trailing comma is required.
single_tuple = (42,)
print(single_tuple)  # Output: (42,)

# Accessing Tuple Elements
my_tuple = (1, 2, 3, "apple", "banana")
print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: 'apple'
```
#### Tuple Unpacking
You can unpack tuples into individual variables.
```python
my_tuple = ("John", 25, "Developer")
name, age, profession = my_tuple

print(name)        # Output: John
print(age)         # Output: 25
print(profession)  # Output: Developer
```
#### Tuple Methods
Though tuples are immutable, they have a few methods:

| **Method**   | **Description**                                                                 | **Example**                                                                                     | **Output**        |
|--------------|---------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|-------------------|
| `count(x)`   | Returns the number of times `x` appears in the tuple.                            | `my_tuple = (1, 2, 3, 1, 1)`<br>`my_tuple.count(1)`                                              | `3`               |
| `index(x)`   | Returns the index of the first occurrence of `x`.                                | `my_tuple = (1, 2, 3)`<br>`my_tuple.index(3)`                                                    | `2`               |

#### Use Cases of Tuples
- Return multiple values from a function.
- Fixed collections of data (e.g., coordinates, configurations).
- Heterogeneous data that doesn't require modification.

#### Tuples vs. Lists

| **Aspect**      | **Tuples**                                           | **Lists**                                      |
|-----------------|------------------------------------------------------|------------------------------------------------|
| **Mutability**  | Immutable (cannot be changed after creation).         | Mutable (can add, remove, or modify elements). |
| **Syntax**      | Created with parentheses `()` or just commas.         | Created with square brackets `[]`.             |
| **Performance** | Faster for read-only operations due to immutability.  | Slightly slower due to mutability.             |
| **Use Case**    | Best for fixed-size collections that don’t need modification. | Best for dynamic collections that need to be modified. |
| **Methods**     | Fewer methods (e.g., `count()`, `index()`).           | More methods (e.g., `append()`, `extend()`, `remove()`, etc.). |
| **Heterogeneity** | Can store elements of different types (e.g., integers, strings). | Can also store elements of different types.    |

</details>
<details>
<summary>What is a sequence</summary>

### Sequences
A sequence is a data structure in Python that stores multiple items in an **ordered** manner. Each item in the sequence is assigned an index, starting from 0. Sequences allow you to access, manipulate, and iterate over their elements. Some common sequence types in Python are strings, lists, tuples, and ranges.

#### Key Characteristics of Sequences:
- **Ordered**: The elements have a specific order, and each element is assigned an index.
- **Indexable**: You can access individual elements using their index (starting at 0).
- **Iterable**: You can loop through the elements in a sequence using loops like for.
- **Supports slicing**: You can extract portions of a sequence using slicing (e.g., ``my_list[1:3]``).

#### Common Sequence Types

| **Type**   | **Description**                                        | **Example**                           |
|------------|--------------------------------------------------------|---------------------------------------|
| **String** | Immutable sequence of characters.                      | `"hello"`                             |
| **List**   | Mutable sequence of elements (of any type).             | `[1, 2, 3, "apple"]`                  |
| **Tuple**  | Immutable sequence of elements (of any type).           | `(1, 2, 3, "apple")`                  |
| **Range**  | Immutable sequence of numbers, often used in loops.     | `range(0, 5)`                         |

#### Sequence Operations

| **Operation**    | **Description**                                      | **Example**                                         | **Output**            |
|------------------|------------------------------------------------------|-----------------------------------------------------|-----------------------|
| **Indexing**     | Access an element by its index.                      | `my_list = [10, 20, 30]`<br>`my_list[1]`            | `20`                  |
| **Slicing**      | Extract a portion of the sequence.                   | `my_list = [10, 20, 30, 40]`<br>`my_list[1:3]`      | `[20, 30]`            |
| **Concatenation**| Combine two sequences of the same type.              | `[1, 2] + [3, 4]`                                   | `[1, 2, 3, 4]`        |
| **Repetition**   | Repeat the elements in a sequence.                   | `[1, 2] * 2`                                        | `[1, 2, 1, 2]`        |
| **Membership**   | Check if an item is in the sequence.                 | `2 in [1, 2, 3]`                                    | `True`                |
| **Length**       | Get the number of elements in the sequence.          | `len([1, 2, 3])`                                    | `3`                   |

</details>
<details>
<summary>What is tuple packing</summary>

### Tuple packing
Tuple packing refers to the process of assigning multiple values to a tuple in a single statement without using parentheses. This allows you to bundle several values into a single tuple variable. Python automatically "packs" these values into a tuple when they are assigned together.
```python
# Tuple packing
my_tuple = 1, 2, "apple", True
print(my_tuple)  # Output: (1, 2, 'apple', True)
```
In this example, multiple values (1, 2, "apple", and True) are packed into a single tuple called ``my_tuple``. No parentheses are needed, but adding them is optional.

#### Key Points:
- Tuple packing allows grouping multiple values in one step.
- Parentheses are optional during tuple packing.
- The values are automatically bundled into a tuple.

#### When to Use Tuple Packing:
When you need to store multiple values in a single variable, such as returning multiple results from a function.
Example in Function Return:
```python
def get_info():
    name = "Alice"
    age = 25
    country = "USA"
    return name, age, country  # Tuple packing in return

result = get_info()
print(result)  # Output: ('Alice', 25, 'USA')
```
Here, the function get_info() returns multiple values, and they are automatically packed into a tuple.
</details>
<details>
<summary>What is sequence unpacking</summary>

### Sequence Unpacking in Python
**Sequence unpacking** is the process of extracting values from a sequence (such as a list, tuple, or string) and assigning them to multiple variables in a single statement. This allows you to easily work with multiple values without accessing them individually by index.
Example
```python
# Sequence unpacking
my_tuple = (1, 2, "apple")
a, b, c = my_tuple

print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: apple
```
In this example, the values from my_tuple are unpacked and assigned to the variables ``a``, ``b``, and ``c`` in one line.
#### Key Points:
- Sequence unpacking can be used with any sequence type, including lists, tuples, and strings.
- The number of variables on the left side must match the number of elements in the sequence being unpacked.
- If the number of variables does not match the number of elements, a ``ValueError`` will be raised.

#### Using an Asterisk for Extended Unpacking:
Python also allows for extended unpacking using the asterisk (``*``) operator. This is useful when you want to capture multiple elements in one variable.
```python
# Extended sequence unpacking
my_list = [1, 2, 3, 4, 5]
first, *rest = my_list

print(first)  # Output: 1
print(rest)   # Output: [2, 3, 4, 5]
```
In this example, first captures the first element of the list, and rest captures all remaining elements as a new list.

#### When to Use Sequence Unpacking:
- When you want to assign multiple values from a sequence to variables in a clean and readable way.
- When you want to extract specific elements while ignoring others.
</details>
<details>
<summary>What is the del statement and how to use it</summary>

### The del Statement
The ``del`` statement in Python is used to delete objects, including variables, list elements, or slices, and dictionary entries. It can remove references to the object, making it eligible for garbage collection if no other references exist.
**Syntax:** `del <object>`

#### Key Features of the del Statement:
- Deleting Variables: You can delete a variable completely, removing its reference.
- Deleting List Elements: You can remove specific elements from a list by their index.
- Deleting Slices: You can delete multiple elements from a list using slicing.
- Deleting Dictionary Entries: You can remove specific key-value pairs from a dictionary.

#### Examples of Using the `del` Statement


| **Example**                          | **Description**                                        | **Output**                     |
|--------------------------------------|--------------------------------------------------------|--------------------------------|
| **Deleting a Variable**             | Remove a variable completely.                          | Raises `NameError`             |
| `x = 10`                             | Assigns 10 to variable `x`.                           | `10`                           |
| `del x`                             | Deletes variable `x`.                                 | -                              |
|                                      |                                                        | -                              |
| **Deleting List Elements**           | Remove specific elements from a list.                 | `[1, 2, 4, 5]`                |
| `my_list = [1, 2, 3, 4, 5]`         | Assigns a list to `my_list`.                          | `[1, 2, 3, 4, 5]`             |
| `del my_list[2]`                   | Deletes the element at index 2.                       | -                              |
|                                      |                                                        | -                              |
| **Deleting Slices**                 | Remove multiple elements from a list using slicing.   | `[1, 4, 5]`                   |
| `my_list = [1, 2, 3, 4, 5]`         | Assigns a list to `my_list`.                          | `[1, 2, 3, 4, 5]`             |
| `del my_list[1:3]`                 | Deletes elements from index 1 to 2.                   | -                              |
|                                      |                                                        | -                              |
| **Deleting Dictionary Entries**      | Remove specific key-value pairs from a dictionary.    | `{'a': 1, 'c': 3}`            |
| `my_dict = {'a': 1, 'b': 2, 'c': 3}`| Assigns a dictionary to `my_dict`.                    | `{'a': 1, 'b': 2, 'c': 3}`    |
| `del my_dict['b']`                 | Deletes the entry with key 'b'.                       | -                              |


</details>

## Tasks
### 0. Print a list of integers
Write a function that prints all integers of a list.
**Prototype:** ``def print_list_integer(my_list=[]):``
- Format: one integer per line. See example
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use ``str.format()`` to print integers
```bash
$ cat 0-main.py
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

$ ./0-main.py
1
2
3
4
5
```
### 1. Secure access to an element in a list
Write a function that retrieves an element from a list like in C.
**Prototype:** ``def element_at(my_list, idx):``
- If ``idx`` is negative, the function should return ``None``
- If ``idx`` is out of range (> of number of element in ``my_list``), the function should return ``None``
- You are not allowed to import any module
- You are not allowed to use ``try/except``
```bash
$ cat 1-main.py
#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

$ ./1-main.py
Element at index 3 is 4
```
### 2. Replace element
Write a function that replaces an element of a list at a specific position (like in C).
**Prototype:** ``def replace_in_list(my_list, idx, element):``
- If ``idx`` is negative, the function should not modify anything, and returns the original list
- If ``idx`` is out of range (> of number of element in ``my_list``), the function should not modify anything, and returns the original list
- You are not allowed to import any module
- You are not allowed to use ``try/except``
```bash
$ cat 2-main.py
#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

$ ./2-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 9, 5]
```  
### 3. Print a list of integers... in reverse!
Write a function that prints all integers of a list, in reverse order.
**Prototype:** ``def print_reversed_list_integer(my_list=[]):``
- Format: one integer per line. See example
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use ``str.format()`` to print integers
```bash
$ cat 3-main.py
#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

$ ./3-main.py
5
4
3
2
1
```
### 4. Replace in a copy
Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).
**Prototype:** ``def new_in_list(my_list, idx, element):``
- If ``idx`` is negative, the function should return a copy of the original ``list``
- If ``idx`` is out of range (> of number of element in ``my_list``), the function should return a copy of the original ``list``
- You are not allowed to import any module
- You are not allowed to use ``try/except``
```bash
$ cat 4-main.py
#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

$ ./4-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 4, 5]
```
### 5. Can you C me now?
Write a function that removes all characters ``c`` and ``C`` from a string.
**Prototype:** ``def no_c(my_string):``
- The function should return the new string
- You are not allowed to import any module
- You are not allowed to use ``str.replace()``
```bash
$ cat 5-main.py
#!/usr/bin/env python3
no_c = __import__('5-no_c').no_c

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))

$ ./5-main.py
Best Shool
hiago
 is fun!
```
### 6. Lists of lists = Matrix
Write a function that prints a matrix of integers.
**Prototype:** ``def print_matrix_integer(matrix=[[]]):``
- Format: see example
- You are not allowed to import any module
- You can assume that the list only contains integers
- You are not allowed to cast integers into strings
- You have to use ``str.format()`` to print integers
```bash
$ cat 6-main.py
#!/usr/bin/python3
print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

$ ./6-main.py | cat -e
1 2 3$
4 5 6$
7 8 9$
--$
$
```
### 7. Tuples addition
Write a function that adds 2 tuples.
**Prototype:** ``def add_tuple(tuple_a=(), tuple_b=()):``
- Returns a tuple with 2 integers:
    + The first element should be the addition of the first element of each argument
    + The second element should be the addition of the second element of each argument
- You are not allowed to import any module
- You can assume that the two tuples will only contain integers
- If a tuple is smaller than 2, use the value ``0`` for each missing integer
- If a tuple is bigger than 2, use only the first 2 integers
```bash
$ cat 7-main.py
#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))

$ ./7-main.py
(89, 100)
(2, 89)
(1, 89)
```
### 8. More returns!
Write a function that returns a tuple with the length of a string and its first character.
**Prototype:** ``def multiple_returns(sentence):``
- If the sentence is empty, the first character should be equal to ``None``
- You are not allowed to import any module
```bash
$ cat 8-main.py
#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

$ ./8-main.py
Length: 22 - First character: A
```  
### 9. Find the max
Write a function that finds the biggest integer of a list.
**Prototype:** ``def max_integer(my_list=[]):``
- If the list is empty, return ``None``
- You can assume that the list only contains integers
- You are not allowed to import any module
- You are not allowed to use the builtin ``max()``
```bash
$ cat 9-main.py
#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))

$ ./9-main.py
Max: 90
```
### 10. Only by 2
Write a function that finds all multiples of 2 in a list.
**Prototype:** ``def divisible_by_2(my_list=[]):``
- Return a new list with ``True`` or ``False``, depending on whether the integer at the same position in the original list is a multiple of 2
- The new list should have the same size as the original list
- You are not allowed to import any module
```bash
$ cat 10-main.py
#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1

$ ./10-main.py
0 is divisible by 2
1 is not divisible by 2
2 is divisible by 2
3 is not divisible by 2
4 is divisible by 2
5 is not divisible by 2
6 is divisible by 2
```
### 11. Delete at
Write a function that deletes the item at a specific position in a list.
**Prototype:** ``def delete_at(my_list=[], idx=0):``
- If ``idx`` is negative or out of range, nothing change (returns the same list)
- You are not allowed to use ``pop()``
- You are not allowed to import any module
```bash
$ cat 11-main.py
#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)

$ ./11-main.py
[1, 2, 3, 5]
[1, 2, 3, 5]
```
### 12. Switch
Complete the source code in order to switch value of ``a`` and ``b``
- You can find the source code [here](https://github.com/alx-tools/0x03.py/blob/master/12-switch_py)
- Your code should be inserted where the comment is (line 4)
- Your program should be exactly 5 lines long
```bash
$ ./12-switch.py
a=10 - b=89
$ wc -l 12-switch.py
5 12-switch.py
```
### 13. Linked list palindrome
**Technical interview preparation:**
Write a function in C that checks if a singly linked list is a palindrome.

**Prototype:** ``int is_palindrome(listint_t **head);``
- Return: ``0`` if it is not a palindrome, 1 if it is a palindrome
- An empty list is considered a palindrome
```bash
$ cat lists.h 
#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);

#endif /* LISTS_H */
$
$ cat linked_lists.c 
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
$
$ cat 13-main.c
#include <stdio.h>
#include <stdlib.h>
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
    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 17);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 17);
    add_nodeint_end(&head, 1);
    print_listint(head);

    if (is_palindrome(&head) == 1)
        printf("Linked list is a palindrome\n");
    else
        printf("Linked list is not a palindrome\n");

    free_listint(head);

    return (0);
}
$
$ gcc -Wall -Werror -Wextra -pedantic 13-main.c linked_lists.c 13-is_palindrome.c -o palindrome
$ ./palindrome
1
17
972
50
98
98
50
972
17
1
Linked list is a palindrome
```
### 14. CPython #0: Python lists
CPython is the reference implementation of the Python programming language. Written in C, CPython is the default and most widely used implementation of the language.
Since we now know a bit of C, we can look at what is happening under the hood of Python. Let’s have fun with Python and C, and let’s look at what makes Python so easy to use.
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS
Create a C function that prints some basic info about Python lists.
**Prototype:** ``void print_python_list_info(PyObject *p);``
- Format: see example
- Python version: 3.4
- Your shared library will be compiled with this command line: ``gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/- include/python3.4 100-print_python_list_info.c``
- OS: ``Ubuntu 14.04 LTS``
- Start by reading:
    + listobject.h
    + object.h
    + [Common Object Structures](https://docs.python.org/3.4/c-api/structures.html)
    + [List Objects](https://docs.python.org/3.4/c-api/list.html)
```bash
julien@ubuntu:~/CPython$ gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c
julien@ubuntu:~/CPython$ cat 100-test_lists.py 
import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]
l = ['hello', 'World']
lib.print_python_list_info(l)
del l[1]
lib.print_python_list_info(l)
l = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], "My string"]
lib.print_python_list_info(l)
l = []
lib.print_python_list_info(l)
l.append(0)
lib.print_python_list_info(l)
l.append(1)
l.append(2)
l.append(3)
l.append(4)
lib.print_python_list_info(l)
l.pop()
lib.print_python_list_info(l)
julien@ubuntu:~/CPython$ python3 100-test_lists.py 
[*] Size of the Python List = 2
[*] Allocated = 2
Element 0: str
Element 1: str
[*] Size of the Python List = 1
[*] Allocated = 2
Element 0: str
[*] Size of the Python List = 7
[*] Allocated = 7
Element 0: str
Element 1: int
Element 2: int
Element 3: float
Element 4: tuple
Element 5: list
Element 6: str
[*] Size of the Python List = 0
[*] Allocated = 0
[*] Size of the Python List = 1
[*] Allocated = 4
Element 0: int
[*] Size of the Python List = 5
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
Element 4: int
[*] Size of the Python List = 4
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
julien@CPython:~/CPython$ 
```