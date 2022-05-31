# defaultdict여도 없는 key를 indexing하면 error가 발생한다.
# indexing함에 있어 항상 예외가 발생할 수 있음을 기억해야 한다.
'''
주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.

항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
모든 공항은 알파벳 대문자 3글자로 이루어집니다.
주어진 공항 수는 3개 이상 10,000개 이하입니다.
tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
주어진 항공권은 모두 사용해야 합니다.
만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.


<<입출력 예시>>
입력: [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
출력: ["ICN", "JFK", "HND", "IAD"]

입력: [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
출력: ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

입력: [["ICN", "AOO"], ["AOO", "BOO"], ["AOO", "BOO"], ["BOO", "AOO"], ["BOO", "FOO"], ["FOO", "COO"], ["COO", "ZOO"]]
출력: ["ICN", "AOO", "BOO", "AOO", "BOO", "FOO", "COO", "ZOO"]

입력: [["ICN", "BBB"], ["ICN", "CCC"], ["BBB", "CCC"], ["CCC", "BBB"], ["CCC", "ICN"]]
출력: ["ICN", "BBB", "CCC", "ICN", "CCC", "BBB"]

입력: [["ICN", "AOO"], ["AOO", "BOO"], ["AOO", "COO"], ["COO", "AOO"], ["BOO", "ZOO"]]
출력: ["ICN", "AOO", "COO", "AOO", "BOO", "ZOO"]

입력: [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]
출력: ["ICN", "BOO", "DOO", "BOO", "ICN", "COO", "DOO", "COO", "BOO"]

입력: [["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]
출력: ["ICN", "AAA", "ICN", "AAA", "ICN", "AAA"]

입력: [["ICN", "AOO"], ["ICN", "AOO"], ["AOO", "ICN"], ["AOO", "COO"]]
출력: ["ICN", "AOO", "ICN", "AOO", "COO"]

입력: [["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]
출력: ["ICN", "AAA", "ICN", "AAA", "ICN", "AAA"]
'''


import collections


def solution(tickets):
    to_go = len(tickets)
    fairway = collections.defaultdict(list)
    route = ['ICN'] + [None]*len(tickets)
    answer = list()

    for departure, arrival in tickets:
        fairway[departure].append(arrival)
    for key in fairway.keys():
        fairway[key].sort()

    def dfs(num, fairway):
        if num == to_go:
            answer.append(route)
            raise NotImplementedError
        now = route[num]
        if now not in fairway.keys():
            return

        temp_fairway = {k: v[:] for k, v in fairway.items()}
        destinations = temp_fairway[now]
        if destinations:
            num += 1
            for destination in destinations:
                route[num] = destination
                del temp_fairway[now][temp_fairway[now].index(destination)]
                dfs(num, temp_fairway)
                temp_fairway[now].append(destination)
                temp_fairway[now].sort()

    try:
        dfs(0, fairway)
    except NotImplementedError:
        return answer[0]
