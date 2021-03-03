options = int(input("Enter number of options: "))
start_V = int(input("Enter start value: "))
best = 1
r = 0.0
risk = 0.0

for i in range(1,options+1):
    print("Option: "+str(i))
    u_v=int(input("Enter high value: "))
    l_v=int(input("Enter low value: "))
    ex_E= (u_v+l_v)/2
    temp_e = (ex_E-start_V)/float(start_V)
    if(temp_e>r):
        r=temp_e
        best = i
        risk = (u_v-l_v)/2

print("Best investment: "+str(best))
print("Best average return: "+str(round(r*100,1)))
print("Rist = "+ str(risk))