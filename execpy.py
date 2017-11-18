from pandocfilters import toJSONFilter, RawBlock
import subprocess as sp
import sys
from io import StringIO, BytesIO

main_out = StringIO()
pandoc_out = BytesIO()
former_out = sys.stdout

def make_md_row(l):
    return f"|{'|'.join(str(i) for i in l)}|\n"

def make_table(T):
    r = make_md_row(T[0])
    r += make_md_row(['-'*5]*len(T[0]))
    for row in T[1:]:
      r += make_md_row(row)
    return r

def execpy(key, value, format, _):
    if key == 'CodeBlock':
        [[ident, classes, keyvals], code] = value
        if '#!exec' in code:
            sys.stdout = main_out
            exec(code, globals(), locals())
            sys.stdout = pandoc_out
            res = sp.Popen('pandoc', stdout=sp.PIPE, stdin=sp.PIPE)
            res.stdin.write( bytes(main_out.getvalue(),'utf-8'))
            out, err = res.communicate()
            res.terminate()
            sys.stdout = former_out
            return RawBlock('html', out.decode())

        elif 'svgbob' in classes:
            svgb = sp.Popen('svgbob', stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE)
            svgb.stdin.write( bytes(code,'utf-8'))
            out,res = svgb.communicate()
            svgb.terminate()
            return RawBlock('html', out.decode())

if __name__ == "__main__":
    toJSONFilter(execpy)
    main_out.close()
    pandoc_out.close()
