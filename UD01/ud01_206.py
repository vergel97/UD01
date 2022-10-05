#a false
#b true
#c true
#d false
#e true
#f false
W = False
X = True
Y = True
Z = False
print(W or Y and X and W or Z)
print(X and not Y and not X or not W and Y)
print(not (W or not Y) and X or Z)
print(X and Y and W or Z or X)
print (Y or not (Y or Z and W))
print (not X and Y and (not Z or not X))