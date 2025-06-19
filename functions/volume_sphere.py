from math import pi

def width_length():
    user_radius = int(input("Enter radius :"))
    helper = user_radius*user_radius*user_radius
    volume = (4/3)*pi*helper
    print("the area is :",volume)
width_length()
#area
