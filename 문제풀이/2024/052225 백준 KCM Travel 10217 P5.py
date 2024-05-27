from sys import maxsize, stdin, stdout
input = stdin.readline
INF = float('inf')


def solution(airports, budget, flights_count, flights):
    arrival = airports

    dp = [[maxsize]*(budget+1) for _ in range(airports + 1)]
    dp[1][0] = 0
    curr_min = maxsize

    for curr_cost in range(budget+1):
        for airport in range(1, arrival+1):
            if dp[airport][curr_cost] == maxsize:
                continue

            for end, cost, distance in flights[airport]:
                if curr_cost + cost > budget:
                    continue

                dp[end][curr_cost+cost] = \
                    min(dp[end][curr_cost + cost],
                        dp[airport][curr_cost] + distance)

    min_distance = min(dp[arrival])

    return 'Poor KCM' if min_distance == maxsize else str(min_distance)


def main():
    test_cases = int(input())
    answers = []

    for _ in range(test_cases):
        airports, budget, flights_count = map(int, input().split())

        # flights[start] = [(end, cost, distance)]
        flights = [[] for _ in range(airports + 1)]
        for _ in range(flights_count):
            start, end, cost, distance = map(int, input().split())
            flights[start].append((end, cost, distance))

        answer = solution(airports, budget, flights_count, flights)
        answers.append(str(answer))

    stdout.writelines(answers)

    return 0


if __name__ == "__main__":
    main()
