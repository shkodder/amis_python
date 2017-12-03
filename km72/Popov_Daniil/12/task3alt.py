def set_groups(l):
    global result
    group = []
    result = [group]
    expect = None
    for i in l:
        if (i == expect) or (expect is None):
            group.append(i)
        else:
            group = [i]
            result.append(group)
        expect = i
    return result
print(set_groups([2,3,3,4,5,5,5,6,7,1,1]))
def solution(result):
    answer=[]
    for j in result:
        answer.append(len(j))
    return max(answer)
print (solution(result))

