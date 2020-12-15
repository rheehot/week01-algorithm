# 평균은 넘겠지 - 16m 28s

'''
case_num = int(input())
cases = []
for _ in range(case_num):
    cases.append(list(map(int, input().split())))

for i in range(len(cases)):
    avg = sum(cases[i][1:])/cases[i][0]
    count = 0
    for j in range(1, len(cases[i])):
        if cases[i][j] > avg:
            count += 1
    answer = format(float(count)/float(cases[i][0])*100, ".3f")
    print(f'{answer}%')
'''
'''
소수점으로 나타내기
round(숫자, 몇째자리숫자까지?)
format(숫자, 어떻게?".2f")
'''

N = int(input())
cases = []

for _ in range(N):
    cases.append(list(map(int, input().split())))

for case in cases:
    l = len(case)
    avg = (sum(case[1:l]) / (l-1))
    count = 0
    for s in case[1:l]:
        if s > avg:
            count += 1

    temp = count / (l-1) * 100
    answer = format(temp, ".3f")
    print(f"{answer}%")
