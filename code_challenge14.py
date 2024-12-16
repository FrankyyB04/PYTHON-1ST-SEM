#BANK SIMULATION PROGRAM
#CREATE ACCOUNT
#DEPOSIT
#WITHDRAW
#CHECK BALANCE
import os
print("\t--> WELCOME TO MY BANK SIMULATION PROGRAM <--")
acc = input("Do you want to create a new account (yes/no)? ")
if acc.lower() == "yes":
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    mid = input("Enter your middle initial: ")
    print(f"Account created successfully for {first} {mid} {last}!")
    print("Filipino denomination: 1000php, 500php, 200php, 100php, 50php, 20php, 10php, 5php, 1php")
    cash = eval(input("Enter the amount you want to deposit: "))
    th = cash//1000
    th_c = cash%1000
    fh = th_c//500
    fh_c = th_c%500
    two_h = fh_c//200
    two_h_c = fh_c%200
    one_h = two_h_c//100
    one_h_c = two_h_c%100
    fif = one_h_c//50
    fif_c = one_h_c%50
    twe = fif_c//20
    twe_c = fif_c%20
    ten = twe_c//10
    ten_c = twe_c%10
    five = ten_c//5
    five_c = ten_c%5
    one = five_c//1
    one_c = five_c%1

else:
    print("Thank you for using the system")

def denomination():
    print(th,"- 1000")
    print(fh,"- 500")
    print(two_h,"- 200")
    print(one_h,"- 100")
    print(fif,"- 50")
    print(twe,"- 20")
    print(ten,"- 10")
    print(five,"- 5")
    print(one,"- 1")

def add():
    global cash
    addbalance = eval(input("Enter the amount you want to deposit: "))
    cash += addbalance


def withdraw():
    cash2 = eval(input("Enter the amount you want to withdraw:  "))
    global cash
    if cash2 <= cash:
        cash -= cash2
        print("Thank you for using our system")
        return
    else:
        print("Insufficient balance")

def balance():
    print(f"Here's your remaining balance: {cash}")

repeat = True

while repeat:
    print("PLEASE SELECT FROM THE OPTIONS BELOW")
    print("1 -- Withdraw")
    print("2 -- Check Balance")
    print("3 -- Denomination Breakdown")
    print("4 -- Add balance")
    print("5 -- Exit")
    choice = eval(input("Which program would you like to run (1,2,3) -- > "))

    if choice == 1:
        os.system("cls")
        withdraw()
        continue
    elif choice == 2:
        os.system("cls")
        balance()
        continue
    elif choice == 3:
        os.system("cls")
        denomination()
        continue
    elif choice == 4:
        os.system("cls")
        add()
        continue
    elif choice == 5:
        os.system("cls")
        print("Thank you for using my program")
        repeat = False
        break
    else:
        os.system("cls")
        print("Invalid Choice")
        continue