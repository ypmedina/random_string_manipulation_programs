"""Prog06: Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.
Example:
Input: jUAn DEla CrUZ
Output: JuaN deLA cRuz"""

user_input = input("Please enter your full name: ").swapcase()

print(user_input)