"""
Coding Exercise 3
Create a program that prompts the user to input their name repeatedly.
Then, the program repeatedly prints out the name
 with the first letter capitalized.
"""
while True:
    user_input = input("What is your name? ")
    print(user_input.capitalize())