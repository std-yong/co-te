def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            answer += (absolutes[i] * 1)
        elif signs[i] == False:
            answer += (absolutes[i] * -1)
            
    return answer