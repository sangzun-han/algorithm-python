#동명이인 찾기

def find_same_name(n):
  name_dict = dict()
  for name in n:
    if name in name_dict:
      name_dict[name] += 1
    else:
      name_dict[name] = 1
    
  result = set()
  for name in name_dict:
    if name_dict[name] >= 2:
      result.add(name)
  return result

# 학생번호로 학생이름 찾기
def get_name(s_info,find_no):
  if find_no in s_info:
    return s_info[find_no]
  else:
    return "?"
  
