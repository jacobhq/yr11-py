import math

r = int(input("Radius of ballpit (nearest whole number): "))
h = int(input("Height of ballpit (nearest whole number): "))
b = int(input("Radius of one ball (nearest whole number): "))

v = (math.pi * r**2) * h
vb = (4/3) * math.pi * b**3

num = v/vb

print(f"\nVolume of pit: {str(v)}\nVolume of ball: {str(vb)}\n")
print(f"Total number of balls: {str('%.0f'%(num))}")
