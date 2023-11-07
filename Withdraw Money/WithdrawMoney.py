def withdrawMoney(id, total, path):
    global Count
    if total == S:
        ways.append(path)
        Count = Count + 1
        return True

    for i in range(id, n):
        if t[i] + total <= S:
            withdrawMoney(i, total + t[i], path + [t[i]])


# Read input from a file
with open('input10.txt', 'r') as f:
    n, S = map(int, f.readline().split())
    t = list(map(int, f.readline().split()))

t.sort()
Count = 0
ways = []
withdrawMoney(0, 0, [])

# Write output to a file
with open('output10.txt', 'w') as f:
    f.write(str(Count) + '\n')
    for way in ways:
        f.write(' '.join(map(str, way)) + '\n')
