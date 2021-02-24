s = list(map(str,input().split()))
n = int(input())
########실패##########
# def solution(s, n):
#     new_dic = {}
#     new_list = []
#     answer = []
#     for i in range(len(s)):
#         new_list.append(s[i][n])
#         new_dic[s[i]] = s[i][n]
#     new_list.sort()
#     for i in range(len(s)):
#         key = next(key for key, value in new_dic.items() if value == new_list[i])
#         answer.append(key)
#     return answer
#####################
#
# def solution(strings, n):
#     for i in range(len(strings)-1):
#         for j in range(i+1, len(strings)):
#             if strings[i][n] > strings[j][n]:
#                 temp = strings[i]
#                 strings[i] = strings[j]
#                 strings[j] = temp
#             elif strings[i][n] == strings[j][n]:
#                 if strings[i] > strings[j]:
#                     temp = strings[i]
#                     strings[i] = strings[j]
#                     strings[j] = temp
#                 else:
#                     continue
#             else:
#                 continue
#     return strings

def strange_sort(strings, n):
    return sorted(strings, key=lambda x: x[n])

strings = ["sun", "bed", "car"]
print(strange_sort(strings, 1))