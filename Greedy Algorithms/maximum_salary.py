from itertools import permutations


def largest_number(numbers):
    numbers = list(map(str,numbers))
    concat = ''
    for i in numbers:
        concat += i
    numbers = [*concat]
    numbers.sort()
    largest=''
    for i in range(len(numbers)):
        largest+= max(numbers)
        numbers.remove(max(numbers))
        
    return int(largest)


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number(input_numbers))