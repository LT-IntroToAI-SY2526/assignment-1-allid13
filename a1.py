# Assignment 1: AI-Generated Python Problems
# Name: Allison Duran

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
"I'm learning Python basics in a high school programming class. I have some experience with javascript. 
Can you create 5-7 practice problems that cover Variables and basic data types, Conditionals (if/elif/else),
 Loops (for and while),Functions, Basic list operations1'"
 
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
PROBLEM 1: Variables & Data Types
"Create variables to store your name (string), age (integer), and height in meters (float). Then print a sentence like:
My name is Alice, I am 16 years old and 1.7 meters tall."

name = "Alice"
age = 16
height = 1.7

Problem 2: Conditionals (if/elif/else)
"Write a function grade_score(score) that
takes a test score (0 to 100) and returns the grade as follows:"

90 or above: "A"

80 to 89: "B"

70 to 79: "C"

60 to 69: "D"

Below 60: "F"

if num < 60:
    print("F")
elif num >= 60 and num <= 69:
    print("D")
elif num >= 70 and num <= 79:
    print("C")
elif num >= 80 and num <= 89:
    print ("B")
elif num >= 90:
    print("A")

Problem 3:Write a for loop that prints the numbers from 1 to 10.

for i in range(11):
    if i > 0 and i <= 10:
        print(i)

Problem 4: Write a while loop that starts at 5 and counts down to 1,
 then prints "Blast off!".

count = 5
while count > 0:
    print(count)
    count -= 1
print("Blast Off!")


Problem 5: Write a function add(a, b) that returns the sum of two numbers.
num_one = 3
num_two = 7

def add_numbers():
    sum = num_one+num_two
    print(sum)
    
add_numbers()


Problem 6:Given a list of numbers, print the first, middle, and last elements.
nums=[13,24,43,56,40]
print("First:", nums[0])
print("Middle:" , nums[2])
print("Last:" , nums[4])







"""



# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


#Problem number 1
name = "Alice"
age = 16
height = 1.7
print("My name is " + name + ", I am " + str(age)+ " years old and " + str(height)+ " meters tall.")
#should print My name is Alice, I am 16 years old and 1.7 meters tall.

#Problem number 2
num = 67
num = 87
num = 78
if num < 60:
    print("F")
elif num >= 60 and num <= 69:
    print("D")
elif num >= 70 and num <= 79:
    print("C")
elif num >= 80 and num <= 89:
    print ("B")
elif num >= 90:
    print("A")
#this code should read the number that it being given under variable num and return it's correct letter grade.  

#Problem number 3
for i in range(11):
    if i > 0 and i <= 10:
        print(i)
# this code should prrint out all number 1 through 10

#Problem number 4
count = 5
while count > 0:
    print(count)
    count -= 1
print("Blast Off!")
# this code should count backwards from 5 to 1 and then after it reaches 1 it should print out "blast off!"

#Problem number 5
num_one = 3
num_two = 7

def add_numbers():
    sum = num_one+num_two
    print(sum)
    
add_numbers()
#this code should add the numbers 3 and 7 and output the sum which is 10

#Problem number 6
nums=[13,24,43,56,40]
print("First:", nums[0])
print("Middle:" , nums[2])
print("Last:" , nums[4])
#this code should only print out the first number, the middle and the last not the rest of the numbers 

