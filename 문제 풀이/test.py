def solution(numbers, target):
    answer = 0
    times = 0
    parameter = 0
    while times < 2 ** len(numbers) :
        candidate = 0
        bin_par = '0' * (len(numbers) + 2 - len(bin(parameter))) + bin(parameter)[2:]
        for i in range(len(numbers)) :
            if bin_par[i] == '0' :
                candidate += numbers[i]
            else :
                candidate -= numbers[i]
        if candidate == target :
            answer += 1
        parameter += 1
        times += 1
    return answer

def solution(dirs):
    point = [0, 0]
    path = set()
    for i in dirs :
        if i == 'U' :
            if point[1] == 5 :
                continue
            else :
                path.add(tuple(point + ['U']))
                point[1] += 1
                path.add(tuple(point + ['D']))
        elif i == 'L' :
            if point[0] == -5 :
                continue
            else :
                path.add(tuple(point + ['L']))
                point[0] -= 1
                path.add(tuple(point + ['R']))
        elif i == 'D' :
            if point[1] == -5 :
                continue
            else :
                path.add(tuple(point + ['D']))
                point[1] -= 1
                path.add(tuple(point + ['U']))
        elif i == 'R' :
            if point[0] == 5 :
                continue
            else :
                path.add(tuple(point + ['R']))
                point[0] += 1
                path.add(tuple(point + ['L']))
    return len(path) // 2

print(solution("ULURRDLLU"))



