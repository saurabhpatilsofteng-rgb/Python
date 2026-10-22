# Python Fundamentals — Beginner to Advanced

## 1. Introduction to Python

Python is a high-level, general-purpose programming language known for its readable syntax and extensive ecosystem.

### Uses of Python
- **Backend development:** Build web applications and REST APIs using FastAPI and Django.
- **Artificial intelligence and machine learning:** Develop models using TensorFlow and other ML libraries.
- **Data analysis:** Process, analyze, and visualize data.
- **Automation and scripting:** Automate repetitive tasks and system operations.
- **Application integration:** Connect frontend applications with backend services through APIs.
- **Data engineering:** Process and transform large amounts of data.

## 2. Variables and Data Types

A variable is a name that refers to a value. Python determines the type of a value at runtime, so you do not need to declare a variable's type explicitly.

### Important data types

| Data type | Example | Purpose |
|---|---|---|
| `int` | `25` | Whole numbers |
| `float` | `45.50` | Decimal numbers |
| `str` | `"Python"` | Text |
| `bool` | `True` | Boolean values: `True` or `False` |
| `NoneType` | `None` | Represents the absence of a value |
| `list` | `[10, 20, 30]` | Ordered, mutable collection |
| `tuple` | `(10, 20, 30)` | Ordered, immutable collection |
| `set` | `{10, 20, 30}` | Collection of unique elements |
| `dict` | `{"name": "Amit"}` | Key-value pairs |

### Topics to learn
- Variable naming rules
- Dynamic typing
- Type checking using `type()`
- Type conversion using `int()`, `float()`, `str()` and `bool()`
- Mutable vs. immutable objects
- `is` vs. `==`

## 3. Operators and Input/Output

Operators perform calculations, comparisons, and logical operations.

### Topics to learn
- Arithmetic operators
- Comparison operators
- Logical operators: `and`, `or`, `not`
- Assignment operators
- Membership operators: `in`, `not in`
- Identity operators: `is`, `is not`
- User input using `input()`
- Output using `print()`
- String formatting using f-strings
- Operator precedence

## 4. Conditional Statements and Loops

Conditional statements control which code executes. Loops repeat a block of code.

### Topics to learn
- `if`, `elif`, `else`
- Nested conditions
- `for` loops
- `while` loops
- `range()`
- `break`, `continue`, `pass`
- Nested loops
- Looping through strings and collections
- List comprehensions

## 5. Python Collections

Collections allow you to store and manage multiple values.

### Lists
- Creating and accessing lists
- Indexing and slicing
- Adding and removing elements
- Updating elements
- Sorting and reversing
- List methods
- Nested lists
- List comprehensions

### Tuples
- Creating tuples
- Indexing and slicing
- Tuple unpacking
- Tuple methods
- Immutability

### Sets
- Creating sets
- Adding and removing elements
- Union, intersection and difference
- Removing duplicates
- Set comprehensions

### Dictionaries
- Creating dictionaries
- Accessing and updating values
- Adding and deleting key-value pairs
- `keys()`, `values()`, `items()`
- `get()`, `update()`, `pop()`
- Nested dictionaries
- Dictionary comprehensions

## 6. Functions

A function is a reusable block of code that performs a specific task.

### Topics to learn
- Defining functions using `def`
- Calling functions
- Parameters and arguments
- The `return` statement
- Positional arguments
- Default arguments
- Keyword arguments
- Variable-length arguments: `*args` and `**kwargs`
- Positional-only and keyword-only parameters
- Multiple return values
- Local and global scope
- The `global` and `nonlocal` keywords
- Recursion
- Type hints
- Docstrings

## 7. Lambda Functions

A lambda function is a small anonymous function defined using the `lambda` keyword.

### Topics to learn
- Lambda syntax
- Lambda with one or more arguments
- Lambda with `map()`
- Lambda with `filter()`
- Lambda with `sorted()` and its `key` parameter
- Lambda vs. regular functions
- When to use and avoid lambda functions

## 8. String Handling and Comparisons

Strings represent text and are immutable in Python.

### Topics to learn
- Creating strings
- Indexing and slicing
- String concatenation and repetition
- String methods: `strip()`, `split()`, `join()`, `replace()`
- Searching with `find()` and `in`
- String formatting with f-strings
- String comparisons
- Case-sensitive comparisons
- Comparing strings using `==`, `!=`, `<` and `>`
- Escape characters and raw strings
- String immutability

## 9. Modules and Packages

A module is a Python file that can be imported into another file. A package organizes related modules into a directory structure.

### Topics to learn
- Importing modules with `import` and `from`
- Built-in modules such as `math`, `random` and `datetime`
- Creating custom modules
- Creating packages
- The `__init__.py` file
- Import aliases using `as`
- The `if __name__ == "__main__":` pattern
- Installing packages using `pip`
- Virtual environments using `venv`
- Managing dependencies with `requirements.txt`

## 10. File Handling and Exceptions

File handling allows programs to read and write data. Exception handling allows programs to respond to runtime errors gracefully.

### File handling
- Opening files with `open()`
- Reading files
- Writing and appending data
- File modes: `r`, `w`, `a`, `x`, `b`
- Using `with` to manage files safely
- Working with text files and CSV files
- Reading and writing configuration files

### Exception handling
- Syntax errors vs. runtime exceptions
- `try` and `except`
- Handling specific exceptions
- `else` and `finally`
- Raising exceptions using `raise`
- Creating custom exceptions
- Resource cleanup and safe error handling

## 11. Working with JSON

JSON (JavaScript Object Notation) is a common data format used by REST APIs and configuration files.

### Topics to learn
- JSON objects and arrays
- Python dictionaries and lists vs. JSON objects and arrays
- `json.dumps()` — Python object to JSON string
- `json.loads()` — JSON string to Python object
- `json.dump()` — Write JSON to a file
- `json.load()` — Read JSON from a file
- Pretty-printing with `indent`
- Handling invalid JSON
- Serializing and deserializing data
- Returning JSON responses from FastAPI

## 12. Object-Oriented Programming (OOP)

OOP organizes code around classes and objects. It is useful for modeling entities such as employees, customers, products and bank accounts.

### Topics to learn
- Classes and objects
- Attributes and methods
- The `__init__()` constructor
- The `self` parameter
- Instance, class and static methods
- Instance variables and class variables
- Encapsulation
- Inheritance
- Polymorphism
- Abstraction
- Method overriding
- Multiple inheritance
- Composition vs. inheritance
- Properties using `@property`
- Special methods such as `__str__()` and `__repr__()`

## 13. Dataclasses

Dataclasses reduce repetitive code for classes primarily used to store data.

### Topics to learn
- The `@dataclass` decorator
- Automatically generated `__init__()` and `__repr__()`
- Type annotations
- Default values
- `field()` and mutable defaults
- Frozen dataclasses
- Comparing dataclasses
- Dataclasses vs. regular classes
- Dataclasses vs. Pydantic models

## 14. Advanced Python

### 14.1 Iterators and Iterables
An iterable is an object you can loop over. An iterator produces values one at a time.

- `iter()` and `next()`
- The iterator protocol
- Creating custom iterators
- `StopIteration`
- Lazy evaluation

### 14.2 Generators
- The `yield` keyword
- Generator functions
- Generator expressions
- Memory-efficient processing
- `yield` vs. `return`

### 14.3 Decorators
- Functions as first-class objects
- Functions inside functions
- Passing functions as arguments
- Returning functions
- Creating decorators
- `*args` and `**kwargs` in decorators
- `functools.wraps`
- Practical uses such as logging and timing

### 14.4 Context Managers
- The `with` statement
- Resource management
- `__enter__()` and `__exit__()`
- Creating context managers
- The `contextlib` module

### 14.5 Comprehensions
- List comprehensions
- Dictionary comprehensions
- Set comprehensions
- Generator expressions
- Conditional comprehensions
- Readability vs. performance

### 14.6 Advanced Function Concepts
- Closures
- Higher-order functions
- Functional programming basics
- `map()`, `filter()` and `reduce()`
- Unpacking with `*` and `**`

### 14.7 Memory Management
- Object references
- Mutable vs. immutable objects
- Shallow copy vs. deep copy
- Reference counting
- Garbage collection
- Identity and equality

### 14.8 Concurrency and Parallelism
- Processes vs. threads
- The `threading` module
- The `multiprocessing` module
- Asynchronous programming
- `async` and `await`
- `asyncio`
- The Global Interpreter Lock (GIL)
- Choosing the right approach for I/O-bound and CPU-bound tasks

### 14.9 Type Hints and Validation
- Type annotations
- Optional values and union types
- Generic types
- Type aliases
- Static type checking
- `TypedDict`
- Runtime validation with Pydantic

### 14.10 Testing and Debugging
- Unit testing with `unittest` or `pytest`
- Assertions
- Fixtures and parametrized tests
- Mocking dependencies
- Logging
- Debugging with breakpoints
- Profiling and performance measurement

## 15. Working with APIs and Databases

### HTTP and REST APIs
- HTTP methods: GET, POST, PUT, PATCH and DELETE
- Status codes
- Request headers and response bodies
- JSON request and response data
- Authentication and authorization
- Calling APIs using `requests` or an asynchronous HTTP client

### Database integration
- SQL fundamentals
- Connecting Python to PostgreSQL
- CRUD operations
- Parameterized queries
- Transactions and rollback
- Connection pooling
- ORM fundamentals
- SQLAlchemy basics

## 16. Python for Backend Development with FastAPI

- Creating a FastAPI project
- Routes and path parameters
- Query parameters
- Request bodies
- Pydantic models
- Data validation
- Response models
- Dependency injection
- Exception handling
- Async endpoints
- Database integration
- Authentication with OAuth2 and JWT
- Middleware and CORS
- Automated API documentation
- Unit and integration testing
- Docker and deployment

## 17. Python for AI and Machine Learning

### Fundamentals
- NumPy arrays and vectorized operations
- Pandas DataFrames
- Data cleaning and preprocessing
- Basic statistics and linear algebra

### Machine learning
- Supervised and unsupervised learning
- Training and testing datasets
- Features and labels
- Model training and evaluation
- Overfitting and underfitting
- Saving and loading models

### TensorFlow
- Tensors, shapes and data types
- Tensor operations
- Variables and automatic differentiation
- Keras models and layers
- Loss functions and optimizers
- Training loops
- Model evaluation
- Saving and loading models
- Serving predictions through FastAPI

## 18. Real-World Python Project

Build an Employee Prediction API that integrates with your Java backend.

1. Use Python to preprocess employee data.
2. Train a TensorFlow model to predict a defined business outcome.
3. Save the trained model.
4. Create a FastAPI endpoint that returns predictions.
5. Store employee data and prediction results in PostgreSQL.
6. Call the Python API from Spring Boot using Java's `RestClient`.
7. Use Spring AI and Ollama to explain predictions in natural language.
8. Add tests, input validation, logging, Docker and deployment.
9. Optionally expose approved application functions through MCP for AI clients.

**Recommended learning order:** Python fundamentals → functions and collections → OOP → files and JSON → advanced Python → NumPy and Pandas → FastAPI → PostgreSQL → TensorFlow → Spring Boot integration → Spring AI and MCP.
