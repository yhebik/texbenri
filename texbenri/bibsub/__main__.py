#!/usr/bin/env python3
import sys
import os
import re

__all__ = ['load_refdict', 'bibsub']


_DEFAULT_DICT = os.path.join(os.path.dirname(__file__), 'refdict.dat')


def load_refdict(dictpaths):
    """Load "refdict.txt" and transform it into a dict object."""
    refdict = {}
    for fname in dictpaths:
        with open(fname) as f:
            s = f.read()
        for l in s.splitlines():
            if not re.match('^\s*$', l):
                key, value = re.split('\s?=\s?', l)
                key = re.sub('^\s+', '', key)
                refdict[key] = value
    return refdict


def bibsub(fname, refdict, silent):
    """Substitute full journal names in BibTeX file into their abbreb.."""
    fmtbase = '\{{\s*(the )?{0}\s*\}}'
    with open(fname) as f:
        substituted = f.read()
    for key, value in refdict.items():
        expr = fmtbase.format(key)
        if re.search(expr, substituted, flags=re.I):
            if not silent:
                print('{0} -> {1}'.format(key, value))
            substituted = re.sub(
                expr, '{{{0}}}'.format(value), substituted, flags=re.I)
    return substituted


def getargs():
    """Parse command line argument and return the result as a dict object."""
    import argparse
    descrep = 'Substitute full journal names in bib file into their abbreb..'
    parser = argparse.ArgumentParser(
        prog='texbenri.bibsub',
        description=descrep,
        )
    parser.add_argument(
        'fname',
        help='target bib file name',
        )
    parser.add_argument(
        '-d', '--dict',
        help='"," separated extra list of dict files',
        default=None,
        )
    parser.add_argument(
        '-n', '--dry-run',
        help='dry-run mode: do nothing actually',
        default=False,
        dest='dryrun',
        action='store_true',
        )
    parser.add_argument(
        '-s', '--silent',
        help='invoke silent mode',
        default=False,
        action='store_true',
        )
    keys = vars(parser.parse_args())
    return keys


def main():
    """ """
    keys = getargs()
    # Load dictionaries.
    dictpaths = keys['dict'].split(',') if keys['dict'] else []
    dictpaths.append(_DEFAULT_DICT)
    refdict = load_refdict(dictpaths)
    # Excecute substitution.
    substituted = bibsub(keys['fname'], refdict, keys['silent'])
    if not keys['dryrun']:
        with open(keys['fname']+'.tmp', 'w') as f:
            f.write(substituted)
        os.rename(keys['fname']+'.tmp', keys['fname'])


if __name__ == '__main__':
    main()
