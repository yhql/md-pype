# md-pype

Set of pandocfilters to extend markdown with python execution and command redirection

## Contains

`execpy.py` : main filter that performs :
 - python codeblocks (beginning with `#!exec)` execution and if anything is printed inside the block, redirect it to be parsed by pandoc. (will) provide some convenience functions to make markdown tables, ...
- cobeblocks marked with `svgbob` are parsed by svgbobrus

Only works when outputting html so far.

## Requirements

`pandoc`
`python 3.6`, with `pandocfilters`

## Use

`pandoc file -o file.html --filter=./execpy.py`

## Example

See testdoc.md and the result in testdoc.html
