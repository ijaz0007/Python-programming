from typing import Any

name: Any = "Pakistan"
print(name)  # print
print(type(name))  # type
print(id(name))  # physical address
print([i for i in dir(name) if "__" not in i])  # methods and attributes
