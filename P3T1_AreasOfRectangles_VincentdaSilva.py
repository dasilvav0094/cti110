# A python program that compares the area of two rectanges given the deminsions
# 10.01.19
# CTI-110 P3T1 - Area of Rectangles
# Vincent daSilva
#

""" Pseudocode
- user input the length and width of the first rectangle
- user input the length and width of the second rectangle

- calculate the area (length * width) of each rectangle
- use comparative decision structures to compare the area values
    - if statement to display which rectangle has the greater area
    - or display that values are equal
"""

Ax = float(input("Enter length of Rectangle 'A': "))
Ay = float(input("Enter width of Rectangle 'A': "))

Bx = float(input("Enter length of Rectangle 'B': "))
By = float(input("Enter width of Rectangle 'B': "))

areaA = (Ax * Ay)
areaB = (Bx * By)

if areaA > areaB:
    print("The area of Rectangle A is greater")
elif areaA < areaB:
    print("The area of Rectangle B is greater")
else:
    print("The rectangles have equal area")
