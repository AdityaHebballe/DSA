from itertools import permutations


def largest_number(numbers):
    numbers = list(map(str,numbers))
    concat = ''
    for i in numbers:
        concat += i
        
    numbers.sort()
    largest=''
    for i in range(1,len(numbers)):
        largest+= max(number)
    return largest


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number(input_numbers))