# -*- coding: utf-8 -*-

def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeitalic(fn):
    def wrapped(*args):
        return "<i>" + fn(*args) + "</i>"
    return wrapped


def makecustom(arg):
    def real_makecustom(fn):
        def wrapped(*args):
            return "<" + arg +">" + fn(*args) + "</" + arg + ">"
        return wrapped
    return real_makecustom


# @makeitalic
# @makebold
@makecustom('a')
def hello(name):
    return "hello %s" % name

print hello('Ivan') ## выведет <b><i>hello habr</i></b>