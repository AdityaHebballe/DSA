from sys import stdin

# def check(distance, tank, stops):
#     if distance<tank:
#         return 0
#     next_stop=tank
#     curr_stop = 0
#     no_of_stops=0
#     for i in range(len(stops)):
#             if stop[len(stops)-i]<next_stop:
#                 distances-=next_stop
#                 no_of_stops+=1
#                 next_stop+= tank
#     return no_of_stops

def min_refills(distance, tank, stops):
    if distance<tank:
        return 0
    next_stop=tank
    no_of_stops=0
    for i in range(1,len(stops)):
        if stops[len(stops)-i]<next_stop:
            distance-=stops[len(stops)-i]
            no_of_stops+=1
            next_stop=stops[len(stops)-i]
            next_stop+= tank
            if distance<0:
                break
    return no_of_stops


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
