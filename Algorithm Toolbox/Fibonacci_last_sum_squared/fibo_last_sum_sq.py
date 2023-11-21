def fibonacci_number(n):
    prev=0
    curr=1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    sum_series = [1]
    for i in range(2,61):
        fib = prev%10 + curr%10
        sum_series.append((sum_series[-1]+pow(fib%10,2))%10)
        prev,curr = curr%10,fib%10
    return sum_series[n%60-1]%10

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))