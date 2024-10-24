# 0x0B. Python - Input/Output
## Resources
- [7.2. Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [8.7. Predefined Clean-up Actions](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions)
- [Dive Into Python 3: Chapter 11. Files](https://histo.ucsf.edu/BMS270/diveintopython3-r802.pdf) (until “11.4 Binary Files” (included))
- [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [Learn to Program 8 : Reading / Writing Files](https://www.youtube.com/watch?v=EukxMIsNeqU&ab_channel=DerekBanas)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) (ch. 8 p 180-183 and ch. 14 p 326-333)
- [All about py-file I/O](https://techvidvan.com/tutorials/python-file-read-write/)
## Learning Objectives
<details>
<summary>How to open a file</summary>

### Open a file
In Python, you can open a file using the built-in ``open()`` function. 
**Syntax:** `file_object = open(file_path, mode)`
- ``file_path``: The location of the file you want to open (can be a relative or absolute path).
- ``mode``: The mode in which you want to open the file. Common modes include:

| Mode   | Description                                                                 |
|--------|-----------------------------------------------------------------------------|
| `'r'`  | Read-only mode. The file must exist.                                         |
| `'w'`  | Write-only mode. If the file exists, it will be truncated. If not, created.  |
| `'a'`  | Append mode. Data is added to the end of the file. Creates the file if necessary. |
| `'b'`  | Binary mode. Used for non-text files like images or audio files.             |
| `'r+'` | Read and write mode. The file must exist.                                    |
| `'w+'` | Write and read mode. If the file exists, it will be truncated. If not, created. |

#### Example: Reading from a file
```python
# Open a file in read mode
file = open('example.txt', 'r')

# Read the content of the file
content = file.read()
print(content)

# Always close the file after use
file.close()
```
#### Using ``with`` Statement (Recommended)
It’s recommended to use the ``with`` statement when working with files because it automatically handles closing the file for you, even if an exception occurs.
```python
# Using 'with' to open and read a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# No need to explicitly call file.close() here
```
#### Writing to a file
```python
# Open a file in write mode
with open('output.txt', 'w') as file:
    file.write("Hello, world!")
```
#### Appending to a file
```python
# Open a file in append mode
with open('output.txt', 'a') as file:
    file.write("\nThis is an appended line.")
```
#### Reading file line by line
```python
# Read a file line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip() removes the newline character
```
</details>
<details>
<summary>How to read the full content of a file</summary>

### ``read()``
To read the full content of a file in Python, you can use the ``read()`` method after opening the file.
```python
# Open a file in read mode
with open('example.txt', 'r') as file:
    content = file.read()  # Reads the entire content of the file
    print(content)
```
</details>
<details>
<summary>How to read a file line by line</summary>

### ``for`` loop vs. `readline()` vs. `readlines()`
To read a file line by line in Python, you can either use a loop that iterates over the file object or use the ``readline()`` method. Here are both approaches:

#### 1. Using a ``for`` loop to read line by line
```python
# Open the file and read it line by line using a loop
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip() removes the newline character at the end of each line
```
#### 2. Using ``readline()`` to read a line at a time
```python
# Open the file and read it line by line using readline()
with open('example.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line.strip())  # strip() removes the newline character
        line = file.readline()  # Read the next line
```
- ``readline()``: Reads one line at a time.
- ``while line``: Loops until readline() returns an empty string (end of file).
#### 3. Using ``readlines()`` (less common for large files)
This reads all lines into a list, then you can loop through them:
```python
# Open the file and read all lines at once
with open('example.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())
```
``readlines()``: Reads all lines into a list. Each line in the file becomes an element in the list.
#### Which to use?
- For large files: Use the ``for`` loop or ``readline()`` since they don’t load the entire file into memory.
- For smaller files: ``readlines()`` may be fine if you want to work with the entire file at once
</details>
<details>
<summary>How to move the cursor in a file</summary>

### How to move the cursor in a file
In Python, you can move the cursor (also called the file pointer) within a file using the ``seek()`` method. This method allows you to move the file pointer to a specific position in the file.
**Syntax:** `file.seek(offset, whence)`
- ``offset``: The number of bytes to move the cursor.
- ``whence``: This is optional and specifies the reference point for ``offset``. It can be:
    + ``0``: (default) Move relative to the beginning of the file.
    + ``1``: Move relative to the current file pointer position.
    + ``2``: Move relative to the end of the file.

#### Example: Moving the cursor to the beginning of the file
```python
with open('example.txt', 'r') as file:
    file.seek(0)  # Move to the start of the file
    content = file.read()
    print(content)
```
#### Example: Moving the cursor to a specific byte position
```python
with open('example.txt', 'r') as file:
    file.seek(10)  # Move the cursor to the 10th byte from the start
    content = file.read()
    print(content)
```
#### Example: Moving the cursor to the end of the file
```python
with open('example.txt', 'r') as file:
    file.seek(0, 2)  # Move the cursor to the end of the file
    print("Cursor moved to the end of the file")
```
#### Example: Moving the cursor relative to the current position
```python
with open('example.txt', 'r') as file:
    file.seek(5)  # Move 5 bytes from the start
    file.seek(10, 1)  # Move 10 bytes forward from the current position
    content = file.read()
    print(content)
```
#### Example: Using ``tell()`` to get the current cursor position
The ``tell()`` method returns the current position of the file pointer.
```python
with open('example.txt', 'r') as file:
    print(file.tell())  # Prints the current cursor position (0 at the start)
    file.read(5)  # Read the first 5 characters
    print(file.tell())  # Prints the current cursor position after reading 5 bytes
```
#### Summary of File Pointer Operations:
- ``file.seek(offset, whence)`` is used to move the file pointer to a specific position.
- ``file.tell()`` returns the current position of the file pointer.
</details>
<details>
<summary>How to make sure a file is closed after using it</summary>

### Closing a file
To ensure a file is properly closed after using it in Python, the recommended approach is to use a ``with`` statement. This guarantees that the file is closed automatically, even if an exception occurs during file operations.

#### Using ``with`` statement (Best Practice)
The ``with`` statement manages the file context and ensures the file is properly closed when you're done with it.
```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# File is automatically closed when the block exits
```
#### Without ``with`` (manual closing)
You can also open and close the file manually using ``file.close()``, but this is error-prone if an exception occurs and the file doesn't get closed properly.
**Example (manual closing):**
```python
file = open('example.txt', 'r')
try:
    content = file.read()
    print(content)
finally:
    file.close()  # Ensures the file is closed, even if an exception occurs
```
While this works, it's better to use the with statement to avoid manual file handling and ensure automatic closure.
#### ``.closed`` attribute
The ``.closed`` attribute of a file object is used to check whether a file is closed or not. It returns ``True`` if the file is closed and ``False`` if it’s still open.

```python
with open('example.txt', 'r') as file:
    print(file.closed)  # Output: False, because the file is still open

# After the `with` block, the file is closed
print(file.closed)  # Output: True, because the file has been automatically closed

# Checking .closed without with (manual closing)
file = open('example.txt', 'r')
print(file.closed)  # Output: False, the file is open

file.close()  # Manually closing the file
print(file.closed)  # Output: True, the file is now closed
```
</details>
<details>
<summary>What is and how to use the ``with`` statement</summary>

### ``with`` statement
The ``with`` statement in Python is used to simplify resource management tasks, such as opening files or handling locks. It ensures that resources are properly acquired and released without explicitly needing to manage them (e.g., closing files or releasing locks), even if an error occurs.

The ``with`` statement works with objects that support the **context management protocol**—these objects must implement the ``__enter__()`` and ``__exit__()`` methods.

#### Common Usage of the ``with`` Statement (File Handling)
The most common use case of ``with`` is in file handling. When opening files, the ``with`` statement guarantees that the file is properly closed after its block of code is executed, even if an exception occurs.
```python
# Open a file, read its content, and automatically close the file after the block
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# The file is automatically closed after the with block, even if an error occurs
```
#### Benefits of using with:
**- Automatic resource management:** You don't need to manually close the file or handle exceptions to ensure the resource is released.
**- Cleaner and shorter code:** No need for explicit ``try/finally ``blocks for cleanup.
**- Exception safety:** If an exception is raised inside the block, the file (or other resource) is still properly closed.
#### Equivalent code without ``with`` (manual file handling)
If you don’t use ``with``, you would have to manually open and close the file, which is more error-prone:
```python
file = open('example.txt', 'r')
try:
    content = file.read()
    print(content)
finally:
    file.close()  # Ensure the file is closed, even if an error occurs
```
#### How ``with`` Works Internally
When using ``with``, two methods are automatically called:
- ``__enter__()``: This method is executed when entering the ``with`` block, setting up the resource.
- ``__exit__()``: This method is executed when exiting the ``with`` block, ensuring cleanup (like closing the file).
#### Example of a custom context manager using ``with``
You can create your own class to use with ``with`` by implementing the ``__enter__()`` and ``__exit__()`` methods:
```python
class MyResource:
    def __enter__(self):
        print("Acquiring resource")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Releasing resource")

# Using with a custom context manager
with MyResource() as resource:
    print("Using the resource")
```
Output:
```
Acquiring resource
Using the resource
Releasing resource
```
</details>
<details>
<summary>What is JSON</summary>

### JSON
**JSON** (JavaScript Object Notation) is a lightweight data-interchange format that is easy for humans to read and write and easy for machines to parse and generate. It is widely used for data exchange between servers and web applications, as well as in configurations and APIs due to its simplicity and readability.
#### Key Features of JSON:
**- Human-readable:** The syntax is straightforward and resembles JavaScript object literals.
**- Lightweight:** JSON uses a minimalistic syntax, which makes it suitable for data transmission over networks.
**- Language-independent:** Although it originates from JavaScript, JSON can be used with almost any programming language (like Python, Java, C++, PHP, etc.).
#### JSON Structure:
JSON is built on two structures:
**1. Objects:** Key-value pairs (similar to Python dictionaries or JavaScript objects).
**2. Arrays:** Ordered lists of values (similar to Python lists or JavaScript arrays).
#### JSON Syntax Rules:
- Data is written as key/value pairs.
- Keys are always strings and are enclosed in double quotes.
- Values can be strings, numbers, booleans, arrays, objects, or ``null``.
- Arrays and objects can be nested.
**Example of a JSON object:**
```json
{
  "name": "Alice",
  "age": 30,
  "isStudent": false,
  "courses": ["Math", "Physics", "Chemistry"],
  "address": {
    "street": "123 Main St",
    "city": "New York"
  }
}
```
#### Common Uses of JSON:
**- APIs:** JSON is commonly used to exchange data between a client and a server. Many web services use JSON as the format for sending requests and receiving responses.
**- Configurations:** JSON is used to define configuration files in many frameworks and tools.
**- Data storage:** JSON is often used to store simple data structures, like in NoSQL databases (e.g., MongoDB).

</details>
<details>
<summary>Serialization and Deserialization</summary>

### Working with JSON in Python:
Python provides the ``json`` module to work with JSON data, which allows you to easily convert between Python objects and JSON strings.

#### Serialization: Convert Python objects to JSON:
```python
import json

data = {
    "name": "Alice",
    "age": 30,
    "isStudent": False,
    "courses": ["Math", "Physics", "Chemistry"]
}

json_string = json.dumps(data)
print(json_string)  # Output: JSON-formatted string
```
#### Deserialization: Convert JSON strings to Python objects:
```python
import json

json_string = '{"name": "Alice", "age": 30, "isStudent": false, "courses": ["Math", "Physics", "Chemistry"]}'
data = json.loads(json_string)
print(data)  # Output: Python dictionary
```
#### Common Functions in Python’s json Module:
##### 1. ``json.dumps()``:
Serializes (Converts) Python objects (like dictionaries, lists) into a JSON string.
```python
import json
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)
print(json_string)  # Output: {"name": "Alice", "age": 30}
```
##### 2. ``json.loads()``:
Converts a JSON string back into a Python object (like a dictionary).
```python
import json
json_string = '{"name": "Alice", "age": 30}'
python_obj = json.loads(json_string)
print(python_obj)  # Output: {'name': 'Alice', 'age': 30}
```
##### 3. json.dump():
Serializes (converts) a Python object to a JSON formatted string and writes it directly to a file.
```python
import json
data = {"name": "Alice", "age": 30}
with open('data.json', 'w') as file:
    json.dump(data, file)
# The 'data.json' file will now contain: {"name": "Alice", "age": 30}
```
##### 4. ``json.load()``:
Reads JSON data from a file and converts it into a Python object.
```python
import json
with open('data.json', 'r') as file:
    data = json.load(file)
print(data)  # Output: {'name': 'Alice', 'age': 30}
```
**Summary:**
- ``json.dumps()`` and ``json.loads()`` work with strings.
- ``json.dump()`` and ``json.load()`` work with files.

</details>

## Tasks
### 0. Read file
Write a function that reads a text file (``UTF8``) and prints it to stdout:
- Prototype: ``def read_file(filename=""):``
- You must use the ``with`` statement
- You don’t need to manage ``file permission`` or ``file doesn't exist`` exceptions.
- You are not allowed to import any module
```bash
$ cat 0-main.py
#!/usr/bin/python3
read_file = __import__('0-read_file').read_file

read_file("my_file_0.txt")

$ cat my_file_0.txt
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
$ ./0-main.py
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers. 

A school every software engineer would have dreamt of!
```
### 1. Write to a file
Write a function that writes a string to a text file (``UTF8``) and returns the number of characters written:
- Prototype: ``def write_file(filename="", text=""):``
- You must use the ``with`` statement
- You don’t need to manage file permission exceptions.
- Your function should create the file if doesn’t exist.
- Your function should overwrite the content of the file if it already exists.
- You are not allowed to import any module
```bash
$ cat 1-main.py
#!/usr/bin/python3
write_file = __import__('1-write_file').write_file

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)

$ ./1-main.py
29
$ cat my_first_file.txt
This School is so cool!
```

### 2. Append to a file
Write a function that appends a string at the end of a text file (``UTF8``) and returns the number of characters added:
- Prototype: ``def append_write(filename="", text=""):``
- If the file doesn’t exist, it should be created
- You must use the ``with`` statement
- You don’t need to manage ``file permission`` or ``file doesn't exist`` exceptions.
- You are not allowed to import any module
```bash
$ cat 2-main.py
#!/usr/bin/python3
append_write = __import__('2-append_write').append_write

nb_characters_added = append_write("file_append.txt", "This School is so cool!\n")
print(nb_characters_added)

$ cat file_append.txt
cat: file_append.txt: No such file or directory
$ ./2-main.py
29
$ cat file_append.txt
This School is so cool!
$ ./2-main.py
29
$ cat file_append.txt
This School is so cool!
This School is so cool!
```
### 3. To JSON string
Write a function that returns the JSON representation of an object (string):
- Prototype: def to_json_string(my_obj):
- You don’t need to manage exceptions if the object can’t be serialized.
```bash
$ cat 3-main.py
#!/usr/bin/python3
to_json_string = __import__('3-to_json_string').to_json_string

my_list = [1, 2, 3]
s_my_list = to_json_string(my_list)
print(s_my_list)
print(type(s_my_list))

my_dict = { 
    'id': 12,
    'name': "John",
    'places': [ "San Francisco", "Tokyo" ],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
s_my_dict = to_json_string(my_dict)
print(s_my_dict)
print(type(s_my_dict))

try:
    my_set = { 132, 3 }
    s_my_set = to_json_string(my_set)
    print(s_my_set)
    print(type(s_my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

$ ./3-main.py
[1, 2, 3]
<class 'str'>
{"id": 12, "is_active": true, "name": "John", "info": {"average": 3.14, "age": 36}, "places": ["San Francisco", "Tokyo"]}
<class 'str'>
[TypeError] {3, 132} is not JSON serializable
```
### 4. From JSON string to Object
Write a function that returns an object (Python data structure) represented by a JSON string:
- Prototype: def from_json_string(my_str):
- You don’t need to manage exceptions if the JSON string doesn’t represent an object.
```bash
$ cat 4-main.py
#!/usr/bin/python3
from_json_string = __import__('4-from_json_string').from_json_string

s_my_list = "[1, 2, 3]"
my_list = from_json_string(s_my_list)
print(my_list)
print(type(my_list))

s_my_dict = """
{"is_active": true, "info": {"age": 36, "average": 3.14}, 
"id": 12, "name": "John", "places": ["San Francisco", "Tokyo"]}
"""
my_dict = from_json_string(s_my_dict)
print(my_dict)
print(type(my_dict))

try:
    s_my_dict = """
    {"is_active": true, 12 }
    """
    my_dict = from_json_string(s_my_dict)
    print(my_dict)
    print(type(my_dict))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

$ ./4-main.py
[1, 2, 3]
<class 'list'>
{'id': 12, 'is_active': True, 'name': 'John', 'info': {'age': 36, 'average': 3.14}, 'places': ['San Francisco', 'Tokyo']}
<class 'dict'>
[ValueError] Expecting property name enclosed in double quotes: line 2 column 25 (char 25)
```
### 5. Save Object to a file
Write a function that writes an Object to a text file, using a JSON representation:
- Prototype: ``def save_to_json_file(my_obj, filename):``
- You must use the ``with`` statement
- You don’t need to manage exceptions if the object can’t be serialized.
- You don’t need to manage file permission exceptions.
```bash
$ cat 5-main.py
#!/usr/bin/python3
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "my_list.json"
my_list = [1, 2, 3]
save_to_json_file(my_list, filename)

filename = "my_dict.json"
my_dict = { 
    'id': 12,
    'name': "John",
    'places': [ "San Francisco", "Tokyo" ],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
save_to_json_file(my_dict, filename)

try:
    filename = "my_set.json"
    my_set = { 132, 3 }
    save_to_json_file(my_set, filename)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

$ ./5-main.py
[TypeError] {3, 132} is not JSON serializable
$ cat my_list.json ; echo ""
[1, 2, 3]
$ cat my_dict.json ; echo ""
{"name": "John", "places": ["San Francisco", "Tokyo"], "id": 12, "info": {"average": 3.14, "age": 36}, "is_active": true}
$ cat my_set.json ; echo ""
```
### 6. Create object from a JSON file
Write a function that creates an Object from a “JSON file”:
- Prototype: ``def load_from_json_file(filename):``
- You must use the ``with`` statement
- You don’t need to manage exceptions if the JSON string doesn’t represent an object.
- You don’t need to manage file permissions / exceptions.
```bash
$ cat my_fake.json
{"is_active": true, 12 }
$ cat 6-main.py
#!/usr/bin/python3
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "my_list.json"
my_list = load_from_json_file(filename)
print(my_list)
print(type(my_list))

filename = "my_dict.json"
my_dict = load_from_json_file(filename)
print(my_dict)
print(type(my_dict))

try:
    filename = "my_set_doesnt_exist.json"
    my_set = load_from_json_file(filename)
    print(my_set)
    print(type(my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    filename = "my_fake.json"
    my_fake = load_from_json_file(filename)
    print(my_fake)
    print(type(my_fake))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

$ cat my_list.json ; echo ""
[1, 2, 3]
$ cat my_dict.json ; echo ""
{"name": "John", "places": ["San Francisco", "Tokyo"], "id": 12, "info": {"average": 3.14, "age": 36}, "is_active": true}
$ cat my_fake.json ; echo ""
{"is_active": true, 12 }
$ ./6-main.py
[1, 2, 3]
<class 'list'>
{'name': 'John', 'info': {'age': 36, 'average': 3.14}, 'id': 12, 'places': ['San Francisco', 'Tokyo'], 'is_active': True}
<class 'dict'>
[FileNotFoundError] [Errno 2] No such file or directory: 'my_set_doesnt_exist.json'
[ValueError] Expecting property name enclosed in double quotes: line 1 column 21 (char 20)
```
### 7. Load, add, save
Write a script that adds all arguments to a Python list, and then save them to a file:
- You must use your function ``save_to_json_file`` from ``5-save_to_json_file.py``
- You must use your function ``load_from_json_file`` from ``6-load_from_json_file.py``
- The list must be saved as a JSON representation in a file named ``add_item.json``
- If the file doesn’t exist, it should be created
- You don’t need to manage file permissions / exceptions.
```bash
$ cat add_item.json
cat: add_item.json: No such file or directory
$ ./7-add_item.py
$ cat add_item.json ; echo ""
[]
$ ./7-add_item.py Best School
$ cat add_item.json ; echo ""
["Best", "School"]
$ ./7-add_item.py 89 Python C
$ cat add_item.json ; echo ""
["Best", "School", "89", "Python", "C"]
``` 
### 8. Class to JSON
Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:
- Prototype: ``def class_to_json(obj):``
- ``obj`` is an instance of a Class
- All attributes of the ``obj`` Class are serializable: list, dictionary, string, integer and boolean
- You are not allowed to import any module
```bash
$ cat 8-my_class.py 
#!/usr/bin/python3
""" My class module
"""

class MyClass:
    """ My class
    """

    def __init__(self, name):
        self.name = name
        self.number = 0

    def __str__(self):
        return "[MyClass] {} - {:d}".format(self.name, self.number)

$ cat 8-main.py 
#!/usr/bin/python3
MyClass = __import__('8-my_class').MyClass
class_to_json = __import__('8-class_to_json').class_to_json

m = MyClass("John")
m.number = 89
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)

$ ./8-main.py 
<class '8-my_class.MyClass'>
[MyClass] John - 89
<class 'dict'>
{'name': 'John', 'number': 89}
$ 
$ cat 8-my_class_2.py 
#!/usr/bin/python3
""" My class module
"""

class MyClass:
    """ My class
    """

    score = 0

    def __init__(self, name, number = 4):
        self.__name = name
        self.number = number
        self.is_team_red = (self.number % 2) == 0

    def win(self):
        self.score += 1

    def lose(self):
        self.score -= 1

    def __str__(self):
        return "[MyClass] {} - {:d} => {:d}".format(self.__name, self.number, self.score)

$ cat 8-main_2.py 
#!/usr/bin/python3
MyClass = __import__('8-my_class_2').MyClass
class_to_json = __import__('8-class_to_json').class_to_json

m = MyClass("John")
m.win()
print(type(m))
print(m)

mj = class_to_json(m)
print(type(mj))
print(mj)

$ ./8-main_2.py 
<class '8-my_class_2.MyClass'>
[MyClass] John - 4 => 1
<class 'dict'>
{'number': 4, '_MyClass__name': 'John', 'is_team_red': True, 'score': 1}
```
### 9. Student to JSON
Write a class ``Student`` that defines a student by:
- Public instance attributes:
    + ``first_name``
    + ``last_name``
    + ``age``
- Instantiation with ``first_name``, ``last_name`` and age: ``def __init__(self, first_name, last_name, age):``
- Public method ``def to_json(self):`` that retrieves a dictionary representation of a ``Student`` instance (same as ``8-class_to_json.py``)
- You are not allowed to import any module
```bash
$ cat 9-main.py 
#!/usr/bin/python3
Student = __import__('9-student').Student

students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

for student in students:
    j_student = student.to_json()
    print(type(j_student))
    print(j_student['first_name'])
    print(type(j_student['first_name']))
    print(j_student['age'])
    print(type(j_student['age']))

$ ./9-main.py 
<class 'dict'>
John
<class 'str'>
23
<class 'int'>
<class 'dict'>
Bob
<class 'str'>
27
<class 'int'>
```
### 10. Student to JSON with filter
Write a class ``Student`` that defines a student by: (based on ``9-student.py``)
- Public instance attributes:
    + ``first_name``
    + ``last_name``
    + ``age``
- Instantiation with ``first_name``, ``last_name`` and age: ``def __init__(self, first_name, last_name, age):``
- Public method ``def to_json(self, attrs=None):`` that retrieves a dictionary representation of a ``Student`` instance (same as ``8-class_to_json.py``):
    + If ``attrs`` is a list of strings, only attribute names contained in this list must be retrieved.
    + Otherwise, all attributes must be retrieved
- You are not allowed to import any module
```bash
$ cat 10-main.py 
#!/usr/bin/python3
Student = __import__('10-student').Student

student_1 = Student("John", "Doe", 23)
student_2 = Student("Bob", "Dylan", 27)

j_student_1 = student_1.to_json()
j_student_2 = student_2.to_json(['first_name', 'age'])
j_student_3 = student_2.to_json(['middle_name', 'age'])

print(j_student_1)
print(j_student_2)
print(j_student_3)

$ ./10-main.py 
{'age': 23, 'last_name': 'Doe', 'first_name': 'John'}
{'age': 27, 'first_name': 'Bob'}
{'age': 27}
```
### 11. Student to disk and reload
Write a class ``Student`` that defines a student by: (based on ``10-student.py``)
- Public instance attributes:
    + ``first_name``
    + ``last_name``
    + ``age``
- Instantiation with ``first_name``, ``last_name`` and age: ``def __init__(self, first_name, last_name, age):``
- Public method ``def to_json(self, attrs=None):`` that retrieves a dictionary representation of a ``Student`` instance (same as ``8-class_to_json.py``):
    + If ``attrs`` is a list of strings, only attributes name contain in this list must be retrieved.
    + Otherwise, all attributes must be retrieved
- Public method ``def reload_from_json(self, json):`` that replaces all attributes of the ``Student`` instance:
    + You can assume ``json`` will always be a dictionary
    + A dictionary key will be the public attribute name
    + A dictionary value will be the value of the public attribute
- You are not allowed to import any module

Now, you have a simple implementation of a serialization and deserialization mechanism (concept of representation of an object to another format, without losing any information and allow us to rebuild an object based on this representation)
```bash
$ cat 11-main.py 
#!/usr/bin/python3
import os
import sys

Student = __import__('11-student').Student
read_file = __import__('0-read_file').read_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

path = sys.argv[1]

if os.path.exists(path):
    os.remove(path)

student_1 = Student("John", "Doe", 23)
j_student_1 = student_1.to_json()
print("Initial student:")
print(student_1)
print(type(student_1))
print(type(j_student_1))
print("{} {} {}".format(student_1.first_name, student_1.last_name, student_1.age))


save_to_json_file(j_student_1, path)
read_file(path)
print("\nSaved to disk")


print("Fake student:")
new_student_1 = Student("Fake", "Fake", 89)
print(new_student_1)
print(type(new_student_1))
print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))


print("Load dictionary from file:")
new_j_student_1 = load_from_json_file(path)

new_student_1.reload_from_json(j_student_1)
print(new_student_1)
print(type(new_student_1))
print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))

$ ./11-main.py student.json
Initial student:
<11-student.Student object at 0x7f832826eda0>
<class '11-student.Student'>
<class 'dict'>
John Doe 23
{"last_name": "Doe", "first_name": "John", "age": 23}
Saved to disk
Fake student:
<11-student.Student object at 0x7f832826edd8>
<class '11-student.Student'>
Fake Fake 89
Load dictionary from file:
<11-student.Student object at 0x7f832826edd8>
<class '11-student.Student'>
John Doe 23
$ cat student.json ; echo ""
{"last_name": "Doe", "first_name": "John", "age": 23}
```
### 12. Pascal's Triangle
**Technical interview preparation:**
Create a function ``def pascal_triangle(n):`` that returns a list of lists of integers representing the Pascal’s triangle of ``n``:
- Returns an empty list if ``n <= 0``
- You can assume ``n`` will be always an integer
- You are not allowed to import any module
```bash
$ cat 12-main.py
#!/usr/bin/python3
"""
12-main
"""
pascal_triangle = __import__('12-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

$ 
$ ./12-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```
### 13. Search and update
Write a function that inserts a line of text to a file, after each line containing a specific string (see example):
- Prototype: ``def append_after(filename="", search_string="", new_string=""):``
- You must use the ``with`` statement
- You don’t need to manage ``file permission`` or ``file doesn't exist`` exceptions.
- You are not allowed to import any module
```bash
$ cat 100-main.py
#!/usr/bin/python3
append_after = __import__('100-append_after').append_after

append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")

$ cat append_after_100.txt
At Holberton School,
Python is really important,
But it can be very hard if:
- You don't get all Pythonic tricks
- You don't have strong C knowledge.
$ ./100-main.py
$ cat append_after_100.txt
At School,
Python is really important,
"C is fun!"
But it can be very hard if:
- You don't get all Pythonic tricks
"C is fun!"
- You don't have strong C knowledge.
$ ./100-main.py
$ cat append_after_100.txt
At School,
Python is really important,
"C is fun!"
"C is fun!"
But it can be very hard if:
- You don't get all Pythonic tricks
"C is fun!"
"C is fun!"
- You don't have strong C knowledge.
```
### 14. Log parsing
Write a script that reads ``stdin`` line by line and computes metrics:
- Input format: ``<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>``
- Each 10 lines and after a keyboard interruption (``CTRL + C``), prints those statistics since the beginning:
    + Total file size: ``File size: <total size>``
    + where is the sum of all previous (see input format above)
    + Number of lines by status code:
        - possible status code: ``200``, ``301``, ``400``, ``401``, ``403``, ``404``, ``405`` and ``500``
        - if a status code doesn’t appear, don’t print anything for this status code
        - format: ``<status code>: <number>``
        - status codes should be printed in ascending order
```bash
$ cat 101-generator.py
#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()

$ ./101-generator.py | ./101-stats.py 
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
File size: 16305
200: 3
301: 3
400: 4
401: 2
403: 5
404: 5
405: 4
500: 4
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
Traceback (most recent call last):
  File "./101-stats.py", line 15, in <module>
Traceback (most recent call last):
  File "./101-generator.py", line 8, in <module>
    for line in sys.stdin:
KeyboardInterrupt
    sleep(random.random())
KeyboardInterrupt
```