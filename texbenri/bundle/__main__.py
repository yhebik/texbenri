#!/usr/bin/env python3
import os
import re


__all__ = [
    'parse_graphicspath', 'get_graphics_list',
    'replace_graphics', 'copy_figs', ]


def parse_graphicspath(fname):
    """Parse "\grapchicspath" and return the result as a list object."""
    with open(fname) as f:
        s = f.read()
    l = re.findall('.*graphicspath.*', s)
    graphicspath = ['./']
    if l:
        for i in re.sub('(^.*?{)|(\s*}$)', '', l[-1]).split(','):
            path = re.sub('\s*{|}\s*', '', i)
            if path not in graphicspath:
                graphicspath.append(path)
    return graphicspath


def get_graphics_list(fname):
    """Search for "\includegraphics" and make a list of it."""
    with open(fname) as f:
        s = f.read()
    rawls = re.findall('.*includegraphics.*', s)
    figls = [re.sub('(^.*{)|}\s*$', '', i) for i in rawls]
    ls = [(i, re.sub('(^.*{)|}\s*$', '', i)) for i in rawls]
    ls = tuple(zip(rawls, figls))
    return ls


def replace_graphics(fname, fmt, silent):
    """Replace "\includegraphics" statements."""
    ls = get_graphics_list(fname)
    with open(fname) as f:
        s = f.read()
    for i, l in enumerate(ls):
        string, target = l
        figname = fmt.format(i+1, os.path.splitext(target)[1])
        replaced = string.replace(target, figname)
        s = s.replace(string, replaced)
        if not silent:
            print(target, '->', figname)
    return s


def copy_figs(fname, fmt, prefix):
    """Copy figure files files in a given format in prefix/."""
    import shutil
    graphicspath = parse_graphicspath(fname)
    ls = get_graphics_list(fname)
    for i, l in enumerate(ls):
        target = l[1]
        figname = fmt.format(i+1, os.path.splitext(target)[1])
        for gpath in graphicspath:
            if os.path.isfile(gpath+target):
                shutil.copyfile(gpath+target, prefix+'/'+figname)


def driver(fname, prefix, fmt, silent):
    """Driver routine called from main()."""
    import shutil
    # File check.
    if not os.path.isfile(fname):
        raise FileNotFoundError(fname+' not found')
    # Remove directories recursively and create new one.
    if os.path.isdir(prefix):
        shutil.rmtree(prefix)
    os.mkdir(prefix)
    if not silent:
        print('directory: {0}'.format(prefix))
    # Replace "\includegraphics"  part into the copied file.
    with open(prefix+'/'+fname, 'w') as f:
        f.write(replace_graphics(fname, fmt, silent))
    # Copy files.
    copy_figs(fname, fmt, prefix)


def getargs():
    """Parse command line argument and return the result as a dict object."""
    import argparse
    parser = argparse.ArgumentParser(
        prog='texbenri.bundle',
        description='Reform TeX file and figures to be in a single foldfer',
        )
    parser.add_argument(
        'fname',
        help='target TeX file name',
        )
    parser.add_argument(
        '-d', '--prefix',
        help='prefix (default: bundle)',
        default='bundle',
        )
    parser.add_argument(
        '-f', '--format',
        help='python style format (default: Fig{0:d}{1})',
        dest='fmt',
        default='Fig{0:d}{1}',
        )
    parser.add_argument(
        '-s', '--silent',
        help='invoke silent mode',
        action='store_true',
        default=False,
        )
    keys = vars(parser.parse_args())
    return keys


def main():
    """ """
    keys = getargs()
    args = [keys[i] for i in ('fname', 'prefix', 'fmt', 'silent')]
    driver(*args)


if __name__ == '__main__':
    main()
