def solution(n, words):
    answer = [0, 0]

    word_dict = {}

    for i, word in enumerate(words):
        if i != 0:
            if words[i-1][-1] != words[i][0]:
                #print('틀린단어',i)
                answer[0] = i % n + 1
                answer[1] = i // n + 1
                break

        if word not in word_dict:
            word_dict[word] = 1
        else:
            #print('중복단어',i)
            answer[0] = i % n + 1
            answer[1] = i // n + 1
            break

    return answer 