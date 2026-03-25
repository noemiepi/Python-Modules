# Description
This module introduces us to files and how to open, read, write and close them, how to secure the entire process and different error types linked to this.

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

What happens to the storage system if connections aren’t properly closed?
data loss
limit in how many files can be opened at the same time

Why is the disconnect protocol critical?


What’s the critical difference between extraction mode (’r’) and preservation mode (’w’)?
`r` is to be able to read the file while `w` is to be able to write in the file and create one (not every time). Another command will be necessary to do either of those.
Why is this distinction vital for archivists?
It's 'vital' to be able to either read the file or write in it

Why do the Archives maintain separate channels for standard data and alerts?
It helps distinguish the errors from the data and therefore be able to choose to display only the standard data from the errors or both at the same time.

What could happen if these streams were mixed?
It would be harder to distinguish the errors from the data.

`stdin` is where the program is expected to read the output.
`stdout` is where it is expected to write the normal output.
`stderr` is where it is expected to write error messages.


How does the with protocol prevent data corruption?
When associated with `open()`, `with` automatically closes the file after reading and/or printing the content.

What is the RAII principle and why is it crucial for vault security?
Resource Acquisition Is Initialization (RAII) means that an object's creation and destruction are tied to a resource being acquired and released.
It is used to organize ressource allocation lifetime and can help reduce code complexity, improve readability and make it more difficult to break the code when functions become longer


What are the most dangerous threats to digital archives?
Data loss or corruption.

How does proper crisis response prevent data loss and maintain system stability?
By anticipating it.


# Resources

## Notions:

- [read()](https://www.w3schools.com/python/ref_file_read.asp)

- [write()](https://www.w3schools.com/python/ref_file_write.asp)

- [stdin/stdout/stderr](https://certiquizz.com/fr/cours/programmation/python/python-pour-developpeurs-le-guide-complet-et-avance/redirection-des-entrees-sorties)

- [Diff_stdout_stderr](https://retrocomputing.stackexchange.com/questions/11499/what-was-the-point-of-separating-stdout-and-stderr)

- [with](https://www.geeksforgeeks.org/python/with-statement-in-python/)

- [RAII](https://creatronix.de/raii-in-c-and-python-for-custom-types/#RAII_for_custom_types_in_Python)

## Github:

- [Overtek](https://github.com/Overtekk/Python-Module-00-10/blob/main/Python%20Module%2004/ex4/create_files.py)
