from sys import stdin


def exe(x):
    cou = 0
    l = []
    while cou < int(x):
        y = stdin.readline()
        z = stdin.readline()
        total_len = 0
        rope_len = z.split()

        i = 0
        for _ in rope_len:
            rope_len[i] = int(rope_len[i])
            i += 1

        for q in rope_len:
            total_len += q
            total_len -= 2

        l.append(total_len + 2)
        cou += 1

    for r in l:
        print(r)

c = stdin.readline()
exe(c)
