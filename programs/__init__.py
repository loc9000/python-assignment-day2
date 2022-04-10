# ask if the use wants to do sq. footage or circumference. 
def calculate():
    answer = input("do you want to find the square footage or the circumference? ")
    if answer == 'square footage':
        #ask user for 2 numbers
        width = int(input('what is the width? '))
        height = int(input('what is the height? '))
        area = width * height
        print(area)
        #calculate w * h
    if answer == 'circumference':
        #ask for the radius
        radius = int(input('what is the radius? '))
        circumference = (2 * 3.14) * radius
        print(circumference)
        #calculate 2(3.14)* radius

# calculate()