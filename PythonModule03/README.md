# Description
This module introduces us to arguments and how to use them in different contexts as well as different ways to stock data (lists, tuples, sets and dictionaries) and generators.

# Instructions
To verify if the norm is correctly applied in the different files:
```bash
flake8
```
If there is an issue, the command will send back said issue. Otherwise, nothing will be sent back in the terminal.

To execute the program, once in the corresponding file, use:
```bash
python3 <name of the program>
```

# Notions

`len` can be used to count the number of arguments or items in a list.

## Arguments

`sys` is an import that controls the program input, output and error stream, and it supports reading multiple lines or redirected input.
Typing `import sys` at the beginning enables that.

`sys.argv` is a simple way to access command-line arguments as a list of strings.
`sys.argv[0]` is the first element (the program name), the ones after are the actual arguments that are always converted into strings. Therefore, in some cases, it may need to be converted to the correct data type when working with numbers or other values.

`sys.argv[1:]` when used in a for loop, it will start at the first argument after the name of the program.

## Lists
`Lists` are a series of organised data.

## Tuples

`Tuples` are like lists, it can stock data, but unlike them, we can't change it afterwards, it "protects" it. It's defined with parentheses.
```bash
a = (1, 2, 3)
```
If we want to retrieve / unpack the data inside a tuple, two possibilities exist:
- c = b[0]
- d, = b
In both cases, b is the tuple.

Using `tuple()` can also be used to define a tuple.

## Sets

`Sets` are like lists but they are unordered, unchangeable (you can still add or remove items), and unindexed. They **don't allow duplicates**. It's defined with curly brackets
```bash
a = {1, 2, 3}
```

`union()` joins multiple sets together while ignoring duplicates

`intersection()` brings every common element(s) between different sets

`difference()` brings the unique element(s) of a set compared to the others

Using `set()` can also be used to define a set.

## Dictionaries

`Dictionaries` are meant to store data using keys and values.They are ordered changeable and **don't allow duplicates**. Like sets, they are defined with curly brackets.
```bash
a = {
	key1: value1,
	key2: value2,
	key3: value3
}
```

Using `dict()` can also be used to define a dictionary.
`update()` is a method inserting the specified items in the dictionary when used that way:
```bash
dictionary.update({key: value})
```

## Generators

A generator function will return an iterator object. It uses `yield` to produce a series of results over time.
`yield` pauses the function's execution, returns the value and maintains its state between iterations. That way, the function will continue where it left off at the next call.
On the other hand, `return` will end the function and won't retain its state. It's more suitable when a single result is expected from the function.
The generator's presence will help the program be faster as it won't store as much data as if it were a list or something of the kind

# Resources

## Notions:

[sys](https://www.geeksforgeeks.org/python/python-sys-module/)

[sys.argv](http://codecademy.com/article/command-line-arguments-in-python)

[Tuples](https://courspython.com/tuple.html)

[Sets](https://www.w3schools.com/python/python_sets.asp)

[Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)

[MoreDitionaries](https://www.freecodecamp.org/news/create-a-dictionary-in-python-python-dict-methods/#define-empty)

[Generators](https://www.geeksforgeeks.org/python/generators-in-python/)
