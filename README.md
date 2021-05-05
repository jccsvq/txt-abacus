# txt-abacus
Create traditional Chinese/Japanese abacus (soroban/suanpan) text figures.

A very simple Python 3 module to draw/write diagrams of Chinese/Japanese 
abacus of 1:4, 1:5, 2:5 and 3:5 types with a maximum of 26 rods with 
capacity for the upper suspended bead (Kenshu, Xuánzhū 懸珠) in 2:5 mode
 and lower suspended bead in 1:5 mode. These text based figures can be 
 included in a document using a monospaced font. You can use four color
 patterns.
 
 Defines the sw_print function that does the job.

```python
sw_print(str1, nr=13, left=True, atype='2:5', lrb=True)
```
```
    :param str1: list of raw codes
    :type str1: str
    :param nr: number of columns (max 36)
    :type nr: int
    :param left: ``True`` if leftpad is required, ``False`` for rightpad
    :type left: bool
    :param atype: '1:4', '1:5', '2:5' (default), '3:5'
    :type atype: str
    :param lrb: ``True`` to draw left and right borders
    :type lrb: bool
    :param color: 'bw' set beads: black, unset beads: white (default)
                  'bb' set beads: black, unset beads: black
                  'wb' set beads: white, unset beads: black
                  'ww' set beads: white, unset beads: white
    :type color: str
    :returns: ``None``

    :example:

        >>> sw_print('21 22 23 24 25 30 31 32 33 34 35')
        
		  11 12 13 14 15 15 16 17 18 19 20  0  0
		╔═════════════════════════════════════════╗
		║  │  │  │  │  │  │  │  │  │  │  │  ○  ○  ║
		║  │  │  │  │  │  ●  ●  ●  ●  ●  ●  ○  ○  ║
		║  ●  ●  ●  ●  ●  │  │  │  │  │  │  │  │  ║
		║  ●  ●  ●  ●  ●  ●  ●  ●  ●  ●  ●  │  │  ║
		╠═════════════════════════════════════════╣
		║  ●  ●  ●  ●  ●  │  ●  ●  ●  ●  ●  │  │  ║
		║  │  ●  ●  ●  ●  │  │  ●  ●  ●  ●  │  │  ║
		║  │  │  ●  ●  ●  ○  │  │  ●  ●  ●  ○  ○  ║
		║  ○  │  │  ●  ●  ○  ○  │  │  ●  ●  ○  ○  ║
		║  ○  ○  │  │  ●  ○  ○  ○  │  │  ●  ○  ○  ║
		║  ○  ○  ○  │  │  ○  ○  ○  ○  │  │  ○  ○  ║
		║  ○  ○  ○  ○  │  ○  ○  ○  ○  ○  │  ○  ○  ║
		╚═════════════════════════════════════════╝
		   A  B  C  D  E  F  G  H  I  J  K  L  M

```
Try file test-output.txt in your word processor. For best results, you 
should adjust the line spacing.
