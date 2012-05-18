#class Foo:
#    m = Bar()

#class Bar:
#    m = Foo()


class Foo:
  def __init__(self):
    self.m = Bar()

class Bar:
  def __init__(self):
    self.m = Foo()