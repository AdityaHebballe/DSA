def change(money):
    numCoins=0
    while money>0:
        if money>=10:
            numCoins+=1
            money=money-10
        elif money>=5:
            numCoins+=1
            money=money-5
        else:
            numCoins+=1
            money=money-1
    return numCoins


if __name__ == '__main__':
    m = int(input())
    print(change(m))