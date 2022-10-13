# Rodina Karki
# Class: CS0
# Date: 09/26/2022
# Description: Homework Assignment 2 
#Design and implement an algorithm using Python that finds the perimeter and area of a triangle.
#Given three sides, your Python program computes and displays the perimeter and area along with the following requirements.

#Program Description:
# -Program must prompt the user to enter three sides of a triangle. 
# -Calculate area of the given triangle. 
# -Calculate perimeter of the given triangle.
# -Print the calculated values with proper descriptions.

#Three sides of the triangle is a,b and c.
a = int(input("Side 1 : "))
b = int(input("Side 2 : "))
c = int(input("Side 3 : "))

#Calculate the perimeter
perimeter = a + b + c
print("Perimeter of Triangle : ", perimeter)

#Calculate the semi perimeter
s = (a+b+c)/(2)

#Calculate the area
area= (s*(s-a)*(s-b)*(s-c))**(0.5)
print("Area of the triangle is", round(area,2))

#Function definition to check validity
def is_valid_triangle(a,b,c):
  if a+b>=c and b+c>=a and c+a>=b:
      return True
  else:
      return False
#function call and making decisions
if is_valid_triangle(a,b,c):
  print ('Triangle is valid.')
else:
  print('Triangle is Invalid')