try:
    participant = list(map(str, input().split()))
    completion = list(map(str, input().split()))
except EOFError as e:
    print(end="")
##################정렬 후 비교####################

# def solution(participant, completion):
#     answer = ''
#     part = sorted(participant)
#     comp = sorted(completion)
#     for j in range(len(completion)):
#         if part[j] != comp[j]:
#             answer = part[j]
#             break
#     if answer == '':
#         answer = part[-1]
#     print(answer)
#     return answer
# solution(participant, completion)
##################################################
###################카운터 객체 사용#################
# import collections
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]
# answer = collections.Counter(participant) - collections.Counter(completion)
# print(answer)
#######io####
# stan mimi kiki leo mimi
# mimi kiki leo stan
# Counter({'mimi': 1})
#############
##################################################

###################해시함수 사용#################
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
        print(temp)
    for com in completion:
        temp -= hash(com)
        print(temp)
    answer = dic[temp]
    print(dic)
    return answer
solution(participant, completion)
##################################################