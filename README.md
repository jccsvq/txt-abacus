# txt-abacus
Creates a text model of a traditional 2:5 abacus (soroban/suanpan) with 13 rods.

A very simple Python 3 module for drawing/writing a diagram of a 2:5 abacus with 13 rods with capacity for the suspended bead (Kenshu, Xuánzhū 懸珠) that may be included into a document using a **`monospaced font`**. Defines the function `sw_print` that does the job.

As of May 2021 it can also draw 1:4, 1:5 and 3:5 abacuses.

```python
sw_print(str1, left=True)
```
```
    :param str1: list of raw codes
    :type str1: str
    :param left: ``True`` if leftpad is required, ``False`` for rightpad
    :type left: bool
    :returns: ``None``

    :example:

        >>> sw_print('21 22 23 24 25 30 31 32 33 34 35')
          11 12 13 14 15 15 16 17 18 19 20  0  0
        ╔═════════════════════════════════════════╗
        ║  │  │  │  │  │  │  │  │  │  │  │  ●  ●  ║
        ║  │  │  │  │  │  ●  ●  ●  ●  ●  ●  ●  ●  ║
        ║  ●  ●  ●  ●  ●  │  │  │  │  │  │  │  │  ║
        ║  ●  ●  ●  ●  ●  ●  ●  ●  ●  ●  ●  │  │  ║
        ╠═════════════════════════════════════════╣
        ║  ●  ●  ●  ●  ●  │  ●  ●  ●  ●  ●  │  │  ║
        ║  │  ●  ●  ●  ●  │  │  ●  ●  ●  ●  │  │  ║
        ║  │  │  ●  ●  ●  ●  │  │  ●  ●  ●  ●  ●  ║
        ║  ●  │  │  ●  ●  ●  ●  │  │  ●  ●  ●  ●  ║
        ║  ●  ●  │  │  ●  ●  ●  ●  │  │  ●  ●  ●  ║
        ║  ●  ●  ●  │  │  ●  ●  ●  ●  │  │  ●  ●  ║
        ║  ●  ●  ●  ●  │  ●  ●  ●  ●  ●  │  ●  ●  ║
        ╚═════════════════════════════════════════╝
           A  B  C  D  E  F  G  H  I  J  K  L  M

```
For best results, you should adjust the line spacing in your word processing software.
