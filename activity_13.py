no = int(input("Enter a number of column: "))

for x in range (1,no):
    for y in range(1, no+1):
        print(f" |{x}x{y} = {x*y}|", end="")
    print()