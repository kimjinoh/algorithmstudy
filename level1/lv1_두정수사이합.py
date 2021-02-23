a = int(input())
b = int(input())

def solution(a, b):
    answer = (abs(a-b)+1)*(a+b)//2
    return answer
#
# def solution(a,b):
#     if a > b :
#         a, b = b, a
#     answer = sum(range(a, b+1))
#     return answer