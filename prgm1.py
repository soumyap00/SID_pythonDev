str = input("Enter a String :")
new ='' 
for a in str: 
    if (a.isupper()) == True: 
        new+=(a.lower()) 
    elif (a.islower()) == True: 
        new+=(a.upper()) 
    else:
        new+= a 
print("After swapping cases, the converted string is ",new)