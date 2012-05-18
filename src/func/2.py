import inspect


def myFunc():
    print locals()
    print globals()


def n():
    myFunc()
    print myFunc

n()