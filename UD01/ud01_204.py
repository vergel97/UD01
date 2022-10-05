#x = 88, y = 3.5, z = -5.2,
#A = 86,3
#B = 33,1
#C = 25,1429
#D= 0,5
#E=-51,7647
#F=19,9429
#G=205,3333
#H=16,7619
#I=4
#J=149,6
#K=93,2
#L=0,2
#M=
#N=91,2
x = 88
y = 3.5
z= -5.2
print("A",x + y + z)
print("B",round(2 * y + 3 * (y - z),4))
print("C",round(x / y,4))
print("D",round(x % y,4))
print("E",round(x / (y + z),4))
print("F",round((x / y) + z,4))
print("G",round(2 * x / 3 * y,4))
print("H",round(2 * x / (3 * y),4))
print("I",round(x * y % z,4))
print("J",round(x * (y % z),4))
print("K",round(3 * x - z - 2 * x,4))
print("L",round(2 * x / 5 % y,4))
print("M",round(x - (100 % y) % z,4))

