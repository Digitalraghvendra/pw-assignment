# -*- coding: utf-8 -*-
"""function assignment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1G7dZMZ-sVYdfs7XIsWbjlK3K27_PycIT

# ***FUNCTION ASSIGNMENT***

# ***Theory questions:***


Question-1 What is the difference between a function and a method in Python?


Answer-
In Python, a function is a standalone block of code that can be called multiple times, whereas a method is a function that belongs to a class or object, and is used to perform actions on that object.


Question-2 Explain the concept of function arguments and parameters in Python.

Answer-
In Python, function arguments and parameters refer to the values passed to a function when it's called.

Parameters: These are the names given to the variables in the function definition. They are the placeholders for the values that will be passed to the function.

Arguments: These are the actual values passed to a function when it's called. They are assigned to the corresponding parameters in the function definition.

Example:

def greet(name):  # 'name' is a parameter
  print("Hello, " + name)

greet("John")  # 'John' is an argument



Question-3  What are the different ways to define and call a function in Python?


Answer-
In Python, functions can be defined and called in several ways:

Defining Functions.
1. Standard function definition.
2. Lambda function.
3. Nested function.

Calling functions
1. Standard function call.
2. keyword argument function call.
3. Variable number of Arguments function call.
4. Default Argument function call.


Question-4 What is the purpose of the 'return' statement in a Python function?

Answer-
The return statement in a Python function serves two purposes:

1. Exiting the function: When a return statement is encountered, the function immediately stops executing and returns control to the caller.

2. Returning a value: The return statement can also be used to return a value from the function to the caller. This value can be any Python object, such as a number, string, list, or dictionary.


Question-5 What are iterators in Python and how do they differ from iterables?

Answer-
In Python:

- Iterables: Are objects that can be looped through, such as lists, tuples, dictionaries, and sets. They can be passed to the iter() function to create an iterator.

- Iterators: Are objects that keep track of their position within an iterable and yield values one at a time. They are created by calling iter() on an iterable.


Question-6  Explain the concept of generators in Python and how they are defined.

Answer-
In Python, a generator is a special type of function that can be used to generate a sequence of values instead of computing them all at once and returning them in a list, for example.

Generators are defined using a function definition with the yield keyword instead of return. When a generator is called, it returns an iterator object, which can be used to iterate over the generated values.

Here's an example of a simple generator:

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

To use the generator, you can call it and iterate over the returned iterator object:

seq = infinite_sequence()
for _ in range(10):
    print(next(seq))

This will print the numbers 0 through 9.


Question-7  What are the advantages of using generators over regular functions?

Answer-

The advantages of using generators over regular functions in Python are:

1. Memory Efficiency: Generators use significantly less memory, as they only store the current state of the iteration, rather than storing the entire sequence in memory.

2. Lazy Evaluation: Generators only compute the next value when asked, which can be beneficial for computationally expensive operations or infinite sequences.

3. Flexibility: Generators can be used to implement cooperative multitasking, allowing for efficient handling of concurrent tasks.

4. Improved Performance: Generators can be faster than regular functions, especially when dealing with large datasets, since they avoid the overhead of creating and returning a list.

1. Easier Implementation of Infinite Sequences: Generators make it simple to implement infinite sequences, which would be impractical or impossible with regular functions.



Question-8 What is a lambda function in Python and when is it typically used?

Answer-
A lambda function in Python is a small, anonymous function that can take any number of arguments, but can only have one expression. It's typically used when a small, one-time-use function is needed.

The general syntax of a lambda function is:

lambda arguments: expression

Lambda functions are often used in situations such as:

1. Event handling: As event handlers, where a small, one-time-use function is needed.
2. Data processing: When working with data structures, such as lists or dictionaries, and a small, one-time-use function is needed to perform a specific operation.
3. Map(), filter(), and reduce() functions: As arguments to these higher-order functions, which apply a function to each item in an iterable.
4. One-time-use functions: When a function is only needed once, and defining a separate named function would be unnecessary.


Question-9 Explain the purpose and usage of the map() function in Python.

Answer-
The map() function in Python applies a given function to each item of an iterable (such as a list, tuple, or string) and returns a map object, which is an iterator.

Purpose:

The map() function is used to:

1. Apply a transformation to each element of an iterable.
2. Create a new iterable with the transformed elements.

Usage:

The general syntax of the map() function is:

map(function, iterable)

Where:

- function is the function to be applied to each element of the iterable.
- iterable is the iterable (such as a list, tuple, or string) whose elements will be transformed.

Example:

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

In this example, the square() function is applied to each element of the numbers list using the map() function, and the resulting squared numbers are collected in a new list called squared_numbers.

Note that in Python 3.x, the map() function returns an iterator, so we need to use the list() function to convert it to a list. In Python 2.x, map() returns a list directly.


Question-10 What is the difference between 'map()", "reduce()', and 'filter() functions in Python?

Answer-
In Python, map(), reduce(), and filter() are three fundamental functions that operate on iterables. Here's a brief overview of each:

Map()

- Applies a given function to each item of an iterable.
- Returns a map object, which is an iterator.
- Syntax: map(function, iterable)

Example:

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]


Reduce()

- Applies a given function to the first two items of an iterable, then to the result and the next item, and so on.
- Returns a single value, which is the result of the reduction.
- Syntax: reduce(function, iterable)

Note: In Python 3.x, reduce() is moved to the functools module. You need to import it before using: from functools import reduce

Example:

import functools
numbers = [1, 2, 3, 4, 5]
product = functools.reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120


Filter()

- Constructs an iterator from elements of an iterable for which a function returns True.
- Returns a filter object, which is an iterator.
- Syntax: filter(function, iterable)

Example:

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]


In summary:

- map() applies a function to each item of an iterable.
- reduce() applies a function to the first two items of an iterable, then to the result and the next item, and so on.
- filter() constructs an iterator from elements of an iterable for which a function returns True.


Question-11 write the internal mechanism for sum operation using reduce function on this given list: [47,11,42,13];


Answer-
Here's the internal mechanism for the sum operation using the reduce function on the given list:

Given list: [47, 11, 42, 13]

Reduce function: reduce(lambda x, y: x + y, [47, 11, 42, 13])

Internal mechanism:

1. x = 47, y = 11 => x + y = 58
2. x = 58, y = 42 => x + y = 100
3. x = 100, y = 13 => x + y = 113

Result: 113

Note: The lambda function lambda x, y: x + y is applied to the first two elements of the list, then to the result and the next element, and so on, until the list is exhausted.
"""



"""# ***Practical Questions:***

Question-1 Write a Python function that takes a list of numbers as input and returns the sum of all even numbers in the list.

"""

def sum_even_numbers(numbers):
    """
    Returns the sum of all even numbers in the input list.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The sum of all even numbers in the list.
    """
    return sum(num for num in numbers if num % 2 == 0)

# Example usage:
numbers = [1, 2, 3, 4, 5, 6]
result = sum_even_numbers(numbers)
print("Sum of even numbers:", result)

"""Question-2 Create a Python function that accepts a string and returns the reverse of that string."""

def reverse_string(s):
    """
    Returns the reverse of the input string.

    Args:
        s (str): The input string.

    Returns:
        str: The reverse of the input string.
    """
    return s[::-1]

# Example usage:
input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print("Reversed String:", reversed_string)

"""Question-3 Implement a Python function that takes a list of integers and returns a new list containing the squares of each number."""

def square_numbers(numbers):
    """
    Returns a new list containing the squares of each number in the input list.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A new list containing the squares of each number.
    """
    return [num ** 2 for num in numbers]

# Example usage:
numbers = [1, 2, 3, 4, 5]
squared_numbers = square_numbers(numbers)
print("Squared Numbers:", squared_numbers)

"""Question-4 Write a Python function that checks if a given number is prime or not from 1 to 200."""

def check_prime_numbers(n):
    """
    Checks if a number is prime or not.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Check prime numbers from 1 to 200
for num in range(1, 201):
    if check_prime_numbers(num):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

"""Question-5 Create an iterator class in Python that generates the Fibonacci sequence up to a specified number of terms."""

class FibonacciIterator:
    def __init__(self, n):
        self.n = n
        self.a, self.b = 0, 1
        self.current_term = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_term >= self.n:
            raise StopIteration
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.current_term += 1
        return result

# Example usage:
fib_iterator = FibonacciIterator(10)
for num in fib_iterator:
    print(num)

"""Question-6 Write a generator function in Python that yields the powers of 2 up to a given exponent."""

def powers_of_two(exponent):
    for i in range(exponent + 1):
        yield 2 ** i

# Example usage:
for power in powers_of_two(5):
    print(power)

"""Question-7 Implement a generator function that reads a file line by line and yields each line as a string."""

def read_file_lines(file_path):
    """
    Reads a file line by line and yields each line as a string.

    Args:
        file_path (str): The path to the file.

    Yields:
        str: Each line of the file.
    """
    try:
        with open(file_path, 'r') as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

#Example usage:
file_path = 'example.txt'
for line in read_file_lines(file_path):
    print(line)

"""This generator function works as follows:

1. The function opens the file in read mode ('r') using a with statement, which ensures the file is properly closed after it is no longer needed.
2. The function uses a for loop to iterate over each line in the file.
3. Inside the loop, the yield statement produces each line as a string, stripped of any leading or trailing whitespace using the strip() method.
4. If the file does not exist, the function catches the FileNotFoundError exception and prints an error message.

"""



"""Question-8 Use a lambda function in Python to sort a list of tuples based on the second element of each tuple.

"""

# Define the list of tuples
tuples_list = [(3, 6), (1, 9), (2, 4), (5, 1), (7, 8)]

# Use a lambda function as the key for the sort() method
tuples_list.sort(key=lambda x: x[1])

# Print the sorted list
print(tuples_list)

"""Question-9 Write a Python program that uses "map() to convert a list of temperatures from Celsius to Fahrenheit."""

# Define a function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Define a list of temperatures in Celsius
celsius_temperatures = [0, 10, 20, 30, 40]

# Use map() to convert the temperatures to Fahrenheit
fahrenheit_temperatures = list(map(celsius_to_fahrenheit, celsius_temperatures))

# Print the converted temperatures
print("Celsius Temperatures:", celsius_temperatures)
print("Fahrenheit Temperatures:", fahrenheit_temperatures)

"""Question-10 Create a Python program that uses "filter()" to remove all the vowels from a given string."""

# Define a function to check if a character is a vowel
def is_vowel(char):
    return char.lower() in 'aeiou'

# Define a string
input_string = "Hello, World!"

# Use filter() to remove vowels from the string
vowel_free_string = ''.join(filter(lambda x: not is_vowel(x), input_string))

# Print the original and vowel-free strings
print("Original String:", input_string)
print("Vowel-Free String:", vowel_free_string)

"""Question-11 Imagine an accounting routine used in a book shop. It works on a list with sublists, which look like this:

Order Number

34587

98762

77226

88112

Book Title and Author

Learning Python, Mark Lutz

Programming Python, Mark Lutz

Head First Python, Paul Barry

Einführung in Python3, Bernd Klein

Quantity

4

5

3

3

Price per Item

40.95

56.80

32.95

24.99

Write a Python program, which returns a list with 2-tuples. Each tuple consists of the order number and the product of the price per item and the quantity. The product should be increased by 10,- C if the value of the order is smaller than 100,00 €.

Write a Python program using lambda and map.
"""

# Define the data
orders = [
    [34587, "Learning Python, Mark Lutz", 4, 40.95],
    [98762, "Programming Python, Mark Lutz", 5, 56.80],
    [77226, "Head First Python, Paul Barry", 3, 32.95],
    [88112, "Einführung in Python3, Bernd Klein", 3, 24.99]
]

# Use map and lambda to calculate the order values
order_values = list(map(
    lambda order: (order[0], order[3] * order[2] + (10 if order[3] * order[2] < 100 else 0)),
    orders
))

# Print the result
print(order_values)

