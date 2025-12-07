with open("./input.txt") as f:
    diagram = [list(l.rstrip()) for l in f]

rows, cols = len(diagram), len(diagram[0])

splitters = []
for i in range(rows):
    for j in range(cols):
        if diagram[i][j] == "^":
            splitters.append((i, j))

splitters_involved = set()
graph = {}
for i in range(len(splitters)):
    s1 = splitters[i]
    graph[s1] = set()

    for s2 in splitters[i + 1:]:
        if s1[1] + 1 == s2[1]:
            splitters_involved.add(s2)
            graph[s1].add(s2)
            break
    else:
        graph[s1].add((rows - 1, s1[1] + 1))

    for s2 in splitters[i + 1:]:
        if s1[1] - 1 == s2[1]:
            splitters_involved.add(s2)
            graph[s1].add(s2)
            break
    else:
        graph[s1].add((rows - 1, s1[1] - 1))

print(len(splitters_involved) + 1)  # extra 1 for the first splitter


def calc_paths(node, memo):
    if node not in graph:
        return 1

    if node in memo:
        return memo[node]

    total = 0
    for neighbor in graph[node]:
        total += calc_paths(neighbor, memo)
    memo[node] = total
    return total


print(calc_paths(splitters[0], {}))
