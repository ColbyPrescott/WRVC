- `type(3)` -> `<class 'int'>`
- Use ints wherever possible for exactness
- `10/3` = `3.3333333333335`
- `++` does not exist, use `+= 1`
- Mixed type expressions will automatically convert to float
- Explicit typing can be done with `int()` and `float()`
- `round(x, numDecimals)` can also be used, rounding to type int by default
- `int("32")` -> `32`
- `str(10)` -> `'10'`
- `int("10.5)` -> Error
- Accumulator will build up a value in a variable known as the accumulator variable
- `range(start, n)` returns list from `start` to `n-1`
- `range(start, n, x)` returns list from `start` to `n-1` jumping by `x`

## Math Library
- `import math`
- `math.sqrt(x)`
- `math.factorial(x)`