# 주어진 리스트에 특정값 찾기 ,위치 돌려주는 알고리즘
def find(lists,x):
    list_len = len(lists)
    for index in range(list_len):
        if (lists[index] == x):
            return index
    return -1

# 찾는 값이 나오는 모든 위치를 리스트로 돌려주는 알고리즘
def dupfind(lists,x):
    lens = len(lists)
    result = []
    for i in range(lens):
        if x == lists[i]:
            result.append(i)
    return result

# 학생번호 입력 -> 학생번호 해당하는 이름
stu_no = [39,14,67,105]
stu_name = ["Justin","John", "Mike", "Summer"]

def findStudent(s_no, s_name, number):
    lens = len(s_no)
    for index in range(lens):
        if number == s_no[index]:
            return s_name[index]
    return '?'



