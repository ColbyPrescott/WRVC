# Haii Mr. Field so I know your comment about "Add more comments" was an example for another student and wasn't meant to be taken literally but I briefly took it literally and decided to show you what I would have typed if I had taken it literally :D

# python/chapter3/p86-e16-fibonacciMoreComments.py
# I am currently listing out the path of the file because apparently the reader is blind
# This is a Python file
# Written as part of John Zelle's "Python Programming: An Introduction to Computer Science (Fourth Edition)"
# specifically chapter 3, page 86, exercise 16 in which a super simple program is put together to calculate the nth number in the Fibonacci sequence

# Compute nth number in Fibonacci sequence
# 1, 1, 2, 3, 5, 8, 13, 21, etc...

# Define the main function that will be called at the end of the file
# It is called main as a common programming practice
# Python uses 'def' as the keyword to define a function, in this case the main function
# There are no parameters in the main function, therefore the parentheses contain no parameters
# Bastard colon of a curly bracket-less language >:(
def main():
    # Give a program description to the user
    # using the print function, in order to print stuff to the user
    # A string is passed because a string represents 
    # It is essentially the same as the program description comment, but slightly more user friendly
    print("Compute the Nth number in the Fibonacci sequence")
    
    # Determine which number the user wants to find
    # Fun fact: I was at first calling it "digit" rather than "number" but then I realized that the sequence soon contains two digit numbers
    # This variable represents the index into the sequence that the user wants to find
    # n is a terrible name but it's a little hard to pick one with so little other context
    n = int(input("Enter the number to find: "))
    
    # Integer variables a and b will be used to calculate the Fibonacci sequence
    # a is the running output, and b is the next value
    # a and b will be summed to calculate a new value in the sequence, then b will be moved to a and the sum will be moved to b
    # The sum will need to be stored in a temporary variable because a will be overwritten by the time the sum is needed for setting b
    
    # Start a and b with the first two digits of the sequence. The sequence is considered to start as [0, 1, 1, 2, 3] rather than [1, 1, 2, 3] as given in the problem so that asking for number 1, the first number, will yield the first number of the given array, and asking for number 0, as in index 0, will correspond with my own interpretation of the Fibonacci sequence and make me happy. Wow I did not think I would rewrite this comment to be even longer
    a = 0 # Initialize a to integer 0 for the reasons listed above
    b = 1 # Initialize b to integer 1 for the reasons listed above
    # Loop through the above described algorithm to put the desired nth number of the sequence into the a variable
    # i is only needed for the setup of the for Loop
    for i in range(n):
        # Calculate a temporary sum now so that overwritting a will not affect the result
        sum = a + b
        # Shift the sequence down, placing the current value of b into a
        # This is done with the assignment operator, =
        # Do note that the assignment operator is not the same thing as equality in mathematics. This is teaching the computer to do baby math, not teaching math to a baby
        a = b
        # Shift the sequence down, placing the newly calculated Fibonacci number into b
        b = sum
        # Repeat the for loop again
    # End of for loop
    
    # Now that the requested Fibonacci number has been calculated and placed in variable a, print it out the the user
    # Yippee. How fun.
    # The sep="" was used so that the spaces can be manually controlled
    # I found the sep parameter while looking through the print function header in VSCode. I am currently typing this in https://www.online-python.com/ , so the parameter is just something I committed to memory
    # The spaces need to be manually controlled so that the requested number does not appear as "Fibonacci number # 6 is: 8"
    # The # is included to help differentiate between the user's input and the output
    # The user's input is shown because, I, uh.. why *did* I include the input in the final print? I haven't done that for the last few exercises. Maybe I just wanted clarity, oh well
    print("Fibonacci number #", n, " is: ", a, sep="")
# End of main

# Call main to execute the main body of the program
# The identifier "main" is used because that is what the function was named earlier
# The two empty parentheses are used to indicate this as a function call, and they are empty because main does not accept any arguments
main()

# I purposely made these comments horrific and yet I still have a feeling they are better than what I may end up seeing throughout the year
# Ah oh no space octopi have bound the enter key to accapt autocomplete on this random website, what have they done! It just tried to correct "year" to "bytearray"!
# Ah- it appears I don't know how to end this file
# Probably could've added more comments
