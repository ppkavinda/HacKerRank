def count_game(lucky_no):
    count = 0
    position = 0
    inc = 0

    while not count == lucky_no:
        count += 1

        if inc % 2 == 0:
            position += 1
            if position == 1338:
                position = 1
        else:
            position -= 1
            if position == 0:
                position = 1337

        if count % 7 == 0 or "7" in str(count):
            inc += 1

    print(position)

x = input()
count_game(int(x))
