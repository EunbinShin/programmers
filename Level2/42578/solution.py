def solution(clothes):
    answer = 1
    cloth_dict = {}

    for cloth in clothes:
        if cloth[1] not in cloth_dict.keys():
           cloth_dict[cloth[1]] = 1
        else:
            cloth_dict[cloth[1]] += 1
    
    for v in cloth_dict.values():
        answer *= (v + 1)

    return answer - 1