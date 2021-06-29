def find_gcd(x, y):
    while(y):
        x, y = y, x % y
  
    return x
      
      
a = input("Enter the number of elements: ")
arr = [] 
b = int(a)

print("enter the elements:")

for i in range(0, b): 
    y = int(input()) 
    arr.append(y)
    
  
num1=arr[0]
num2=arr[1]
gcd=find_gcd(num1,num2)
  
for i in range(2,len(arr)):
    gcd=find_gcd(gcd,arr[i])
      
print("the GCD of the input elements",arr,"is:",gcd)