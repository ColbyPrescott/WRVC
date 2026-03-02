- `type("Hello World!")` yields `<class 'str'>`
- A string is a sequence of characters
- Strings can be indexed just like an array with `<string>[<expr>]`
- The Python interpreter will represent strings around single quotation marks
- Python allows indexing from the end of an array by using negative numbers, such as `test_str[-1]` to get the last character
- Indexing will yield a single character, slicing will result in multiple characters, aka a substring
- Slicing is done with `<string>[<start>:<end>]`. The start character is included, the end is excluded
- String concatenation (+) will glue two string together. `"Hello" + " " + "World" + "!"` yields `"Hello World!"`
- String repetition (*) will concatenate a string with itself multiple times.  `"Hi" * 3` and `3 * "Hi"` both yield `"HiHiHi"`
- Both concatenation and repetition will build a new string, rather than modifying the original string
- The length of a string can be retrieved with the `len` function. `len("Hello")` yields `5`
- Strings can also be traversed within a for loop, such as `for ch in "Hello":`
- `ord("<character>")` can be used to turn a character into  Unicode number, and `chr(<integer>)` can be used to turn a Unicode number into a character

## Some String Functions
- `capitalize()`
- `center(width)`
- `count(sub)`
- `find(sub)`
- `join(list)`
- `ljust(width)`
- `lower()`
- `lstrip()`
- `replace(oldusb, newsub)`
- `rfind(sub)`
- `rstrip()`
- `split(optional sub)`
- `strip()`
- `title()`
- `upper()`

## Formatted String Literals
- Python can evaluate expressions inside strings by using formatted string literals `f"<string>"`
- `f"3 + 4 = {3 + 4}"` yields `"3 + 4 = 7"`
- Formatted string literals can use a format specifier such as `f"Cost is ${total:0.2f}"` using `<min_width>:<precision><type>`
  - `f"This int, {7:5}, uses a width of 5"` yields `"This int,     7, uses a width of 5`
  - `f"This float, {3.1415926:10.5}, uses width 10 and precision 5"` yields `"This float,    3.14159, uses width 10 and precision 5"`
  - Skipping the `f` type may result in `e` being used
- By default, numeric values will be right-justified and text values will be left-justified
- Justification can be specified with `<`, `^`, and `>`
  -   `f"Left justification: {'Cool':<10}"` yields   `"Left justification: Cool      "`
  - `f"Center justification: {'Cool':^10}"` yields `"Center justification:    Cool   "`
  -  `f"Right justification: {'Cool':>10}"` yields  `"Right justification:       Cool"`

## Extra

- Python has the `divmod` function to provide both the quotient and remainder in a single function call

## Tasks
- p. 241, p.245, p.260
- exercises 1&2