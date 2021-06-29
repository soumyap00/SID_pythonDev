def triplets(A, size, val):
    
    for i in range( 0, size-2):
 
        for j in range(i + 1, size-1):
             
            for k in range(j + 1, size):
                if A[i] + A[j] + A[k] == val:
                    print("The Triplet whose sum is",val,"is", A[i],", ", A[j], ", ", A[k])
                    return True
    
    print("the triplet not present in the array")
    return False

A = []
size = int(input("Enter number of elements in the list : "))

print("Enter elements:")
for i in range(0, size):
   elm = int(input())
   A.append(elm)
print("The entered list is: \n",A)

val =int(input("Enter the sum value:"))
triplets(A, size, val)