for tc in range(10):
    dump = int(input())
    box = list(map(int, input().split()))

    for _ in range(dump):
        max_box = max(box)
        min_box = min(box)
        max_box_index = box.index(max_box)
        min_box_index = box.index(min_box)

        box[max_box_index] -= 1
        box[min_box_index] += 1

    print(f"#{tc+1} {max(box) - min(box)}")
