- Functions divide up the program
- Functions reduce code duplication
- Some examples so far have been `main()`, `Point.getX()`, etc.
- DRY: Don't Repeat Yourself
- Functions are like subprograms
- Functions are called / invoked
- Gives example with singing Happy Birthday
- Gives example with future_val 
- Formal and actual parameters
- Local / private variables are defined inside a function
- Global / public variables are defined outside a function
- Local variables do not retain their values when a function ends
- All functions return a value whether they use `return` or not. void functions will return `None`
- Actual parameters are usually duplicated
- Mutable objects, when passed by parameter, are not duplicated. (They effectively get passed by reference)

Discussion questions will be on test

Skip programming exercised 4, 9, 10

1. **In your own words, describe the two motivations for defining functions in your programs.**<br>
Functions help reduce code duplication and can give names to different sections of code that allow you to take a higher level view of the program's processes.
2. **We have been thinking about computer programs as sequences of instructions where the computer methodically executes one instruction and then moves on to the next one. Do programs that contain functions fit this model?**<br>
Knowing exactly how a CPU treats functions / subroutines, I would argue that functions do not degrade the representation of computers executing one instruction and moving onto the next. The action of executing a function, in of itself, is an instruction for the computer to run.
3. **Parameters are an important concept in defining functions. A) What is the purpose of parameters? B) What is the difference between a formal parameter and an actual parameter? C) In what ways are parameters similar to and different from ordinary variables?**<br>
A) The purpose of parameters is to move variables from one scope to another. If every variable were in the global scope, the program would become very cluttered. B) A formal parameter lies in the function definition, such as `cat` in `def testFunc(cat):`. They do not yet have a value assigned, they are simply placeholders. On the other hand, actual parameters are the values given the function at the time that it is called, and the formal parameters are assigned to them. C) Parameters are similar to ordinary variables in that they are named values, can be modified, are destroyed with their scope, etc. The main thing to keep in mind is that the scope changes when a function is called, so unless the variable and parameter is a reference to an object, the parameter will be holding a copy of the ordinary variable's value.
4. **Functions can be thought of as miniature (sub)programs inside other programs. Like any other program, we can think of functions as having input and output to communicate with the main program. A) How does a program provide "input" to one of its functions? B) How does a function provide "output" to the program?**<br>
A) A program can provide inputs to one of its functions by putting values inside of the parentheses during the function call. B) A function can provide output by using the `return` keyword.
5. **Consider the function**
```Python
def cube(x):
    answer = x * x * x
    return answer
```
- - A. **What does this function do?**
This function will take a number x, cube it (AKA multiply three instances of it together), then return the result
- - B. **Show how a program could use this function to print the value of `y^3`, assuming `y` is a variable.**
This could be accomplished with `print(cube(y))`.
- - **Here is a fragment of a program that uses this function.**
```Python
answer = 4
result = cube(3)
print(answer, result)
```
**The output from this fragment is `"4 27"`. Explain why the output is not `"27 27"`, even though `cube` seems to change the value of `answer` to `27`.**
`answer` that is set to `4` does not get rewritten to `27` because the main section of the program and `cube` are two different scopes, which means the `answer` in the main section and `answer` in the `cube` function are different variables.