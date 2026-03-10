# Lists
- Stores a collection of values
- Is useful when the number of values is unknown
- Denoted with square brackets `[]`
- Ordered sequence of items
- Common list generator: `range(5) == [0, 1, 2, 3, 4]`
- CS lists and arrays are based upon mathematical concepts, such as S = S0, S1, S2, S3, S4, ..., Sn-1 and summation notation
- Indexing a single item inside a list works just like indexing a string. Ex: `s[2]`
- Arrays in most programming languages are of fixed size and homogeneous. Their size must be set upon declaration, and they can only hold values of the same type
- Python lists are dynamic, with adjustable size and heterogeneous holding any mix of data types
- Lists are mutable, strings are not. `lst[3] = "W"` can word but not `s[3] = "W"`
- Assignment also works with slicing. Ex: `lst[1:3] = ["Two", "Words"]` 
- Lists grow and shrink as needed

## List Operators
- Concatenation: `<seq> + <seq>`
- Repetition: `<seq> * <int-expr>`
- Indexing: `<seq>[]`
- Length: `len(<seq>)`
- Slicing: `<seq>[:]`
- Iteration: `for <var> in <seq>:`
- Membership check: `<expr> in <seq>`

## List Methods
- `<list>.append(x)` Adds element `x` to end of list
- `<list>.sort()` Sorts the list (from "lowest" to "highest")
- `<list>.reverse()` Reverses the order of the list
- `<list>.index(x)` Returns index of first occurence of `x`
- `<list>.insert(i, x)` Inserts `x` into list at index `i`
- `<list>.count(x)` Returns the number of occurences of `x` in the list
- `<list>.remove(x)` Deletes the first occurence of `x` in the list
- `<list>.pop(i)` Deletes the ith element of the list and returns its value
- `<list>.pop()` Deletes the last element of the list and returns its value
- `<list1>.extend(<list2>)` Adds the items in `list2` to the end of `list1`

# Tuples
- Tuples look just like lists but use parentheses instead of square brackets
- Indexing and slicing still works
- Tuples are immutable, meaning the items inside and the size can't be changed
- More efficient / performant than lists
- Tuple example: `pair = (3, r)`
- Simultaneous assignment: `x, y = pair`

# Dictionaries
- A collection of items
- Values are accessed by a key rather than an index
- Can be created by listing key-value pairs. Ex: `passwords = {"guido": "superpassword", "turing": "sciencestuffz"}`
- Keys and values are joined by a colon, and commas separate the pairs
- Accessing value is done with indexing notation, but with the key. Ex: `passwords["guido"]` yields `'superpassword'`
- Dictionaries are mutable; the value associated with each key can be changed
- Mappings are unordered. If you print it out, the order will look random

# Sets
- A collection of items
- Unordered (Order is irrevelant)
- Unindexed (There is no indexing by index or key)
- Unchangable, not exactly immutable (The existing values can't change, but can be removed and added)
- Do not allow duplicate values
- Can loop through a set with `for x in <set>:`
- Can check if an item is in a set with `x in <set>`
- Add items with `<set>.add(x)`
- Combine sets with `<set>.update(<iterable>)`
- Remove an item with `<set>.remove(x)` (Will throw an error if the item doesn't exist)
- Remove an item with `<set>.discard(x)` (Will not throw an error)
- Remove a random item with `<set>.pop()`
- Empty a set with `<set>.clear()`
- Join sets without modifying the existing one with `<set>.union(<iterable>)` or `<set> | <set>` (The `|` operator only works set to set)
- Create a new set with items that are shared between two others with `<set1>.intersection(<set2>)` or `<set1> & <set2>`

# Frozenset
- It exists. Tuple and set combined
- Unordered
- Unindexed
- Immutable
- (Wow)

# Other
- Mean: Average
- Median: Middle number of sorted array
- Standard deviation: sqrt(sum((mean - each_value)^2) / (num_values - 1))
- A data structure is a way of storing and organizing data
