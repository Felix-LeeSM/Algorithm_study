


def solution(id_list, report, k):
    reported = {i : [] for i in id_list} # k가 v에게 신고당함 >> len(reported[key]) >= k인 key를 찾아야 함. 
    mails_togo = {i : 0 for i in id_list}
    for i in set(report):
        reported[i.split()[1]].append(i.split()[0]) # 신고 당한 사람 : 신고 한 사람.
    banned = [i for i in reported if len(reported[i]) >= k] # 밴 당한 사람.
    for i in banned:
        for j in reported[i]:
            mails_togo[j] += 1
    return [mails_togo[i] for i in id_list] # dictionary는 python 3.5버젼 이하에서 순서가 보장되지 않으므로, id_list를 기준으로 하여 새로운 list 작성