#setting condition in Python/Programming
#Conditions can only be answered by TRUE/FALSE
# (and) operator - result would be true ONLY IF BOTH CONDITIONS ARE TRUE
# (or) operaton - the result would be TRUE  IF EITHER CONDITIONS ARE TRUE]
# (not) operator - would REVERSE any result of the condition

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age <= 8 and age >=1 :
	print(f"Hello {name}, you are considered as a toddler")
elif age >= 9 and age  <= 14 :
	print(f"Hello {name}, you are considered as a pre-teen") 
elif age >= 15 and age  <= 18 :
	print(f"Hello {name}, you are considered as a teenager") 
elif age >= 19 and age  <= 27 :
	print(f"Hello {name}, you are considered as a early adulthood") 
elif age >= 28 and age  <= 44 :
	print(f"Hello {name}, you are considered as a middle age") 
elif age >= 45 and age  <= 59 :
	print(f"Hello {name}, you are considered as a past adulthood") 
elif age >= 60  and age <= 120 :
	print(f"Hello {name}, you are considered as a senior") 
else:
	print("Invalid age")