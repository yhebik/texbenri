#!/usr/bin/env python3
import os
import re
import unittest
import texbenri.bundle.__main__ as tbm


class Test(unittest.TestCase):
    TEMP = 'test_file/'
    TARGET = 'test'
    FLIST = ['f1.eps', 'f2.eps']

    def setUp(self, ):
        os.mkdir(self.TEMP)
        s = ''
        s += '\graphicspath{ {./}, {../} }\n'
        for eps in self.FLIST:
            s += '\includegraphics[width=\hsize]{{{0}}}\n'.format(eps)
        with open(self.TEMP+self.TARGET+'.tex', 'w') as f:
            f.write(s)
        for eps in self.FLIST:
            with open(self.TEMP+eps, 'w') as f:
                f.write('')
        os.chdir(self.TEMP)

    def tearDown(self, ):
        import shutil
        os.chdir('..')
        shutil.rmtree(self.TEMP)

    def testFunc_parse_graphicspath(self, ):
        r = tbm.parse_graphicspath(self.TARGET+'.tex')
        [self.assertTrue(si in r) for si in ['./', '../']]

    def testFunc_get_graphics_list(self, ):
        ls = tbm.get_graphics_list(self.TARGET+'.tex')
        self.assertTrue(isinstance(ls, tuple))

    def testFunc_replace_graphics(self, ):
        fmt = 'Fig{0:d}{1}'
        s = tbm.replace_graphics(self.TARGET+'.tex', fmt, True)
        self.assertFalse(re.search(self.FLIST[0], s))
        self.assertTrue(re.search(fmt.format(1, '.eps'), s))

    def testFunc_copy_figs(self, ):
        fmt = 'Fig{0:d}{1}'
        prefix = 'test_prefix'
        os.mkdir(prefix)
        tbm.copy_figs(self.TARGET+'.tex', fmt, prefix)
        self.assertTrue(fmt.format(1, '.eps') in os.listdir(prefix))


if __name__ == '__main__':
    unittest.main()
