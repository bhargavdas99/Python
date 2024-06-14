def convert(n,val):
    if n==1:
        nval=val*82.04
        print(f"${val} = ₹{'{:.2f}'.format(nval)}")
    else:
        nval=val/82.04
        print(f"₹{val}= ${'{:.2f}'.format(nval)}")
print("(1)USD to INR") 
print("(2)INR to USD")
n=int(input("Enter the value 1 or 2: "))
if n!=2 and n!=1:
    print("Enter valid number!!")
    quit()
val=int(input("Enter money value to convert: "))
convert(n,val)
