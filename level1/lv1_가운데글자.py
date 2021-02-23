s = input()

# def solution(s):
#     answer = ''
#     a = len(s)
#     a = a//2
#     if len(s) % 2 == 0:
#         answer = s[a-1] + s[a]
#     else:
#         answer = s[a]
#     print(answer)
#     return answer
# solution(s)
def solution(s):
    answer = ''
    answer = s[(len(s)-1)//2:len(s)//2+1]
    print(answer)
    return answer
solution(s)