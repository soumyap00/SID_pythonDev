num = int(input("enter a number: "))
count=0
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   
  
for digit in str(factorial):
    if int(digit)==0:
        count+=1
print("The no of zeros in the factorial of ",num," is ",count)