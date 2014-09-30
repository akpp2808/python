# def func(**kwargs):
#     print kwargs
def func(*args):
    print args

func(*[{'a': 1}, {'b': 2}])