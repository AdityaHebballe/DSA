def primitive_calculator(n, sum=0, count=0):
    if sum == n:
        return count
    if sum < n:
        return min(primitive_calculator(n, sum + 1, count + 1), primitive_calculator(n, sum * 2, count + 1), primitive_calculator(n, sum * 3, count + 1))

print(primitive_calculator(23))