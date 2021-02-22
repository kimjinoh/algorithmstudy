try:
    n = int(input())
except EOFError as e:
    print(end="")

# def solution(n):
#     answer = ''
#     c1 = '수박'
#     if n == 0:
#         return answer
#     elif n == 1:
#         answer = '수'
#     elif n%2 == 0:
#         answer = c1 * int(n/2)
#     elif n%2 == 1:
#         answer = c1 * (int(n/2)+1)
#         answer = answer[:-1]
#     print(answer)
#     return answer
# solution(n)
###########정석##########
# def solution(n):
#     answer = "수박"*(n//2) + "수"*(n%2)
#     print(answer)
#     return answer
# solution(n)
#########################
#####신박######
def solution(n):
    answer = "수박"*n
    print(answer[:n])
    return answer[:n]
solution(n)
###############

