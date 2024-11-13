medical=input("Enter Y or N:")
atten=int(input("Enter attendence:"))

if medical=="Y" :
    print("Allowed")
else:
    if atten>=75:
     print("Allowed")
    else:
       print("Not allowed")  