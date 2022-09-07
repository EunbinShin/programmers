def solution(s):
    answer = []
    zero_cnt = 0
    cnt = 0

    while s != '1':
        zero_cnt += s.count('0')
        cnt += 1

        s = s.replace('0', '')
        s = bin(len(s))[2:]
        
    answer.append(cnt)
    answer.append(zero_cnt)
    
    return answer