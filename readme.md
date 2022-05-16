# Playdate-Font Utils

## png2fnt.py

Convert PNG sprite sheet to Panic Playdate FNT font file with embeddd base64 encoded PNG.

### Usage

Assuming a png sprite sheet where the glyphs are uniform size (e.g. width=7, height=11)

```shell
python3 png2fnt.py 7x11 'abcdefghijklmopqrstuvwxyz' filename.png
python3 png2fnt.py 7x11 'abcdefghijklmopqrstuvwxyz' filename.png > fontname.fnt
```

## See also:

* https://github.com/jaames/playdate-reverse-engineering/blob/main/formats/fnt.md
