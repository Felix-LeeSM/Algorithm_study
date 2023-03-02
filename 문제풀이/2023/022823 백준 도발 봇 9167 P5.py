'''
도발 봇 성공다국어
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	333	71	39	21.910%
문제
중세 기사 시대에, 사악한 조롱에 대항하는 정신력, 즉 '멘탈'은 아주 중요한 것이었다.

킹 현우는 자신의 노예들이 약한 멘탈을 갖기를 바라지 않았다. 
그래서 자신의 엄청난 코딩 능력으로 트레이닝용 도발 봇을 만들어냈다.

하지만 현우는 아직 인공지능 수업을 듣지 않았고, 
아는 것이라곤 오토마타 1단원 뿐이었기 때문에 같은 상태에서 
같은 입력을 받는다면 항상 같은 행동을 하는 것이 보장되는 봇 하나를 짜는 것이 고작이었다.

현우가 만든 도발 봇은 아래의 테이블과, 이어 설명할 몇 가지 규칙에 따라 행동한다.

<taunt> ::= <sentence> | <taunt> <sentence> | <noun>! | <sentence>
<sentence> ::= <past-rel> <noun-phrase> | <present-rel> <noun-phrase> | <past-rel> <article> <noun> 
<noun-phrase> ::= <article> <modified-noun>
<modified-noun> ::= <noun> | <modifier> <noun>
<modifier> ::= <adjective> | <adverb> <adjective>
<present-rel> ::= your <present-person> <present-verb>
<past-rel> ::= your <past-person> <past-verb>
<present-person> ::= steed | king | first-born
<past-person> ::= mother | father | grandmother | grandfather | godfather
<noun> ::= hamster | coconut | duck | herring | newt | peril | chicken | vole | parrot | mouse | twit 
<present-verb> ::= is | “masquerades as”
<past-verb> ::= was | personified
<article> ::= a
<adjective> ::= silly | wicked | sordid | naughty | repulsive | malodorous | ill-tempered
<adverb> ::= conspicuously | categorically | positively | cruelly | incontrovertibly
쌍따옴표 안에 있는 문구는 항상 하나의 단어로 취급된다.

위의 표를 읽는 법을 모른다면 이 링크를 참고하자.

봇은 위의 테이블을 참조하여, 아래와 같은 규칙으로 도발을 한다.

'단어'란, 최소 한 개의 영어 알파벳을 포함하고 있으며, 
다른 단어와 최소 한 개 이상의 공백 문자로 구분되어 있는 연속된 문자열을 의미한다.
봇은 우선 상대의 말을 모두 듣는다. 그 이후, 상대의 말에 몇 개의 단어가 있는지에 따라 도발의 수가 결정된다. 
상대가 3개의 단어를 말할 때마다 한 개의 도발을 하며, 
만일 상대가 말한 단어의 수가 3으로 나누어 떨어지지 않는다면 한 번의 도발을 더 한다.
기본적으로 봇이 하는 도발은 위의 테이블에서 <taunt> 하나로 시작하여 재귀적으로 계속 확장하게 된다. 
이때, 자세히 보면 <taunt>가 다시 <taunt>를 만들게 되어 한 문장에 도발이 두 번 들어가는 경우가 있는데, 
이런 경우엔 도발을 두 번 한 것으로 세야 한다. 
만일 상대가 말한 문장이 4개의 단어로 이루어져 있고, 
봇이 한 문장에 도발을 두 번 하게 된다면, 그대로 봇은 임무를 다한 것이다.
어떤 기호에 대한 표현식이 총 N가지이고, 
이 기호를 지금 K번째로 만났으면 ((K-1) mod N) + 1 번째 선택지를 택한다. 
이 선택은 모든 기호에 대해 독립적이다. 
예를 들어, 첫 번째 도발은
<taunt>
=> <sentence>
=> <past-rel> <noun-phrase>
=> your <past-person> <past-verb> <article> <modified-noun>
=> your mother was a <noun>
=> your mother was a hamster
가 되며, 두 번째 도발의 첫 확장 부분은
<taunt>
=> <taunt> <sentence>
=> <noun>! <present-rel> <noun-phrase>
=> ...
이 될 것이다.
이외에 항상 적용되는 특별한 예외 규칙으로, 
상대가 말한 문장에 t-h-e-h-o-l-y-g-r-a-i-l (대소문자 구분 없음) 의 12글자가 순서대로 
(비연속적이어도 상관 없음) 등장한다면, 봇이 처음으로 만드는 도발은 "(A childish hand gesture)." 가 되어야 한다. 
이 도발은 선택지를 거치지 않기 때문에 각 기호들의 선택 상태에 아무 영향을 미치지 않으며, 한 개의 도발로 카운트된다.
킹 현우는 이 복잡한 봇을 통해 노예들을 훈련시킬 것이다.

킹 현우의 도발 봇이 어떻게 행동하게 될 지 시뮬레이션해 보자.

입력
입력은 임의의 여러 줄로 구성된다.

각 줄은 봇의 상대가 말한 내용으로 구성되어 있으며, 항상 알파벳 대소문자, 숫자, ",.-!?", 공백으로만 이루어져 있다.

모든 라인은 최소 1개, 최대 72개의 문자로 이루어져 있으며, 단어는 항상 하나 이상의 공백으로 구분되어져 있다.

모든 라인에 대해, 단어가 0개인 경우는 없다.

출력
각 입력에 대해, 아래와 같이 출력한다.

"Knight:", 스페이스(아스키 코드 32), 입력된 문장을 순서대로 출력한다. 
이때, 입력에 만일 1개 이상의 공백 문자(스페이스, 탭)가 있다면 모두 단 하나의 스페이스(아스키 코드 32)로 대체되어야 한다.
"Taunter:", 스페이스(아스키 코드 32) , 입력에 맞는 도발, 마침표 하나를 필요한 도발 수만큼 순서대로 출력한다. 
각 단어는 항상 하나의 스페이스(아스키 코드 32)로 구분되어야 한다.
위의 두 출력단이 끝나면, 빈 줄 하나를 추가로 출력한다.
모든 도발은 대문자로 시작해야 하며, 추가적인 공백 문자가 있어서는 안 된다.

쌍따옴표 안에 있는 문구는 항상 하나의 단어로 취급되며, 쌍따옴표는 도발에 포함되지 않는다. 
도발을 출력할 때, 도발 앞과 뒤에 위에서 설명한 공백 문자 이외에 다른 공백 문자가 있어서는 안 된다.

예제 입력 1 
Hello! 
Are you feeling alright? 
Is there someone else I could talk to? 
Anyone at    all? 
We seek the holy grail . . .
예제 출력 1 
Knight: Hello! 
Taunter: Your mother was a hamster. 

Knight: Are you feeling alright? 
Taunter: Coconut! Your steed is a silly duck. 

Knight: Is there someone else I could talk to? 
Taunter: Your father personified a herring. 
Taunter: Your grandmother was a newt. 
Taunter: Peril! Your king masquerades as a conspicuously wicked chicken. 

Knight: Anyone at all? 
Taunter: Your grandfather personified a vole. 

Knight: We seek the holy grail . . . 
Taunter: (A childish hand gesture). 
Taunter: Your godfather was a parrot.
'''
from sys import argv, stdin
input = stdin.readline


def holyGrail(line: str) -> bool:
    key = 'holygrail'
    cur = 0
    for char in line:
        if char == key[cur]:
            cur += 1
            if cur == len(key):
                return True
    return False


def wordCount(line: str):
    wCnt = 0
    alpha = False
    for char in line:
        if char == ' ':
            wCnt += alpha
            alpha = False
            continue
        if ord('a') <= ord(char.lower()) <= ord('z'):
            alpha = True
    wCnt += alpha

    return wCnt


def clearDoubleSpace(line: str):
    return ' '.join(line.split())


def makeTaunt():
    tree = {
        'taunt': [['sentence'], ['taunt', 'sentence'], ['noun!'], ['sentence']],
        'sentence': [['past-rel', 'noun-phrase'], ['present-rel', 'noun-phrase'], ['past-rel', 'article', 'noun']],
        'noun-phrase': [['article', 'modified-noun']],
        'modified-noun': [['noun'], ['modifier', 'noun']],
        'modifier': [['adjective'], ['adverb', 'adjective']],
        'present-rel': [['your', 'present-person', 'present-verb']],
        'past-rel': [['your', 'past-person', 'past-verb']],
    }
    leaves = {
        'present-person': ['steed', 'king', 'first-born'],
        'past-person': ['mother', 'father', 'grandmother', 'grandfather', 'godfather'],
        'noun': ['hamster', 'coconut', 'duck', 'herring', 'newt', 'peril', 'chicken', 'vole', 'parrot', 'mouse', 'twit'],
        'present-verb': ['is', 'masquerades as'],
        'past-verb': ['was', 'personified'],
        'article': ['a'],
        'adjective': ['silly', 'wicked', 'sordid', 'naughty', 'repulsive', 'malodorous', 'ill-tempered'],
        'adverb': ['conspicuously', 'categorically', 'positively', 'cruelly', 'incontrovertibly'],
        'your': ['Your'],
        '!': ['!']
    }

    cnts = {k: -1 for k in leaves.keys()}
    cnts.update({k: -1 for k in tree.keys()})

    def taunt(key: str):
        if key == 'noun!':
            key = 'noun'
            cnts[key] += 1
            return leaves[key][cnts[key] % len(leaves[key])].capitalize()+'!'

        cnts[key] += 1
        if key in leaves:
            return leaves[key][cnts[key] % len(leaves[key])]

        ret = []

        for part in tree[key][cnts[key] % len(tree[key])]:
            ret.append(taunt(part))

        return ' '.join(ret)

    def make_cntr():
        cnt = -1

        def cntr():
            nonlocal cnt
            temp = cnt
            cnt = cnts['taunt']
            return cnt-temp
        return cntr
    return taunt, make_cntr()


def solution(inputs: list[str]):
    ret = []
    gesture = '(A childish hand gesture)'
    taunt, tntCntr = makeTaunt()
    tntsReq = 0
    tntsDone = 0

    for wCnt, flag, line in zip(
            map(wordCount, inputs),
            map(holyGrail, inputs),
            map(clearDoubleSpace, inputs)):

        temp = []
        temp.append(f'Knight: {line}')

        tntsReq += wCnt//3 + (wCnt % 3 > 0)

        curDone = 0

        while tntsReq > tntsDone+curDone:
            if flag:
                temp.append(f'Taunter: {gesture}.')
                flag = False
                curDone += 1
                continue

            temp.append(f'Taunter: {taunt("taunt")}.')
            curDone += tntCntr()

        tntsDone = min(curDone+tntsDone, tntsReq)
        ret.append('\n'.join(temp))

    return '\n\n'.join(ret)


def main(args=argv) -> int:
    inputs = [s.strip() for s in stdin]
    answer = solution(inputs)

    print(answer)
    return 1


if __name__ == '__main__':
    main()
