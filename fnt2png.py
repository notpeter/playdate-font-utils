#!/usr/bin/env python3

__version__ = '1.0.1'
__copyright__ = "Copyright (c) Peter Tripp 2022"

"""
    fnt2png - Panic Playdate FNT font to PNG sprite.
    Usage: fnt2png input.fnt output.png
    URL: https://github.com/notpeter/playdate-font-utils/
"""

import argparse, base64, json, pathlib, re, sys

def fnt2png(filename:pathlib.Path, out_file:pathlib.Path):
    with open(filename, 'r') as f:
        print(f" IN: {filename}")
        for line in f.readlines():
            if line.startswith('data='):
                png = base64.b64decode(line[5:])
                break
    with open(out_file, 'wb') as o:
        o.write(png)
        print(f"OUT: {out_file}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(f"png2fnt")
    parser.add_argument('input', help='fnt input filename')
    parser.add_argument('output', help='png output filename', nargs='?')
    args = parser.parse_args()
    dim_re = re.compile(r"(?P<x>\d+)x(?P<y>\d+)")
    if args.input.upper().endswith('FNT') or pathlib.Path(args.input).exists():
        fnt2png(filename=args.input, out_file=(args.output or args.input + ".png"))
    else:
        print(f"Error. Input filename ({input}) expected a fnt file.", file=sys.stderr)
        sys.exit(1)