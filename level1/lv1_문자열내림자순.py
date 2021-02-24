s = input()

def solution(s):
    s = list(s)
    answer = ''
    s.sort(reverse=True)
    for i in s:
        answer += i
    print(answer)
    return answer
solution(s)

# def solution(s):
#     answer = ''.join(sorted(s, reverse=True))
#     print(answer)
#     return answer
# solution(s)