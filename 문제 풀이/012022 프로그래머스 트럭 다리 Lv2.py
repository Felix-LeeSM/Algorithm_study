# 프로그래머스 트럭 다리
import collections
def solution(bridge_length, weight, truck_weights):
    curweight = 0 
    time = 0 
    togo = len(truck_weights) 
    truck_weights += [0]*bridge_length 
    arrived = 0 
    onbridge = collections.deque([0]*bridge_length) 
    truck_weights = collections.deque(truck_weights) 
    while True: 
        time += 1 
        gone = onbridge.popleft() 
        curweight -= gone 
        if gone != 0: 
            arrived += 1 
        if curweight + truck_weights[0] <= weight: #
            curweight += truck_weights[0] 
            onbridge.append(truck_weights.popleft()) 
        else :
            onbridge.append(0)
        if arrived == togo: 
            break
    return time