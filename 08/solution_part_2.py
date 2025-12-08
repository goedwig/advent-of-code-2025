with open("./input.txt") as f:
    boxes = [tuple(map(int, l.rstrip().split(","))) for l in f]

circuits = [[box] for box in boxes]
circuit_indexes_by_boxes = {box: i for i, box in enumerate(boxes)}

while True:
    min_box1, min_box2 = None, None
    min_dist = float("inf")

    for i in range(len(circuits) - 1):
        for box1 in circuits[i]:
            x1, y1, z1 = box1
            for j in range(i + 1, len(circuits)):
                for box2 in circuits[j]:
                    x2, y2, z2 = box2
                    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
                    if dist < min_dist:
                        min_box1 = box1
                        min_box2 = box2
                        min_dist = dist

    ni1 = circuit_indexes_by_boxes[min_box1]
    ni2 = circuit_indexes_by_boxes[min_box2]

    for box in circuits[ni2]:
        circuit_indexes_by_boxes[box] = ni1

    circuits[ni1] += circuits[ni2]
    circuits[ni2].clear()

    if circuits.count([]) == len(circuits) - 1:
        print(min_box1[0] * min_box2[0])  # part 2
        break
