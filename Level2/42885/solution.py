def solution(people, limit):
    answer = 0
    
    people.sort()
  
    i = 0
    j = len(people) - 1

    #두 명이 탈 수 있는 경우의 수
    while i < j:
        if people[i] + people[j] <= limit:
            people[i] = people[j] = 0
            i = i + 1
            answer += 1
        else:
            j = j - 1

    print(people)

    #한 명이 탈 수 있는 경우의 수
    for p in people:
        if p != 0:
            answer += 1

    return answer

people = [70, 80, 50, 50]
limit = 100
#3
print(solution(people, limit))