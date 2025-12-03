with open("./input.txt") as f:
    ratings = [list(map(int, l.rstrip())) for l in f]


def find_max(bank, start_idx, end_idx):
    max = max_idx = 0
    for i in range(start_idx, end_idx):
        if bank[i] > max:
            max = bank[i]
            max_idx = i
    return max, max_idx


def calc_max_joltage(digits):
    total = 0
    for bank in ratings:
        max_idx = -1
        for i in range(digits - 1, -1, -1):
            end_idx = len(bank) - i
            max, max_idx = find_max(bank, max_idx + 1, end_idx)
            total += max * (10 ** i)
    return total


print(calc_max_joltage(2))  # part 1
print(calc_max_joltage(12))  # part 2
