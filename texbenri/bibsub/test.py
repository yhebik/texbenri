#!/usr/bin/env python3
import os
import re
import unittest
import texbenri.bibsub.__main__ as tbm


class Test(unittest.TestCase):
    REFFILE = 'testdict.dat'
    TEXFILE = 'testdict.tex'
    FULL = 'The Journal of test'
    AB = 'J. test'

    def setUp(self, ):
        s = '    ' + self.FULL + ' = ' + self.AB + '\n'
        with open(self.REFFILE, 'w') as f:
            f.write(s)
        s = 'journal = {{{0}}}'.format(self.FULL)
        with open(self.TEXFILE, 'w') as f:
            f.write(s)

    def tearDown(self, ):
        for i in (self.REFFILE, self.TEXFILE):
            os.remove(i)

    def testFunc_load_refdict(self, ):
        refdict = tbm.load_refdict([self.REFFILE, ])
        self.assertTrue(self.FULL in refdict.keys())
        self.assertTrue(self.AB in refdict.values())

    def testFunc_bibsub(self, ):
        refdict = {self.FULL: self.AB}
        s = tbm.bibsub(self.TEXFILE, refdict, True)
        self.assertFalse(re.search(self.FULL, s))
        self.assertTrue(re.search(self.AB, s))


if __name__ == '__main__':
    unittest.main()
