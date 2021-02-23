arr = list(map(int, input().split()))

# def solution(arr):
#     answer =[]
#     for i in range(len(arr)-1):
#         if arr[i] != arr[i+1]:
#             answer.append(arr[i])
#     answer.append(arr[-1])
#     print(answer)
#     return answer
# solution(arr)

# def solution(arr):
#     answer =[]
#     for i in arr:
#         if answer[-1:] == [i]:
#             continue
#         answer.append(i)
#     print(answer)
#     return answer
# solution(arr)

def solution(arr):
    answer = []
    for i in arr:
        if len(answer) == 0 or answer[-1] != i:
            answer.append(i)
    print(answer)
    return answer
solution(arr)
