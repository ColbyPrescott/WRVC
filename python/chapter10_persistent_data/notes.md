## Overview
- Thus far, data has been embedded in the program, the same every time, or it has been entered by the user, which must be done every time the program is run
- Persistent data is typically stored as a file in secondary memory (ex. hard drive)
- Files can contain any data type, but the easiest to work with contain text. They can be read by humans and edited in common text editors
- Python handles the multiple conventions for new lines automatically, converting it to and from `\n`

## Opening, Reading, and Writing files
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
- Write methods
  - `print(<data>, file=<outputfile>)` will work just like the `print` statement. Does not work if file was opened in binary mode since print will cast to strings
  - `<file>.write(<data>)` will add data exactly as written. No newline if not included in data

## Absolute and Relative Paths
- Top-level directory is the root directory
- Absolute paths start at the root directory
- Relative paths start with anything other than the root directory, 
- A running program has a *working directory*, where all Python relative paths are based off of
- `.` and `..` represent the working directory and parent of the working directory respectively
- The `__file__` special attribute is a string of the path of the Python file 
- Python will accept forward slashes on any device, but permits back slashes on Windows. Usually avoided for the requirement of an escape character

## Pathlib
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

# Bytes and More Data Types
- `<str>.encode()` will turn a string into type `bytes`
- `<bytes>.decode()` will turn bytes into a string
- `<bytes>[i]` will return an integer 0-255 at that index
- Asking Python to print a binary sequence may yield `b'Hello world!'` because it uses ASCII for a representation of the bytes
- If converted characters are above 255, they will become several bytes
  - `(s + chr(128) + chr(256) + chr(512) + chr(1024)).encode()` yields `b'Hello world!\xc2\x80\xc4\x80\xc8\x80\xd0\x80'`
- `open(<path>, "rb")` will open a file for reading in byte mode. `<file>.read()` will return type `bytes`. Same with `wb`

# Pickle
- Library that turns Python objects into and from files
- Object to file is called *serialization*
- File to object is called *deserialization*
- `import pickle`, `with open(...) as <file>` as usual
- Export with `pickle.dump(<data>, <outfile>)`
- Import with `pickle.load(<infile>)`
- One possible extension to use is `.pkl`
- Pickle works with all built-in types and many programmer-made types, but not all objects, such as graphics objects
- Loading a pickle file could cause arbitrary code execution

## Remote Files
- URL stands for Uniform Resource Locator
- You could type a URL into a browser and then download the file
- `from urllib.request import urlopen`
- `with urlopen(<url_string>) as <infile>:`
- Acts like a file opened in `"rb"` mode

## Other
- Can create a file dialog box with `from tkinter.filedialog import askopenfilename, asksaveasfilename, askdirectory`