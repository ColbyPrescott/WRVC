- *Search* is the process of looking for a piece of data in a collection. Ex `lst.index(<num>)`
- Test if value in list with `if x in lst`
- Note: `lst.index` will throw an error if not found
- Linear search: Scan items one by one until a match is found, or get to the end
  - Good as any for randomly ordered lists
  - Implemented in `in` and `lst.index`
- Binary search: Cut the search space in half every time, like guess the number 1 - 100
  - Only works on sorted lists
  - Start with a low and high value, and move the appropriate one to the middle

## Comparing Algorithms
- Empirical test: Could run tests and time how long each one takes
- Binary search is faster than linear, at least for larger lists. Linear is faster for smaller lists
- The speed of an algorithm depends on how many steps it takes in relation to the difficulty (e.g. number of elements to search through). Count the steps
- For linear search, doubling the list length will double the time. This is called a *linear time algorithm*
- The binary search halves the search space every iteration. Doubling list length will add one iteration. n = 2^i. i = log2(n). Example of *log time algorithm*

## Recursive Problem Solving
- *Divide and conquer* algorithms will split a problem into smaller versions of the same problem, and usually are pretty fast
- A function can be recursive without without being cyclical, as long as it converges to a single value
- Good recursive functions will have
  - A base case in which no recursion is needed
  - All chains of recursion eventually end up at the base case
- Example fast exponentiation:
  - `a^n =` 
    - `a^(n//2) * a^(n//2)` if n is even
    - `a^(n//2) * a^(n//2) * n` if n is odd
- Recursion is a generalization of loops; anything that can be done with a loop can be done with recursion
- Recursion is sometimes slower than a linear solution, such as calculating Fibonacci numbers. If one calculation requires a calculation of the previous and second previous number in the sequence, the recursions will expand rather than converge
- *Selection sort*: Loop through a list and keep track of the lowest value. Move it to the start. Repeat in remaining section of list
- *Merge sort*: Split a list in two, sort first half, sort second half, merge them back together
  - With a base case of one element or less being already sorted and converging sizes, the sorting can be done with a recursive call to merge sort

Problems to do: Anagrams, Towers of Hanoi, read chapter summary. Exercises 1 Fibonnaci and 2 