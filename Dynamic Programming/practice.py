import math
def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinMax(M,m,i,j,operators):
    max_value = float('-inf')
    for k in range(i,j):
        a = evaluate(M[i][k], M[k+1][j], operators[k])
        b = evaluate(M[i][k], m[k+1][j], operators[k])
        c = evaluate(m[i][k], M[k+1][j], operators[k])
        d = evaluate(m[i][k], m[k+1][j], operators[k])
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)
    return min_value, max_value
        

def maximum_value(dataset):
    operands = []
    operators = []
    for i in dataset:
        if i in ['+','-','*']:
            operators.append(i)
        else:
            operands.append(int(i))
    M= [[-1]*len(operands) for _ in range(len(operands))]
    m= [[-1]*len(operands) for _ in range(len(operands))]
    for i in range(len(operands)):
        M[i][i] = operands[i]
        m[i][i] = operands[i]
    for j in range(1,len(operands)):
        for i in range(len(operands)-j                    ):
            k = i+j
            m[i][k],M[i][k] = MinMax(M,m,i,k,operators)
    return M[0][len(operands)-1]

if __name__ == "__main__":
    print(maximum_value(input()))