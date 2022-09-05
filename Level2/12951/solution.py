def solution(s):
    answer = ''

    firstFlag = True
    for s_char in s:
        if firstFlag:
            answer += s_char.upper()
        else:
            answer += s_char.lower()

        if s_char == ' ':
            firstFlag = True
        else:
            firstFlag = False

    return answer
