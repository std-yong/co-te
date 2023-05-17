def solution(weights):
    count = 0
    rate = [(2, 3), (2, 4), (3, 4), (4, 3), (4, 2), (3, 2)]
    dic = {}
    for i in weights:
        dic.setdefault(i, 0)
        dic[i] += 1
        
    for i in dic:
        #중복값 있을 때
        if dic[i] > 1:
            count += dic[i] * (dic[i]-1) // 2
            
        #비율로 봤을때 가능하면 count 추가
        for (j, k) in rate:
            good = i * j / k
            if (good in dic):
                count += dic[i] * dic[good]
                
        #제거 (두번 계산 방지)
        dic[i] = 0

    return count