def simple(a):
    a += 1

def complexity2(b):
    if b is not None:
        print("Not none")

def complexity4(c):
    if c is None:
        print("None")
    elif c == 1:
        print("One")
    elif c == 2:
        print("Two")
    elif c == 3:
        # degraded
        print("Three")
    else:
        print("More")

def goodnew():
    print("i am simple")
