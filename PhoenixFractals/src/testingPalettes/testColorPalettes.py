from colour import Color
import sys
from HTML_Palette import stylesheet, html_palette


def print_palette(name, colors):
    """Print a color palette to STDERR"""
    title = f"{name} ({len(colors)} colors {colors[0]}->{colors[-1]})"
    print(title, file=sys.stderr)
    print('=' * len(title), file=sys.stderr)
    for i, c in enumerate(colors):
        print(f"{i:3} {c}", file=sys.stderr)
    print(file=sys.stderr)


# The color palette used by the Phoenix Fractal in Assignment 5.0
hardcoded = [
        '#ffe4b5', '#ffe5b2', '#ffe6af', '#ffe8ac', '#ffe9a9', '#ffeba7',
        '#ffeda4', '#ffefa1', '#fff19e', '#fff49b', '#fff698', '#fff995',
        '#fffc92', '#ffff90', '#fcff8d', '#f9ff8a', '#f5ff87', '#f1ff84',
        '#eeff81', '#e9ff7e', '#e5ff7b', '#e1ff78', '#ddff76', '#d8ff73',
        '#d3ff70', '#ceff6d', '#c9ff6a', '#c4ff67', '#beff64', '#b9ff61',
        '#b3ff5f', '#adff5c', '#a7ff59', '#a0ff56', '#9aff53', '#93ff50',
        '#8dff4d', '#86ff4a', '#7fff47', '#78ff45', '#70ff42', '#69ff3f',
        '#61ff3c', '#59ff39', '#51ff36', '#49ff33', '#40ff30', '#38ff2e',
        '#2fff2b', '#28ff29', '#25ff2c', '#22ff30', '#1fff33', '#1cff37',
        '#19ff3b', '#16ff3f', '#14ff43', '#11ff48', '#0eff4c', '#0bff51',
        '#08ff56', '#05ff5b', '#02ff60', '#00fe65', '#00fc6b', '#00f971',
        '#00f677', '#00f37c', '#00f081', '#00ed86', '#00ea8b', '#00e790',
        '#00e595', '#00e299', '#00df9d', '#00dca2', '#00d9a5', '#00d6a9',
        '#00d3ad', '#00d0b0', '#00cdb4', '#00cbb7', '#00c8ba', '#00c5bd',
        '#00c2bf', '#00bcbf', '#00b4bc', '#00acb9', '#00a4b6', '#009db4',
        '#0095b1', '#008eae', '#0087ab', '#0080a8', '#0079a5', '#0072a2',
        '#006c9f', '#00669c', '#005f9a', '#005997', '#005494', '#004e91',
        '#00488e', '#00438b', '#003e88', '#003985', '#003483', '#002f80',
        '#002b7d', '#00267a', '#002277'
        ]

# Uncomment to print the hardcoded palette on STDERR
print_palette("hardcoded", hardcoded)

# Uncomment to create an HTML file to visualize the palette
stylesheet()  # output the CSS only once
html_palette("hardcoded", hardcoded)  # call this function as desired


# Use a for loop and colour.Color's `.range_to()` method to generate 111 colors
# spanning from `hardcoded[0]` to `hardcoded[-1]`
start = Color(hardcoded[0])
dynamic = []
for c in start.range_to(hardcoded[-1], len(hardcoded)):
    dynamic.append(c.hex_l)


# This `assert` statement proves that `hardcoded` is identical to `dynamic`.
# If they differed the program would crash with an `AssertionError`
assert hardcoded == dynamic, "dynamic colors made with a for loop"
print("`hardcoded` is the same as the palette made with a for loop", file=sys.stderr)


# Python's list comprehesion feature generates the list of colors compactly
dynamic = [ c.hex_l for c in start.range_to(hardcoded[-1], len(hardcoded)) ]
assert hardcoded == dynamic, "dynamic colors made with a list comprehension"
print("`hardcoded` is the same as the palette made in a list comprehension", file=sys.stderr)
html_palette("dynamic", dynamic)


# Recreate this palette in 32 steps
shorter = [ c.hex_l for c in start.range_to(hardcoded[-1], 32) ]
print_palette("shorter", shorter)
html_palette("shorter", shorter)  # Or, output an HTML file to visualize the palette


# Stretch this palette out over 256 colors
longer = [ c.hex_l for c in start.range_to(hardcoded[-1], 256) ]
#print_palette("longer", longer)
html_palette("longer", longer)


# Make the palette take 694 steps instead
# Do you see a problem?
too_long = [ c.hex_l for c in start.range_to(hardcoded[-1], 694) ]
#print_palette("too_long", too_long)
html_palette("too_long", too_long)


# Make a new palette spanning 694 colors around the RGB color cube,
# interspersed with black
# https://en.wikipedia.org/wiki/RGB_color_spaces#/media/File:RGB_Cube_Show_lowgamma_cutout_b.png
red = Color('red')
yel = Color('yellow')
grn = Color('green')
cya = Color('cyan')
blu = Color('blue')
mag = Color('magenta')
blk = Color('black')

really_long  = [ c.hex_l for c in red.range_to(blk, 64) ]
really_long += [ c.hex_l for c in blk.range_to(yel, 64) ][1:]
really_long += [ c.hex_l for c in yel.range_to(blk, 64) ][1:]
really_long += [ c.hex_l for c in blk.range_to(grn, 64) ][1:]
really_long += [ c.hex_l for c in grn.range_to(blk, 64) ][1:]
really_long += [ c.hex_l for c in blk.range_to(cya, 64) ][1:]
really_long += [ c.hex_l for c in cya.range_to(blk, 64) ][1:]
really_long += [ c.hex_l for c in blk.range_to(blu, 64) ][1:]
really_long += [ c.hex_l for c in blu.range_to(blk, 64) ][1:]
really_long += [ c.hex_l for c in blk.range_to(mag, 64) ][1:]
really_long += [ c.hex_l for c in mag.range_to(blk, 64) ][1:]

# print_palette("really_long", really_long)
html_palette("really_long", really_long)


# Vim magic - plz ignore
# :autocmd bufwritepost <buffer> silent !python3 palette.py > palette.html 2>/dev/null

