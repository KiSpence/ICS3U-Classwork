#34
number = int(input("Enter a number "))
if number % 2 == 1 :
	print(f"{number} is an odd number.")

else:
	print(f"{number} is an even number.")

print(" ")

#36
letter = input("Enter one letter ")
if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
	print(f"{letter} is a vowel.")

elif letter == "y":
	print("Y can be a vowel sometimes. Don't ask, I didn't make the rules.")

else:
	print(f"{letter} is a consonant.")

print(" ")

#37
side = input("How many sides does your shape have? ")
if side == "3":
	print("Your shape is a triange.")

elif side == "4":
	print("Your shape is a quadrilateral.")

elif side == "5":
	print("Your shape is a pentagon.")

elif side == "6":
	print("Your shape is a hexagon.")

elif side == "7":
	print("Your shape is a septagon.")

elif side == "8":
	print("Your shape is an octogon.")

elif side == "9":
	print("Your shape is a nonagon.")

elif side == "10":
	print("Your shape is a decagon.")

else:
	print("ERROR")

print(" ")

#38
month = input("Enter a month ")
if month == "April" or "June" or "September" or "November":
	print(f"{month} has 30 days.")

elif month == "February":
	print("February normally has 28 days, but has 29 during a leap year.")

else:
	print(f"{month} has 31 days.")

print(" ")

#43
value = input("What is the value of your banknote? ")
if value == "1":
	print("There is a picture of George Washington on your banknote.")

elif value == "2":
	print("There is a picture of Thomas Jefferson on your banknote.")

elif value == "5":
	print("There is a picture of Abraham Lincoln on your banknote.")

elif value == "10":
	print("There is a picture of Alexander Hamilton on your banknote.")

elif value == "20":
	print("There is a picture of Andrew Jackson on your banknote.")

elif value == "50":
	print("There is a picture of Ulysses S. Grant on your banknote.")

elif value == "100":
	print("There is a picture of Benjamin Franklin on your banknote.")

else:
	print("ERROR")

print(" ")

#44
month = input("Enter the month ")
day = int(input("Enter the day "))
if month == "January" and day == "1":
	print("January 1st is New Year's day!")

elif month == "July" and day == "1":
	print("July 1st is Canada Day!")

elif month == "December" and day == "25":
	print("December 25th is Christmas Day!")

else:
	print("The month and day you entered doesn't have a holiday.")

print(" ")

#46
month = input("Enter a month ")
day = int(input("Enter a day "))

if month == "January" or "February":
	season = "winter"

elif month == "April" or "May":
	season = "spring"

elif month == "July" or "August":
	season = "summer"

elif month == "October" or "November":
	season = "fall"

elif month == "March" and day > 19:
	season = "spring"

elif month == "June" and day > 20:
	season = "summer"

elif month == "September" and day > 21:
	season = "fall"

elif month == "December" and day > 20:
	season = "winter"

print(f"{month} {day} is in {season}")

print(" ")

#48
year = input("Enter the year you were born. ")
if (year - 2000) % 12 == 0:
    sign = "dragon"

elif (year - 2000) % 12 == 1:
    sign = 'snake'

elif (year - 2000) % 12 == 2:
    sign = "horse"

elif (year - 2000) % 12 == 3:
    sign = "sheep"

elif (year - 2000) % 12 == 4:
    sign = "monkey"

elif (year - 2000) % 12 == 5:
    sign = "rooster"

elif (year - 2000) % 12 == 6:
    sign = "dog"

elif (year - 2000) % 12 == 7:
    sign = "pig"

elif (year - 2000) % 12 == 8:
    sign = "rat"

elif (year - 2000) % 12 == 9:
    sign = "ox"

elif (year - 2000) % 12 == 10:
    sign = "tiger"

elif (year - 2000) % 12 == 11:
	sign = "hare"

print(f"Your zodiac sign is a {sign}.")

print(" ")

#51
grade = input("Enter a grade letter ")
if grade == "A+":
	print:("Your grade is 4.0.")

elif grade == "A":
	print("Your grade is 4.0.")

elif grade == "A-":
	print("Your grade is 3.7.")

elif grade == "B+":
	print("Your grade is 3.3.")

elif grade == "B":
	print("Your grade is 3.0.")

elif grade == "B-":
	print("Your grade is 2.7.")

elif grade == "C+":
	print("Your grade is 2.3.")

elif grade == "C":
	print("Your grade is 2.0.")

elif grade == "C-":
	print("Your grade is 1.7.")

elif grade == "D+":
	print("Your grade is 1.3.")

elif grade == "D":
	print("Your grade is 1.0.")

elif grade == "F":
	print("Your grade is 0.")

elif grade == " ":
	print("Your grade is  .")

else:
	print("ERROR")

print(" ")

#52
grade = input("Enter a grade number ")
if grade == "4.0":
	print:("Your grade is an A.")

elif grade == "3.7":
	print("Your grade is an A-.")

elif grade == "3.3":
	print("Your grade is a B+")

elif grade == "3.0":
	print("Your grade is a B.")

elif grade == "2.7":
	print("Your grade is a B-.")

elif grade == "2.3":
	print("Your grade is a C+.")

elif grade == "2.0":
	print("Your grade is a C.")

elif grade == "1.7":
	print("Your grade is a C-.")

elif grade == "1.3":
	print("Your grade is a D+.")

elif grade == "1.0":
	print("Your grade is a D.")

elif grade == "0":
	print("Your grade is an F.")

elif grade == " ":
	print("Your grade is  .")

else:
	print("ERROR")

print(" ")

#hello_name 
def hello_name(name):
  str = "Hello {}!".format(name)
  return str
  
#make_out_word
def make_out_word(out, word):
  str = "{make_out_word{word}}"
  return str

#first_half
def first_half(str):
  str = str[:-len(str)/2]
  return str

#non_start
def non_start(a, b):
  start = start[{non_start} -1]
  return start

#make_abba
def make_abba(a, b):
  str = "{}".format(a ,b )
  return str

#extra_end
def extra_end(str):
  str = "{}".format(extra_end)
  return str

#without_end
def without_end(str):
  str = "{}".format(without_end)
  return str

#left2
def left2(str):
  str = "{}".format(left2)
  return str

#make_tags
def make_tags(str):
  str = "{}".format(make_tags)
  return str

#first_two
def first_two(str):
  str = "{}".format(first_two)
  return str
  
