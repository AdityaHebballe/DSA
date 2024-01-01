# def factorial(n):
#     if n<=1:
#         return 1
#     return n * factorial(n-1)
# print(factorial(3))

# def f(i):
#     if i==0:
#         return i
#     return i+f(i-1)
# print(f(3))

def reverse(arr,i):
    if i==len(arr)//2:
        return arr
    arr[i],arr[len(arr)-1-i] = arr[len(arr)-1-i],arr[i]
    return reverse(arr,i+1)
arr = [1,2,3,4]
print(reverse(arr,0))