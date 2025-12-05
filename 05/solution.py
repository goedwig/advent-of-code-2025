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
    for r1 in ranges:
        r2 = merged_ranges[-1]
        if r1[0] <= r2[1] and r2[0] <= r1[1]:
            merged_ranges[-1] = (min(r1[0], r2[0]), max(r1[1], r2[1]))
        else:
            merged_ranges.append(r1)

    return merged_ranges


ranges = merge_ranges(ranges)

fresh = 0
for i in ids:
    for start, end in ranges:
        if start <= i <= end:
            fresh += 1
            break

print(fresh)  # part 1
print(sum(r[1] - r[0] + 1 for r in ranges))  # part 2
