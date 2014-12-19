texbenri
========
TeX benri (便利 --- useful) command collection as a Python3 package.

## TEST
```sh
$ cd {texbenri's project root}
$ python3 -m unittest
```

## INSTALL
```sh
$ cd {texbenri's project root}
$ sudo python3 setup.py install
```

## USAGE
Because this is a python package, you need to put `python3 -m texbenri`
as a prefix. For example,
```sh
$ python3 -m texbenri.bundle ...
```

## COMMANDS
### `bundle`
```
usage: texbenri.bundle [-h] [-d PREFIX] [-f FMT] [-s] fname

Reform TeX file and figures to be in a single foldfer

positional arguments:
  fname                 target TeX file name

optional arguments:
  -h, --help            show this help message and exit
  -d PREFIX, --prefix PREFIX
                        prefix (default: bundle)
  -f FMT, --format FMT  python style format (default: Fig{0:d}{1})
  -s, --silent          invoke silent mode
```
### `bbl`
```
usage: texbenri.bbl [-h] [-s STYLE] fname

Make bbl file as simple as possible

positional arguments:
  fname                 target bbl file name

optional arguments:
  -h, --help            show this help message and exit
  -s STYLE, --style STYLE
                        bst file name (acsrev|aip) (default: acsrev)
```
### `bibsub`
```
usage: texbenri.bibsub [-h] [-d DICT] [-n] [-s] fname

Substitute full journal names in bib file into their abbrebiations.

positional arguments:
  fname                 target bib file name

optional arguments:
  -h, --help            show this help message and exit
  -d DICT, --dict DICT  "," separated extra list of dict files
  -n, --dry-run         dry-run mode: do nothing actually
  -s, --silent          invoke silent mode
```
