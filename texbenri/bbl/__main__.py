#!/usr/bin/env python3
import re


class ConverterCollection(object):
    """Convert bbl contents into a format as simple as possible."""
    def __init__(self, bbls):
        """ """
        self.bbls = bbls[:]

    def conv_acsrev(self, ):
        """acsrev (revtex4) converter."""
        s = self.bbls
        s = re.sub('\\\\bibitem\[.*?\]', '\\\\bibitem', s, flags=re.S)
        s = re.sub('\\\\bibinfo{.*?}', '', s)
        s = re.sub('\\\\bibf?namefont', '', s)
        s = re.sub('\\\\emph', '\\\\textit', s)
        return s

    def conv_aip(self, ):
        """aip convertor"""
        s = self.bbls
        s = re.sub('\s?\\\\newblock', '', s)
        s = re.sub('\\\\em', '\\\\it', s)
        return s




def getargs():
    """Parse command line argument and return the result as a dict object."""
    import argparse
    parser = argparse.ArgumentParser(
        prog='texbenri.bbl',
        description='Make bbl file as simple as possible',
        )
    parser.add_argument(
        'fname',
        help='target bbl file name',
        )
    parser.add_argument(
        '-s', '--style',
        help='bst file name (acsrev|aip) (default: acsrev)',
        dest='style',
        default='acsrev',
        )
    keys = vars(parser.parse_args())
    return keys


def main():
    """ """
    keys = getargs()
    with open(keys['fname']) as f:
        bbl = f.read()
    cc = ConverterCollection(bbl)
    s = getattr(cc, 'conv_'+keys['style'])()
    print(s)


if __name__ == '__main__':
    main()
