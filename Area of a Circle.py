import math

def area_of_circle(radius):
    return round(3.14 * radius * radius, 2)


R = int(input())

print(f"{area_of_circle(R):.2f}")