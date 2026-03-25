# Description
This module continues introducing us to Python notions. Here, following the garden allegory of module 00, we will learn:
- how Python programs are structured and executed
- how to organize complex data structure efficiently using a `class`
- how to protect data

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

# Material
To create a main, the command needed in the file is:
```bash
if __name__ == "__main__":
```

A `class` will serve to store different attributes and methods that can use said attributes.
You can define it using only `class` followed by the name.
`def __init__()` will define the attribute and the function is declared as usual, you only need to add `self` in the parameters, that you can use the attributes defined earlier.
Once defined the value stored in the attributes can be modified like any variable by using a function defined inside the class.

Lists can be used to create multiple objects from one or more classes. Using a loop after can efficiently display the information of each object.

A class can inherit characteristics from a parent class. By defining it like so:
```bash
class Child(Parent):
```
The child class can inherit form its parent class. Defining the attributes stays roughly the same `def __init__()` and then add the line `super().__init__()` to make the child class inherit its parent attributes. It should look like this:
```bash
class Child(Parent):
	def __init__(attribute1, attribute2, attribute3)
		super().__init__(attribute1=attribute1, attribute2=attribute2)
		self.attribute3 = attribute3
```
Here `attribute1` and `attribute2` are inherited attributes from the parent class and `attribute3` is a new attribute exclusive to the child class.

Class method can be created inside of a class using `@classmethod` before the function. For this kind of method, it will be defined like such:
```bash
@classmethod
def methodname(cls) -> type:
```
Here, `cls` is accessed by class name where the one with `self` is accessed by the instance of the class

A static method can be created inside of a class using `@staticmethod` before the method. It does not receive an implicit first argument such as `self` or `cls`. It's defined like this:
```bash
@staticmethod
def methodname() -> type:
```

Three types of encapsulation exist:
- Public: `self.name`
- Private: `self._name`
- Protected: `self.__name`
It will, depending on its type, protect the variable's data:
- `_` indicate that its protected and meant to be used only in a class or subclass
- `__` defines a private method only accessible within the class because its name is altered within the program to protect the method
It will, overall, protect the data from accidentally being corrupted

A getter will read the data. A setter will update the data with an optional validation or a restriction

# Resources

## Notions:

[Class](https://blog.alphorm.com/definir-des-classes-en-python#definir-une-classe-et-ses-attributs-en-python)

[Super_function](https://www.geeksforgeeks.org/python/encapsulation-in-python/)

[Encapsulation](https://www.geeksforgeeks.org/python/encapsulation-in-python/)

[Inheritence](https://www.docstring.fr/glossaire/heritage/)

[Self_and_cls](https://stackoverflow.com/questions/4613000/difference-between-cls-and-self-in-python-classes)

[Class_method](https://docs.python.org/3/library/functions.html#classmethod)

[Static_method](https://docs.python.org/3/library/functions.html#staticmethod)


## Githubs:

[Overtek](https://github.com/Overtekk/Python-Module-00-10/tree/main/Python%20Module%2001)

[alizealebaron](https://github.com/alizealebaron/python_module/tree/main/python_module_01)

[shadox254](https://github.com/shadox254/Module-Python/tree/main/Module-01)
