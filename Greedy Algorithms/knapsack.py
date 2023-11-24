from sys import stdin


def optimal_value(capacity, weights, values):
    
    if capacity<0:
        return 0
    value = 0
    per_element = []
    for i in range(len(weights)):
        per_element.append(values[i]/weights[i])
    for i in range(len(per_element)):
        m= per_element.index(max(per_element))
        weight=min(capacity,weights[m])
        value+=per_element[m]*weight
        capacity-=weight
        per_element[m]=0
        if capacity==0:
            break
    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
