def solution(S):
    sentences = S.replace("?", ".").replace("!", ".").split(".")
    return max([len(x.split()) for x in sentences])

print(solution('We test coders. Give us a try?'))
