with open("./input.txt") as f:
    ranges = [tuple(map(int, r.split("-"))) for r in f.read().split(",")]

result = 0
for start, end in ranges:
    for n in range(start, end + 1):
        ns = str(n)
        if len(ns) % 2:
            continue
        mid = len(ns) // 2
        left, right = ns[:mid], ns[mid:]
        if left == right:
            result += n

print(result)  # part 1

result = 0
for start, end in ranges:
    for n in range(start, end + 1):
        ns = str(n)
        mid = len(ns) // 2
        for size in range(1, mid + 1):
            parts = []
            i = 0
            while i < len(ns):
                parts.append(ns[i:i + size])
                i += size
            if parts.count(parts[0]) == len(parts):
                result += n
                break

print(result)  # part 2
