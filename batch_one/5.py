"""Prog05: Create a program that ask the user to input their fullname in incorrect casing. Print the input in proper casing.
Example:
Input: jUAn DEla CrUZ
Output: Juan Dela Cruz"""

user_input = input("Please enter your full name: ").title()

print(user_input)
