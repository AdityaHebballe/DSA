from sys import stdin

def check(distance, tank, stops):
    curr_stop = tank
    for i in range(len(stops)):
            if stop[len(stops)-i]<curr_stop:
                curr_stop= stop[len(stops)-i]
                distances-=curr_stop
    check(distance, tank+curr_stop, stops)


def min_refills(distance, tank, stops):
    while distance!=0:
        distance=-tank
        for i in range(len(stops)):
            if stop[len(stops)-i]<400:
                stop[len(stop)-i]+tank



    return -1


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
