try:
    participant = list(map(str, input().split()))
    completion = list(map(str, input().split()))
except EOFError as e:
    print(end="")

def solution(participant, completion):
    answer = ''
    part = sorted(participant)
    comp = sorted(completion)
    for j in range(len(completion)):
        if part[j] != comp[j] :
            answer = part[j]
            break
    if answer == '':
        answer = part[-1]
    #count = []
    # for i in range(len(participant)):
    #     count.append(0)
    #     for j in range(i+1, len(participant)):
    #         if participant[i] == participant[j]:
    #             count[i] += 1
    #     for j in range(len(completion)):
    #         if participant[i] == completion[j]:
    #             count[i] -= 1
    #     if count[i] == 0:
    #         answer = participant[i]
    # for i in range(len(participant)):
    #     if participant.count(participant[i]) != completion.count(participant[i]):
    #         answer = participant[i]
    #         break
    print(answer)
    return answer
solution(participant, completion)
