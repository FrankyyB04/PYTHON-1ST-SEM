print("Hello, welcome to Denomination")

#(1000,500,200,100,50,20,10,5,1)
# c sign is for change/sukli

cash = eval(input("Enter Amount here: "))

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

print(th,"- 1000")
print(fh,"- 500")
print(two_h,"- 200")
print(one_h,"- 100")
print(fif,"- 50")
print(twe,"- 20")
print(ten,"- 10")
print(five,"- 5")
print(one,"- 1")












