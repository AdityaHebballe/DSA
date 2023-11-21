def fibonacci_number(n,m):
    fibo = [0,1]
    prev=0
    curr=1
    sum_last = 0
    for i in range(2,120):
        fibo.append((fibo[i-1]%10+fibo[i-2]%10)%10)
    m = m % 60
    n = n % 60
    if m < n:
        m += 60
    for i in range(n,m+1):
        sum_last += (fibo[i]%10)
        
    return sum_last%10

# def getFibonacciPartialSumFast(m, n):
#     sum = 0
 
#     # The input arguments, as the last digit
#     # pattern repeats with a period of 60, and the sum
#     # of 60 such consecutive numbers is 0 mod 10
#     m = m % 60
#     n = n % 60
 
#     # Make sure n is greater than m
#     if n < m:
#         n += 60
 
#     current = 0
#     next = 1
 
#     for i in range(n + 1):
#         if i >= m:
#             sum += current
 
#         new_current = next
#         next = next + current
#         current = new_current
 
#     return sum % 10
if __name__ == '__main__':
    input_n,input_m = map(int,input().split())
    print(fibonacci_number(input_n,input_m))