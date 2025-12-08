from functools import reduce
from operator import mul

with open("./input.txt") as f:
    boxes = [tuple(map(int, l.rstrip().split(","))) for l in f]

circuits = [[box] for box in boxes]
circuit_indexes_by_boxes = {box: i for i, box in enumerate(boxes)}

last_min_dist = float("-inf")
for _ in range(1000):
    min_box1, min_box2 = None, None
    min_dist = float("inf")

    for box1 in boxes:
        x1, y1, z1 = box1
        for box2 in boxes:
            if box1 == box2:
                continue
            x2, y2, z2 = box2
            dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
            if min_dist > dist > last_min_dist:
                min_box1 = box1
                min_box2 = box2
                min_dist = dist

    last_min_dist = min_dist

    ni1 = circuit_indexes_by_boxes[min_box1]
    ni2 = circuit_indexes_by_boxes[min_box2]

    if ni1 == ni2:  # already in the same circuit
        continue

    for box in circuits[ni2]:
        circuit_indexes_by_boxes[box] = ni1

    circuits[ni1] += circuits[ni2]
    circuits[ni2].clear()

circuits.sort(key=len, reverse=True)
print(reduce(mul, map(len, circuits[:3])))  # part 1
