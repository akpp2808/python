import weakref, gc
import unittest

KEY = 'same_key'


class Object:
    pass


class TestWeakValueDictionary(unittest.TestCase):
    def test_main(self):
        o = Object()                   # create a reference (first)
        d = weakref.WeakValueDictionary()
        s = weakref.WeakSet([o])        # create a reference (second)
#        b = a    #TODO: error

        d[KEY] = o            # does not create a reference
        # fetch the object if it is still alive
        self.assertIn(o, d.values())
#        for i in d.iteritems():
#            print 'd', i

        del o                       # remove the one reference
        gc.collect()                # run garbage collection right away
        #entry was automatically removed
        self.assertEqual(len(d), 0)


if __name__ == '__main__':
    unittest.main()
