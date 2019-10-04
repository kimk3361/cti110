# Write a program that asks for the length and width of two rectangles and the program should tell the user which rectangle has the greater area, or if the two rectangles have equal area
# October 4, 2019
# CTI-110 P3T1-Areas of Rectangles
# Kihan Kim
length1 = int(input('Enter the length of Rectangle 1: '))
width1 = int(input('Enter the width of Rectangle 1: '))

length2 = int(input('Enter the length of Rectangle 2: '))
width2 = int(input('Enter the width of Rectangle 2: '))

area1 = length1 * width1
area2 = length2 * width2

if area1 > area2:
    print('Rectangle 1 has the greater area.')
elif area1 < area2:
    print('Rectamgle 2 has the greater area.')
else:
    print('Both have the same area.')

# Input length and width of first rectangle
# Input length and width of second rectangle
# Calculate areas of both rectangles
# Determine which rectangles have greater area or equal area
