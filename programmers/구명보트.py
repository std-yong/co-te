def solution(people, limit):
    answer = 0
    people.sort()
    
    left = 0
    rigth = len(people) - 1
    
    while left <= rigth:
        if people[left] + people[rigth] <= limit:
            left += 1
            rigth -= 1
        else:
            rigth -= 1
        answer += 1

    return answer