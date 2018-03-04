def yield_use():
    i = 1
    while i < 10:
        if i / 2 - i // 2 == 0:
            print("偶数", i, i / 2, i // 2)
            yield i
            print("偶数")
        i += 1


def func():
    global i
    for item in yield_use():
        print("ok", item, end="\n")


func()
