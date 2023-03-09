def ghoul():

    for i in range(1, 1000):
        yield i

print(ghoul()) # not finish # wrong

def say_something():
    print("say something")

    i = 1000
    while i > 7:
        i -= 7
        yield i


for i in ghoul():
    print(i)

