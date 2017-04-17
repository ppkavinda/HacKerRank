from sys import stdin


def eggs(x):
    count = 0
    i1_list = []
    i2_list = []
    grid = [[0 for _ in range(100)] for _ in range(100)]

    while count < int(x):
        i1 = stdin.readline()
        i2 = stdin.readline()

        i1_list = i1.split()
        i2_list = i2.split()

        a = i1_list[0]
        b = i2_list[1]

        u = 0
        while u < a:
            grid[:a][:] += 1
            u += 1

        v = 0
        while v < b:
            grid[:][:b] += 1
            v += 1


eggs(input())
