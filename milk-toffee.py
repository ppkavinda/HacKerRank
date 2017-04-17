from sys import stdin


def amount_of_toffee(students):
    scores = []

    i = 0
    while i < int(students):
        scores.append(stdin.readline())
        i += 1

    j = 0
    for _ in scores:
        scores[j] = int(scores[j])
        j += 1

    toffee = [1 for _ in scores]

    for _ in scores:
        c = 0
        while c < len(scores) - 1:
            current = scores[c]
            nxt = scores[c + 1]
            if current > nxt:
                if not toffee[c] > toffee[c + 1]:
                    toffee[c] = toffee[c + 1] + 1
            if current < nxt:
                if not toffee[c] < toffee[c + 1]:
                    toffee[c + 1] = toffee[c] + 1
            c += 1

    total = 0
    for tof in toffee:
        total += tof

    print(scores)
    print(toffee)
    print(total)

a = stdin.readline()
amount_of_toffee(a)
