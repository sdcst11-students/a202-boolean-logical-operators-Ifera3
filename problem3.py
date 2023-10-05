#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 

You can use max() to help you find the largest number
You can use min() to help you find the smallest number
How can we find the middle number though?
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""

a = int(input("enter a integer: "))
b = int(input("enter a integer: "))
c = int(input("enter a integer: "))

small = min(a, b, c)
large = max(a, b, c)
if a != small and a != large:
    medium = a
elif b != small and b != large:
    medium = b
elif c != small and c != large:
    medium = c

if (small ** 2) + (medium ** 2) == (large ** 2):
    print(f"{small}, {medium}, {large} form a Pythagorean triple")
else:
    print(f"{small}, {medium}, {large} do not form a Pythagorean triple")