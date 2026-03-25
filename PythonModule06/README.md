# Description
This module introduces us to imports and how they work.

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
The file `__init__.py` file enables the user to transform ordinary folders into packages. That way, the folder can be used for imports.
Any Python file is a module, it's defined by the `.py` found after the file's name. On the other hand, a package will contain every module present in the same file as `__init__.py`

Imports enable the user to use different functions from different libraries or files created by the user. Different ways to import files exist, such as:
- `import <file_name>` this will import the entire file
  | Advantages | Disadvantages |
  | --- | --- |
  | Access to everything in the module | / |
  | Readability | / |
- `from <file_name> import <function1>, <function2>,...` this method will import the function from a file one by one, it is needed to write every function name that will be used
  | Advantages | Disadvantages |
  | --- | --- |
  | Access to something specific within the module | Readability (Might not realize it's imported) |
  | Don't have to prepend with the module's name | / |
- `import <file_name> as <chosen_name>` this will import the entire file under a name chosen by the user
  | Advantages | Disadvantages |
  | --- | --- |
  | Access to everything in the module | Readability (Other programmers might not know the library unless they are familiar) |
  | You can choose the module's name (and make it shorter) | / |
- `from <file_name> import *` (not used here) this will import the entire file
  | Advantages | Disadvantages |
  | --- | --- |
  | Access to everything in the module | Readability (Might not realize it's imported) |
  | Don't have to prepend with the module's name | / |

There are two types of imports: absolute and relative.
Absolute imports will write the pathway to the file like so: `from package1.module1 import function1`
  | Advantages | Disadvantages |
  | --- | --- |
  | Are clear and straightforward | Can become lengthy if the pathway is long |
  | Remains valid if the current location of the statement changes | / |
Relative imports will specify the resource to be imported relative to the current location like so: `from .module1 import function1` or `from ..module1 import function1` or even `from . import function1`
  | Advantages | Disadvantages |
  | --- | --- |
  | Are succinct, it can turn a ridiculously long statement into something simpler | Can be messy for shared projects where directory structure is likely to change |
  | / | Readability |

Circular imports occur when two or more modules depend on each other.
Late import, dependency injection and shared module are ways to counter circular dependencies.

# Resources

## Notions:

- [Module vs Package](https://stackoverflow.com/questions/7948494/whats-the-difference-between-a-module-and-package-in-python)

- [Different import methods](https://www.youtube.com/watch?v=iHN5ReXemrw)

- [Absolute vs Relative](https://realpython.com/absolute-vs-relative-python-imports/#absolute-imports)

- [lazy import](https://medium.com/totalenergies-digital-factory/when-lazy-is-good-lazy-import-10bfae7abeb7)

- [Circular import](https://www.datacamp.com/tutorial/python-circular-import)
