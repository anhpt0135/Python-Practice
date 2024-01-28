"""
Coding Exercise 2
Create a program that prompts the user to input their name once.
Then, the program repeatedly prints out the name with the first letter capitalized.
"""
user_prompt = "Enter your name: "
user_input = input(user_prompt)

while True:
    print(user_input.capitalize())
