- Thus far, data has been embedded in the program, the same every time, or it has been entered by the user, which must be done every time the program is run
- Persistent data is typically stored as a file in secondary memory (ex. hard drive)
- Files can contain any data type, but the easiest to work with contain text. They can be read by humans and edited in common text editors
- Python handles the multiple conventions for new lines automatically, converting it to and from `\n`

- Associating a file on disk with an object in the code is called *opening*
- Once finished with a file, it is *closed*
- When reading a file, it gets put in RAM. It will only be put back on disk when you save it
- Opening a file in write mode will delete the contents of the old file
- Opening a file in write mode will create the file if it doesn't exist
- `<variable> = open(<path>, <mode>)`
  - `<path>` is the location of the file on disk
  - `<mode>` is either `"r"`, `"w"`, or `"a"` for read, write, or append
- Technically, files are closed automatically. But it still may lead to errors
- Python's context manager can close a file even if an error occured. Instead of closing, use `with open(<path>, <mode>) as <var>:`
- Can `with open as <1>, open as <2>, etc...:`
- Read methods
  - `<file>.read()` will return all contents as a single multi-line string
  - `<file>.readline()` will return the next line in the file, including the newline character
  - `<file>.readlines()` will return the remaining lines in the file, including newline characters, as a list
- To read a previously read line, the file must be closed and reopened
- Using `readlines` will load the entire thing at once, potentially bad for large files. Alternative is `for line in <file>`
- Write to a file with `print(<data>, file=<outputfile>)`

- Top-level directory is the root directory
- Absolute paths start at the root directory
- Relative paths start with anything other than the root directory, 
- A running program has a *working directory*, where all Python relative paths are based off of
- `.` and `..` represent the working directory and parent of the working directory respectively
- The `__file__` special attribute is a string of the path of the Python file 
- Python will accept forward slashes on any device, but permits back slashes on Windows. Usually avoided for the requirement of an escape character

- The `pathlib` module has many helpful path related methods
- It handles `PosixPath` and `WindowsPath` under the hood
- Can combine paths with the `/` operator
  - `Path.exists()`
  - `Path.with_suffix(<new_extension>)`
  - `Path.name` returns the name and extension of a file with none of the directories
  - `Path.stem` returns just the name, without extension or directories
  - `Path.suffix` returns just the extension of a file
  - `Path.rename(<new_path>)` will rename or move a file
  - `Path.iterdir()` returns a sequence of `Path` objects, one for each file/directory in the original folder
  - `Path.is_file()` returns whether a path points to a file or a directory
  - `Path.glob(<pattern>)` known as *file globbing* returns each file/directory in the original folder that matches a string pattern containing wildcard characters
    - `"*"` for any number of any characters
    - `"?"` for one of any character

## Other
- Can create a file dialog box with `from tkinter.filedialog import askopenfilename, asksaveasfilename, askdirectory`