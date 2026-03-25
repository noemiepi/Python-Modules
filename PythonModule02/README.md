# Description
This module introduces us to the different error types, how to use them and how to create custom errors.

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

# Error types
A few different errors exist within Python:
- `ValueError`: when you receive the wrong type of data, for instance: you receive "abc" instead of a number
- `ZeroDivisionError`: when you try to divide by 0
- `FileNotFoundError`: when you try to open a file that doesn't exist
- `KeyError`: when you look for a key that isn't in a dictionary

Python has different error types to notify the user which kind of problem it is, that way they can differentiate between a `ValueError` where a wrong conversion is happening and a `ZeroDivisionError` where it's a division by zero that crashes the program.

Using functions like `try`, `except`, `finally` and `raise`, we have the possibility to anticipate errors and create new ones. They can be used like so:
```bash
try:
	<condition(s)>
except <error type>:
	print("<error message of your choosing>")
finally:
	print("<final message>")
```
The condition put in the `try` function will be tested one by one until it either went through all of them or it encounters the expected error cited below it.
The `finally` function will always apply once it's done with `try` and/or `except`.
When there is an error, a cleanup is important because it can avoid ressource leaks and improper program termination
A few examples can be:
- closing a file after opening it
- release external resources
- close network connections
For `raise`, it will be noted that way:
```bash
raise <error name>("message that will appear when encountering said error")
```
> [!note]
> 'error name' can either be a pre-existing error or a created error.
> We can also put a variable or use a function in the message by using it like a `print` function.
A program needs to raise errors when it can crash because of it or to alert the user of a problem early on such as a water level that's too low, it won't crash the program but will help the user take care of it.

The difference between raising and catching an error is that `raise` enables us to use a specific exception while catching would stop the program when meeting said exception or another error.
On the other hand, the difference between handling and raising errors is that handling can make the user aware of multiple errors while raising will stop at the first error it encounters.

To create an error without using a pre-existing one like `ValueError`, the use of a class will be needed, like such:
```bash
class ErrorName(Exception):
	pass
```
`Exception` is a pre-existing class that can be used to create errors. By making our ErrorName inherit its traits, we can now use it like any other error types. We just need, beforehand, to use `raise` to define the error message.

# Resources

## Notions:

[ValueError](https://www.docstring.fr/formations/faq/resolution-derreurs/que-signifie-une-erreur-de-type-valueerror/)

[Testing_ValueError](https://www.w3schools.com/python/ref_exception_valueerror.asp)

[FileNotFoundError](https://www.docstring.fr/formations/faq/resolution-derreurs/que-signifie-une-erreur-de-type-filenotfounderror/)

[KeyError](https://www.docstring.fr/formations/faq/resolution-derreurs/que-signifie-une-erreur-de-type-keyerror/)

[Try_Except_and_Raise](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)


## Github:

[Overtek](https://github.com/Overtekk/Python-Module-00-10/tree/main/Python%20Module%2002)
