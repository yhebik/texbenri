texbenri
========

## Python 3 module for TeX


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
