# Example markdown doc 

## Python generated table

Content :

```python
input = range(8)
table = [ list(input), [x*3 for x in input] ]

print(make_table(table))
```

Result :

```python
#!exec
input = range(8)
table = [ list(input), [x*3 for x in input] ]

print(make_table(table))
```

## Ascii drawing to svgbob

Content :

```
+---+    +---+
| a |--->| b |
+---+    +---+
```

Result:

```svgbob
+---+    +---+
| a |--->| b |
+---+    +---+
```
