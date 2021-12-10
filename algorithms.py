# Given an array of integers, determine whether the array is monotonic or 

def ismonotone(a):
    n = len(a)  # size of array
    if n == 1:
        return True
    else:
        #check for monotone behaviour
        if all(a[i] >= a[i+1] for i in range(0, n-1) or a[i] <= a[i+1] for i in range(0, n-1)):
            return True
        else:
            return False

print(isMonotone(A))

A = [6, 5, 4, 4]
#B = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
#C = [1, 1, 2, 3, 7]



