# -*- coding: utf-8 -*-
# def increase(func):
#     def gen(a, b):
#         a += 1
#         return func(a, b)
#     return gen
# 
# 
# # @increase
# def Sum(a, b):
#     print 'a', a, 'b', b
#     return a + b
# 
# Sum = increase(Sum)
# print Sum(2,4)


def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped


def makecustom(arg):
    def real_makecustom(fn):
        def wrapped():
            return "<" + arg +">" + fn() + "</" + arg + ">"
        return wrapped
    return real_makecustom


@makeitalic
@makebold
@makecustom('a')
def hello():
    return "hello habr"

print hello() ## выведет <b><i>hello habr</i></b>

