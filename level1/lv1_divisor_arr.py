arr = list(map(int, input().split()))
divisor = int(input())
# def solution(arr, divisor):
#     answer = []
#     for i in arr:
#         if i % divisor == 0:
#             answer.append(i)
#     if len(answer) == 0:
#         answer.append(-1)
#     return answer

def solution(arr, divisor):
    answer = [i for i in arr if i % divisor ==0]
    answer.sort()
    if len(answer)==0:
        answer.append(-1)
    return answer