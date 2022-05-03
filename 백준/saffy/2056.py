t = int(input())

for i in range(t):
    date = list(input())
    yyyy = date[0]+date[1]+date[2]+date[3]
    mm = date[4]+date[5]
    dd = int(date[6]+date[7])

    if mm == '01' or mm == '03' or mm == '05' or mm == '07' or mm == '08' or mm == '10' or mm == '12':
        if dd >= 1 and dd <= 31:
            print("#{} {}/{}/{}".format(i+1, yyyy, mm, str(dd).zfill(2)))
        else:
            print("#{} {}".format(i+1, -1))
    elif mm == '04' or mm == '06' or mm == '09' or mm == '11':
        if dd >= 1 and dd <= 30:
            print("#{} {}/{}/{}".format(i+1, yyyy, mm, str(dd).zfill(2)))
        else:
            print("#{} {}".format(i+1, -1))
    elif mm == '02':
        if dd >= 1 and dd <= 28:
            print("#{} {}/{}/{}".format(i+1, yyyy, mm, str(dd).zfill(2)))
        else:
            print("#{} {}".format(i+1, -1))
    else:
        print("#{} {}".format(i+1, -1))
