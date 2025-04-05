from typing import List


def solution(schedules, timelogs, startday):
    answer = 0
    for schedule, logs in zip(schedules, timelogs):
        schedule = parse_time(schedule)
        logs = list(map(parse_time, logs))
        logs = filter_weekend(logs, startday)
        diffs = map(lambda log: time_diff(log, schedule), logs)

        answer += all(map(lambda diff: diff <= 10, diffs))

    return answer


def parse_time(num: int) -> int:
    return (num // 100) * 60 + num % 100


def time_diff(one: int, another: int) -> int:
    return one - another


def filter_weekend(timelogs: List[int], start_day: int) -> List[int]:
    return list(
        map(lambda day_log: day_log[1],
            filter(lambda day_log: day_log[0] not in (6, 7, 13, 14),
                   enumerate(timelogs, start=start_day))))


assert 3 == solution(
    [700, 800, 1100],
    [
        [710, 2359, 1050, 700, 650, 631, 659],
        [800, 801, 805, 800, 759, 810, 809],
        [1105, 1001, 1002, 600, 1059, 1001, 1100]
    ],
    5
)

assert 2 == solution(
    [730, 855, 700, 720],
    [
        [710, 700, 650, 735, 700, 931, 912],
        [908, 901, 805, 815, 800, 831, 835],
        [705, 701, 702, 705, 710, 710, 711],
        [707, 731, 859, 913, 934, 931, 905]
    ],
    1)
