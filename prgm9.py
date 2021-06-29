A = []
n = int(input("Enter number of elements in the list : "))

print("Enter elements:")
for i in range(0, n):
    elm = int(input())
    A.append(elm)
print("The entered list is: \n",A)

k =int(input("Enter which smallest number you want to see:"))

A.sort()
print(k,"'th smallest element is",A[k-1])
