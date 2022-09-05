def solution(s):
    answer = []

    s = s[1:-1]
    s_tmp_list = s.split('},')
    s_tmp_list.sort(key=lambda x: len(x))

    s_list = []

    for tmp in s_tmp_list:
        if '{' in tmp:
            tmp = tmp[1:]
        if '}' in tmp:
            tmp = tmp[:-1]

        s_list.append(tmp)

    for s1 in s_list:
        s1_list = list(map(int, s1.split(',')))

        for s2 in s1_list:
            if s2 not in answer:
                answer.append(s2)

    return answer
