# 회문 찾기
def palindrome(s):
    qu = []
    st = []
    for x in s:
        if x.isalpha():
            qu.append(x.lower)
            st.append(x.lower)
    while qu:
        if qu.pop(0) != st.pop():
            return False
    return True

# 큐,스택X 회문
def palindrome_sub(s):
   i = 0
   j = len(s) - 1
   while i < j:
    if s[i].isalpha() == False:
        i += 1
    elif s[j].isalpha() == False:
        j -= 1
    elif s[i].lower() != s[j].lower():
        return False
    else:
        i += 1
        j -+ 1
    return True

