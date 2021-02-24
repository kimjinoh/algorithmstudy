s = input()

# def solution(s):
#     s = list(s)
#     cnt = [0,0]
#     for i in s:
#         if i == 'p' or i == 'P':
#             cnt[0] += 1
#         elif i == 'y' or i =='Y':
#             cnt[1] += 1
#     if cnt[0] == cnt[1]:
#         return True
#     else: return False

def solution(s):
    return s.lower().count('p') == s.lower().count('y')