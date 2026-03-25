# Description
This module introduces us to abstract classes and how they work.

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

## Notions
An abstract class is a class that cannot be instantiated on its own and is designed to be a blueprint for other classes. They allow us to define methods that must be implemented by subclasses.
We can use them when we want to:
- Define a common interface for all subclasses
- Enforce implementation of certain methods in child classes
- Provide a shared functionality while still requiring subclasses to implement specific behavior

Method overriding occurs when a subclass defines a method with the same name, same parameters, and same return type as a method in its superclass. When you call this method on an instance of the subclass, the subclass version is executed instead of the superclass version.

What makes this approach more powerful than separate processing functions?
The code will be clearer to read and by creating a base method, implementing it on a new subclass would be easier.

Difference between method overriding and polymorphism is that method overriding is when you call a method in the subclass with the same signature as the one in the superclass.
Polymorphism is when you are not sure of the object's type at runtime, the behaviors method may differ depending on this.
Overriding is a type of polymorphism.

How does the combination of method overriding and subtype polymorphism enable building scalable, maintainable data processing systems?
By allowing functions and classes to operate on objects of different types with shared interfaces.

What real-world engineering problems does this approach solve?
Designing scalable software systems, Machine Learning Libraries, Database Access or Graphics Engines.

# Resources

## Notions:

- [Abstract Classes](https://www.geeksforgeeks.org/python/abstract-classes-in-python/)

- [Overriding](https://algomaster.io/learn/python/method-overriding)

- [Logging Levels](http://docs.python.org/3/library/logging.html#logging-levels)

- [Protocol](https://dev.to/shameerchagani/what-is-a-protocol-in-python-3fl1)

- [Polymorphism](https://www.acte.in/what-is-polymorphism-in-python#Real)

## Github:

- [shadox254](https://github.com/shadox254/Module-Python/tree/main/Module-05)
