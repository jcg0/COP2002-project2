# Jefferson Griebel / jcg0
# COP2002.0M1: PROGRAM LOGIC
# 06/11/2024
# Project 3: If statements (and lists?)
# Working with lists, for loops, conditionals and if statements to make a small vocabulary program. input a number to get the definition of one of the terms on the list
termInput = input("Enter the number of the term you want: ")

# this is my main function that is storing the functionality for the conditional statement


def main():

    terms = ["1. Algorithm", "2. Variable", "3. Variable Type (data type)", "4. Array", "5. If statement", "6. Loop",
             "7. Function", "8. Class", "9. Object", "10. Method", "11. Programming Language", "12. Control Structure"]

    print("This program will provide definitions to important programming terms.\nChoose a number to see the term's definition.")
    print()
    print("Terms:")
    for term in terms:
        print(term)
    print()
    print(f"Enter the number of the term you want: {termInput}")
    print()
    if (termInput == '1'):
        print("Algorithm: is a set of instructions that are followed to solve a problem.")
    elif (termInput == '2'):
        print("Variable:  container that holds a single number, word, or other information that you can use throughout a program.")
    elif (termInput == '3'):
        print("Basic variable types include: string (words and phrases), char (short for 'character;' a single letter or symbol you can type), int (short for 'integer;' for whole numbers), double or float (for decimal numbers), and bool (short for 'boolean;' for true or falsevalues.")
    elif (termInput == '4'):
        print("Array:  containers that hold variables of the same data type.")
    elif (termInput == '5'):
        print("If statement:  runs a block of code based on whether or not a condition is true.")
    elif (termInput == '6'):
        print("Loop:  check a condition and then run a code block.  The loop will continue to check and run until a specified condition is reached.")
    elif (termInput == '7'):
        print("Function:  block of code that can be referenced by name to run the code it contains.")
    elif (termInput == '8'):
        print("Class:  template definition of the methods and variables in a particular kind of object.")
    elif (termInput == '9'):
        print("Object:  data type that has unique attributes and behavior.")
    elif (termInput == '10'):
        print("Method:  programmed procedure that is defined as part of a class and is available to any object instantiated from that class.")
    elif (termInput == '11'):
        print("Programming Language:  system of notation for writing computer programs. \ Python is an example.")
    elif (termInput == '12'):
        print(
            "Control Structure:  basic blocks for decision making processes in computing.")
    else:
        print("Error! Not a valid choice.")


# the final if statement - I do not think that this is what the final product is supposed to look like according to github classroom
if (termInput):
    main()
else:
    main()
