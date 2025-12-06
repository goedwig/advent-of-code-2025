with open("./input.txt") as f:
    data = f.readlines()

m_1 = [list(l.split()) for l in data]
m_1 = list(zip(*m_1))  # transpose

part_1 = 0
for values in m_1:
    expr = values[-1].join(values[:-1])
    part_1 += eval(expr)

print(part_1)

m_2 = [list(l) for l in data]
m_2 = list(zip(*m_2))  # transpose

part_2 = 0
terms = ["0"]
op = ""
for values in m_2:
    if values[-1] in ("+", "*"):
        expr = op.join(terms)
        part_2 += eval(expr)
        terms = []
        op = values[-1]
        values = values[:-1]

    term = "".join(values).strip()
    if term:  # skip empty columns
        terms.append(term)

expr = op.join(terms)
part_2 += eval(expr)

print(part_2)
