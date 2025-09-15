def main():
    print("This program will convert a temperature in degrees Celsius into degrees Fahrenheit, particularly useful for the pesky radio broadcast that is too German for me, poor Susan")
    
    celsius = float(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()