n = int(input())
data = [list(map(int, input().split())) for _ in range(6)]
max_width = 0
max_height = 0
width_index = 0
height_index = 0

for i in range(len(data)):
    if data[i][0] == 1 or data[i][0] == 2:
        if data[i][1] > max_width:
            max_width = data[i][1]
            width_index = i
    elif data[i][0] == 3 or data[i][0] == 4:
        if data[i][1] > max_height:
            max_height = data[i][1]
            height_index = i

min_width = abs(data[(width_index - 1) % 6][1] -
                data[(width_index + 1) % 6][1])

min_height = abs(data[(height_index - 1) % 6][1] -
                 data[(height_index + 1) % 6][1])
total_area = max_width * max_height
part_area = min_width * min_height

print((total_area - part_area) * n)
