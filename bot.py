def ghoul():
    for i in range(1, 1000):
        yield i

print(ghoul()) # not finish # wrong

def say_something():
    print("say something")