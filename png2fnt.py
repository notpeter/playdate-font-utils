#!/usr/bin/env python3

__version__ = '1.0.0'
__copyright__ = "Copyright (c) Peter Tripp 2022"

"""
    png2fnt - Convert PNG sprite sheet to Panic Playdate FNT font file with embeddd PNG.
    Usage: png2fnt 7x11 'abcdefghijklmopqrstuvwxyz' image.png
    URL: https://github.com/notpeter/playdate-font-utils/
"""

import argparse, base64, json, pathlib, re, sys


def png2fnt(filename:pathlib.Path, letters:str, width:int, height:int, tracking:int=1):
    with open(filename, 'rb') as f:
        data = base64.b64encode(f.read())
    letters = ['space' if letter == ' ' else letter for letter in letters]
    print(
        "\n".join([
            # f'--generator={"png2fnt":"1.0.0"},
            f"datalen={len(data)}",
            f"data={data.decode('utf8')}",
            f"width={width}",
            f"height={height}",
            f"",
            f"tracking={tracking}",
            "\n".join([f"{letter}  {width}" for letter in letters]),
        ])
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(f"png2fnt")
    parser.add_argument('dimensions', help='e.g. 9x11 (width x height)')
    parser.add_argument('letters', help='sprite sheet letter order')
    parser.add_argument('filename', help='filename of the png sprite sheet')
    parser.add_argument('-t', help='tracking pixels between characters (default=1)', type=int, default=1)
    parser.add_argument('--version', action='version', version='%(prog)s 2.0')
    args = parser.parse_args()
    dim_re = re.compile(r"(?P<x>\d+)x(?P<y>\d+)")
    if not re.match(dim_re, args.dimensions):
        print(f"Dimensions not as expected: {args.dimensions} (expected format '11x7')", file=sys.stderr)
        sys.exit(1)
    x = re.match(dim_re, args.dimensions).groupdict()['x']
    y = re.match(dim_re, args.dimensions).groupdict()['y']
    png2fnt(filename=args.filename, letters=args.letters, width=x, height=y, tracking=args.t)
