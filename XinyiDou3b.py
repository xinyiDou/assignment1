more ='y'
count = 1
amount=0
while more=='y':
    c=input("Enter count of item "+str(count)+": ")
    p=input("Enter unit cost for item "+str(count)+": ")
    amount+=(int(c)*float(p))
    more = raw_input("More item (y/n)?"+": ")
    count+=1

tax= input("Enter sales tax rate (%):")
print("Total cost (pretax): "+str(amount))
print("Sales tax: "+ str(amount*(float(tax))/100))
print("Total cost (with tax): "+ str(round(amount*(1+(float(tax)/100)))),2)