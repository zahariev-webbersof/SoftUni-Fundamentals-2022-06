class Test:
    __pi = 3.14

    def __init__(self):
        pass


test = Test()
test.__pi += 10
print(test.__pi)