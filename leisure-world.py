from sys import stdin


def leisure_world(n, inst):
    inst_list = inst.split()
    speed = 0
    ind = 0
    
    for _ in inst_list:
        inst_list[ind] = int(inst_list[ind])
        ind += 1

    for x in inst_list:
        speed += x
        if speed < 0:
            speed = 0

    print(speed)

a = stdin.readline()
b = stdin.readline()

leisure_world(a, b)
