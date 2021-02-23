try:
    a = int(input()) # month
    b = int(input()) # day
except EOFError as e:
    print(end="")

# def solution(a, b):
#     answer = ''
#     day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
#     sum = 0
#     if a < 3:
#         sum = (a-1)*31 + b
#     else :
#         sum = (a//2)*31 + (((a-1)//2)-1)*30 + 29 + b
#         if a > 8 and a % 2 == 1:
#             sum += 1
#     answer = day[sum%7-1]
#     print(answer)
#     return answer
# solution(a,b)

def solution(a, b):
    mon = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    aa = sum(mon[:(a-1)])+b
    answer = day[aa%7-1]
    return answer
