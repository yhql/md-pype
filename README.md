# md-pype

Set of pandocfilters to extend markdown in a static programmed way.

## Contains

`execpy.py` : python codeblocks beginning with `#!exec` are executed and if anything is printed inside the block, redirect it to be parsed by pandoc.
(will) provide some convenience functions to make markdown tables, ...

## Requirements

`pandoc`
`python 3.6`, with `pandocfilters`

## Use

`pandoc file -o file.html --filter=./execpy.py

## Example

See testdoc.md and the result in testdoc.html
