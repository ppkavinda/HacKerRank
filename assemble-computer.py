def computers(comps):
    req_list = ["A", "D", "X", "Y", "P", "R"]
    comp_list = []

    for comp in comps:
        comp_list.append(comp)

    a = comp_list.count(req_list[0])
    d = comp_list.count(req_list[1])
    x = comp_list.count(req_list[2])
    y = comp_list.count(req_list[3])
    p = comp_list.count(req_list[4])
    r = comp_list.count(req_list[5])

    print(min(a, d, x, y, p, r))

computers(input())
