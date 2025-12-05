with open("./input.txt") as f:
    range_data, id_data = f.read().split("\n\n")

ids = [int(i) for i in id_data.split()]

ranges = []
for r in range_data.split():
    start, end = map(int, r.split("-"))
    ranges.append((start, end))
ranges.sort()


def merge_ranges(ranges):
    merged_ranges = [ranges.pop(0)]
    any_merged = False
    while ranges:
        r1 = merged_ranges[-1]
        r2 = ranges.pop(0)

        if r1[0] <= r2[1] and r2[0] <= r1[1]:
            r3 = (min(r1[0], r2[0]), max(r1[1], r2[1]))
            merged_ranges.pop(-1)
            merged_ranges.append(r3)
            any_merged = True
        else:
            merged_ranges.append(r2)

    return merged_ranges, any_merged


while True:
    ranges, any_merged = merge_ranges(ranges)
    if not any_merged:
        break

fresh = 0
for i in ids:
    for start, end in ranges:
        if start <= i <= end:
            fresh += 1
            break

print(fresh)  # part 1
print(sum(r[1] - r[0] + 1 for r in ranges))  # part 2
