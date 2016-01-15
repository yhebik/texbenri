#!/usr/bin/env python3
import argparse
import subprocess

KEYS = sorted(['bbl', 'bundle', 'bibsub'])


def getargs():
    """Parse command line argument and return the result as a dict object."""
    parser = argparse.ArgumentParser(
        prog='texbenri',
        description='Tex "benri" command collection.',
        )
    parser.add_argument(
        'key',
        help='key: ({0})'.format(', '.join(KEYS)),
        )
    parser.add_argument(
        'args',
        help='args given to the command',
        nargs=argparse.REMAINDER,
        )
    return parser.parse_args()


def main():
    args = getargs()
    cmd = 'python3 -m texbenri.{0}'.format(args.key).split()
    cmd.extend(args.args)
    subprocess.call(cmd)


if __name__ == '__main__':
    main()
