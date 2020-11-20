#1
colour = input("What is your favourite colour? ")
print("Oh,",colour,"? Nice choice.")
print("\n")

#2
c = input("How many cans are in the package? ")
d = input("How many packages do you have? ")
c = int(c)
d = int(d)
print("You should have",c * d,"cans in total.")
print("\n")

#3
l = input ("What is the length of the prism? ")
w = input ("What is the width of the prism? ")
h = input ("What is the height of the prism? ")
l = int (l)
w = int (w)
h = int (h)
print("The prism is",l * w * h, "units cubed.")
print("\n")

#4
question = input("Did you mute the teacher when you joined the Google Meet? ")
if question == "Yes": 
	print("That's probably not a good idea.")
else:
	print("Okay. Good.")
