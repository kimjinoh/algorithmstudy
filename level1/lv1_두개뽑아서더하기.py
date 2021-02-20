try:
    numbers = list(map(int, input().split()))
except EOFError as e:
    print(end="")
def solution(numbers):
    new_list = []
    answer = []
    for i in range(0, len(numbers)-1):
        for j in range(i+1, len(numbers)):
            ans = numbers[i] + numbers[j]
            new_list.append(ans)
    for a in new_list:
        if a not in answer:
            answer.append(a)
    for i in range(0, len(answer)-1):
        for j in range(i+1, len(answer)):
            if answer[i] > answer[j]:
                tmp = answer[i]
                answer[i] = answer[j]
                answer[j] = tmp
    return answer