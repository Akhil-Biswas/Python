# Basic Python

## Table of Content

- [Identifiers & Keywords](#identifiers--keywords)
  - Keywords
  - Soft Keywords
- [DataTypes](#datatypes)
- Operators & Precedence
- ***

### Identifiers & Keywords

#### Keywords

- Python has **35 standard** reserved keywords
- 2 keywords **_Python 3.10+_** ([Soft keywords](#soft-keywords-context-specific): `match` and `case`)
- These words are **case-sensitive**
- And cannot be used as identifiers (such as _variable or function names_)

|         Category         |                   Keywords                    |
| :----------------------: | :-------------------------------------------: |
|     Boolean & Values     |            `True`, `False`, `None`            |
|    Logical Operators     |              `and`, `or`, `not`               |
|       Control Flow       |             `if`, `elif`, `else`              |
|    Loops & Iteration     |  `for`, `while`, `break`, `continue`, `pass`  |
|   Functions & Classes    |  `def`, `return`, `lambda`, `yield`, `class`  |
|   Structural & Scoping   |          `global`, `nonlocal`, `del`          |
|    Modules & Context     |        `import`, `from`, `as`, `with`         |
| Comparison & Membership  |                  `is`, `in`                   |
|  Exceptions & Debugging  | `try`, `except`, `finally`, `raise`, `assert` |
| Asynchronous Programming |               `async`, `await`                |

> [!NOTE]
> `True`, `False`, `None` Only these three start with a capital letter.

#### Soft Keywords (Context-Specific)

- Python also includes **soft keywords** like `match`, `case`, `_`, and `type`.
- These only act as reserved keywords within specific syntactic contexts (such as structural pattern matching or type aliases) and can still be used as regular variable names elsewhere in your code.

### DataTypes

|                    |                                          |
| :----------------- | :--------------------------------------- |
| **Numeric Types**  | `int`<br> `float`<br> `complex`          |
| **Text Type**      | `str`                                    |
| **Sequence Types** | `list`<br> `tuple`<br> `range`           |
| **Mapping Type**   | `dict`                                   |
| **Set Types**      | `set`<br> `frozenset`                    |
| **Boolean Type**   | `bool`                                   |
| **Binary Types**   | `bytes`<br> `bytearray`<br> `memoryview` |
| **None Type**      | `NoneType`                               |

### Operators & Precedence

|                          |                                                    |
| :----------------------- | :------------------------------------------------- |
| **Arithmetic Operators** | `+` ,`-` ,`*` ,`/` <br>`%` ,`**` ,`//`             |
| **Assignment Operators** | `=` , `+=` , `-=`, `*=`<br>`/=`,`%=`, `//=`, `**=` |
| **Comparison Operators** | `==`, `!=`, `>`, `<`<br>`>=`, `<=`                 |
| **Logical Operators**    | `and`, `or`, `not`                                 |
| **Identity Operators**   | `is`<br>`is not`                                   |
| **Membership Operators** | `in`, `not in`                                     |
| **Bitwise Operators**    | `&`, `\|`, `^` <br>`~`, `<<`, `>>`                 |
