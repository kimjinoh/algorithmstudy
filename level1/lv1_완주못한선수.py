try:
    participant = list(map(str, input().split()))
    completion = list(map(str, input().split()))
except EOFError as e:
    print(end="")

def solution(participant, completion):
    answer = ''
    count = []
    for i in range(len(participant)):
        count.append(0)
        for j in range(i+1, len(participant)):
            if participant[i] == participant[j]:
                count[i] += 1
        for j in range(len(completion)):
            if participant[i] == completion[j]:
                count[i] -= 1
        if count[i] != -1:
            answer = participant[i]
    # for i in range(len(participant)):
    #     for j in range(len(completion)):
    #         if participant[i] not in completion:
    #             answer = participant[i]
    print(answer)
    return answer
solution(participant, completion)