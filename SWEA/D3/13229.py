day_dict = {
    "MON": 1,
    "TUE": 2,
    "WED": 3,
    "THU": 4,
    "FRI": 5,
    "SAT": 6,
    "SUN": 7,
}

t = int(input())
for tc in range(t):
    day = str(input())

    if 7 - day_dict[day] == 0:
        print("#{} {}".format(tc+1, 7))
    else:
        print("#{} {}".format(tc+1, 7-day_dict[day]))
