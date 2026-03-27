# Description
This module continues module 05's introduction to abstract classes in the context of the creation of a card game.

# Instructions
To verify if the norm is correctly applied in the different files:
```bash
flake8
```
If there is an issue, the command will send back said issue. Otherwise, nothing will be sent back in the terminal.

To execute the program, once in the corresponding file, use:
```bash
python3 -m <exercise file name>.main
```

# Notions
How do abstract base classes ensure consistency across different card types?
By "forcing" the implementation of abstract methods to every child from an abstract parent.

What happens if you try to create a Card directly without implementing required methods?
The object from that class can't be created without a missing abstract method and therefore the program crashes.

How does polymorphism enable the Deck to work with any card type?
Polymorphism is when you are not sure of the object's type at runtime, the behaviors method may differ depending on this. Thereore, you can adapt the functions beheviors depending on the card type.

What are the benefits of this design pattern for card game systems?
By creating a base method, every subclass, here card type, inherits of the same functions. Overall, the code will be clearer to read and easier to understand.

How do multiple interfaces enable flexible card design?
You can create any kind of card you want by combining multiple interfaces together

What are the advantages of separating combat and magic concerns?
You can create a card type that solely focuses on combat skills and another that focuses on magic.

How do Abstract Factory and Strategy patterns work together?
It creates cards and apply a way of using them.

What makes this combination powerful for game engine systems?
You can choose how to play your cards.

How does multiple inheritance allow a class to implement several interfaces?
By inheriting multiple sets of methods, enabling the creation of a card game.

What are the benefits of combining ranking capabilities with card game mechanics?
Being able to update the ranking based on the combat result of the cards.

# Resources

## Notions:

- [Module 05 README](https://github.com/noemiepi/Python-Modules/blob/main/PythonModule05/README.md)

## Githubs:

- [naha7777](https://github.com/naha7777/Python_modules/tree/main/python_module_07)

- [bebenjamin1](https://github.com/bebejamin1/PYTHON_MODULE_07)
