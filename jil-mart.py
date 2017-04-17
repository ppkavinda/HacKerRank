def a_of_pal(txt):
    ans = ''
    txt_list = []
    set_list = []

    for letter in txt:
        txt_list.append(letter)

    for item in txt_list:
        if item not in set_list:
            set_list.append(item)

    if len(txt_list) % 2 == 0:
        for i in set_list:
            if txt_list.count(i) % 2 == 0:
                ans = "YES"
            else:
                ans = "NO"
                break
    else:
        count = 0
        for it in set_list:
            if txt_list.count(it) % 2 == 0:
                ans = "YES"
            else:
                if count == 0:
                    count = 1
                    ans = "YES"
                else:
                    ans = "NO"
                    break

    print(ans)

a_of_pal(input())
