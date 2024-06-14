# Jefferson Griebel / jcg0
# COP2002.0M1: PROGRAM LOGIC
# 05/27/2024
# Working with integers and string using concatenation
# Using variables to store values and then using those same variables to print them to the page using string concatenation

# this section is where I am storing all my values inside their own variables
name = "My name is Jefferson Griebel. "
major = "My major is Programming & Analysis."
answer = "\nI'm most interested in this class because I want to have a deeper\nunderstanding about the right way to code."
num1 = 49
num2 = 31

# this set of variables are the calculations for the number variables
addition = num1+num2
subtraction = num1-num2
multiply = num1*num2
divide = num1/num2
modulo = num1 % num2

# This is the finished print statement that uses concatenation to print the variables with strings
print(name + major + answer)
print()
print(f"{num1} + {num2} = {addition}")
print()
print(f"{num1} - {num2} = {subtraction}")
print()
print(f"{num1} * {num2} = {multiply}")
print()
print(f"{num1} / {num2} = {divide}")
print()
print(f"{num1} % {num2} = {modulo}")
print()
print()
print("This is the end of the program!")
