def solution(s):
    answer = ''
    s = s.split(" ")
    for word in s:
        for i in range(len(word)):
            if i%2:
                answer += word[i].lower()
            else:
                answer += word[i].upper()
        answer += ' '
    return answer[:-1]