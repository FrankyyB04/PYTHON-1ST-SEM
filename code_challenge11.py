for j in range(7,0,-1):
    for k in range(1,j+1):
        print(" ",end=" ")
    for l in range(6,j,-1):
        print("*",end=" ")
    for m in range(7,j,-1):
        print("*",end=" ")
    print()
for x in range(1,6):
    for y in range(0,x+1):
        print(" ",end=" ")
    for z in range(5,x,-1):
        print("*",end=" ")
    for z in range(6,x,-1):
        print("*",end=" ")
    print()
