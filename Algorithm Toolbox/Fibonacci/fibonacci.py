def fibonacci_number(n):
    fibo = [0,1]
    for i in range(2,n+1):
        fibo.append(fibo[i-1]+fibo[i-2])
    return fibo[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))