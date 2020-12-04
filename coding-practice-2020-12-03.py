#Define the function
#Define the parameters
#Return the result
#Call the function and send the arguments.
#Handle the return value by placing it in a variable. Print it out.

# 1. Create a function that takes three numbers and adds them together.
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter one more number: "))

def addition(num1,num2,num3):
	print(num1 + num2 + num3)

"""Takes three numbers from user input and adds them together"""

addition(num1,num2,num3)

print(" ")

#2. Create a function that takes a name and an age and returns a string message including both pieces of data.
name = input("Enter your name ")
age = input("Enter your age ")

def greeting(name,age):
	print(f"Your name is {name} and you are {age} years old.")

"""Takes the user's name and age from input and repeats back to them in a sentence."""

greeting(name,age)

print(" ")

#3. Create a function that takes two numbers and returns the average of those numbers.
first = int(input("Enter a number: "))
second = int(input("Enter another number: "))

def average(first,second):
	print((first + second) / 2)

"""Takes two numbers from the user, adds them together and divides them by two to find the difference."""

average(first,second)

print(" ")

#4. Create a function that takes three numbers and returns the largest (don't use max).
f = int(input("Enter a number: "))
s = int(input("Enter another number: "))
l = int(input("Enter one more number: "))

def largest(f,s,l):
	if f > s:
		if f > l:
			print(f)
	elif l > s:
		if l > f:
			print(l)
	elif s > f:
		if s > l:
			print(s)
	
"""Takes three numbers from the user. After that, compares all numbers to each other in an if statement tree to find the largest number"""

largest(f,s,l)

print()

#5. Create a function that takes a string and returns the first two characters.
words = int(input("Write something: "))

def string(words):
	return words[:2]

"""Takes the string from user and only shows the first two characters."""

string(words)
