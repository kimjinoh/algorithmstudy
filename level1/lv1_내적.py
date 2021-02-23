a = list(map(str, input().split()))
b = list(map(str, input().split()))

# def solution(a, b):
#     answer = 0
#     for i in range(len(a)):
#         answer += a[i]*b[i]
#     return answer

def solution(a, b):
    answer = 0
    for x,y in zip(a,b):
        answer += x*y
    return answer