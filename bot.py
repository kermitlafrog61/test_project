def ghoul():
    i = 1000
    while i > 7:
        i -= 7
        yield i


for i in ghoul():
    print(i)


def say_something():
    print("say something")
