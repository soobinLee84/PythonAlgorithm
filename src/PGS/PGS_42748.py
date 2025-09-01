def solution( commands, array):
    answer=[]


    # array = [1, 5, 2, 6, 3, 7, 4]
    # commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    # k 값 구하기

# 파이썬은 똑똑함으로 2차원 for 문 자동으로 돌려줌
# 대신 commands = [[2, 5, 3], [4, 4], [1, 7, 3, 9]] 이경우는 for 문을 2번 돌려야함 길이가 모두 같은 2차원만 자동으로 똑띠하게 돌려줌
    for i,j,k in commands:
        part = array[i-1:j]
        sorted_part = sorted(part) 
        # 파이썬 0부터 셈으로 -1 해줘야함
        picked = sorted_part[k-1] 
        answer.append(picked)

    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(commands, array))
