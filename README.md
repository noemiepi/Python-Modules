# Description
This module introduces us to the Pydantic library.

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

How does Pydantic’s automatic type conversion work?
It automatically converts a type into another when it's possible.

What happens when you pass a string timestamp to a datetime field?
It converts it automatically.

How does Pydantic handle validation of nested models?
It will handle the nested model's errors first and then the model in which the nested one's are.

What happens when a CrewMember fails validation within a SpaceMission?
It prints an error message before processing the mission.

# Resources

## Notions:

- [Pydantic](https://pydantic.com.cn/en/)

- [Field](https://docs.pydantic.dev/2.6/concepts/fields/)

- [Limits with Field](https://stackoverflow.com/questions/61326020/how-can-i-set-max-string-field-length-constraint-in-pydantic)

- [model_validator](https://docs.pydantic.dev/latest/concepts/validators/#model-after-validator)
