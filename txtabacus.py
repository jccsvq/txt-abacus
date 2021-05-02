# -*- coding: utf-8 -*-
"""
Module txtabacus
--------------

Creates a txt model of a 1:4, 1:5, 2:5 or 3:5 abacus with 13 rods.

Created on Sat Mar 23 17:57:02 2019

Modified on Sun May 2 2021

:author: jccsvq

"""

# Data

nr = 13



def leftpad(str1, n=nr):
    """
    leftpad: Returns a list of rod codes of length `n` padding `str1` to the
    left

    :param str1: String of codes to pad to the left
    :type str1: str
    :param n: Number of rods: default nr
    :type n: int
    :returns: List of codes
    :rtype: list

    .. DANGER:: This implementation only works with `n = 13`.
        Don't change the default!

    :example:

        >>> leftpad('0 0 23 12 5')
        [0, 0, 23, 12, 5, 0, 0, 0, 0, 0, 0, 0, 0]
        >>> leftpad('0 0 23 12 5 34 22 12 2 1 0 0 0 0 0 0 0 0 0 0 0')
        [0, 0, 23, 12, 5, 34, 22, 12, 2, 1, 0, 0, 0]

    """

    ali = [int(i) for i in str1.split()]
    l0 = len(ali)
    if l0 <= n:
        ali.extend([0 for i in range(nr - l0)])
    else:
        ali = ali[:nr-l0]
    return ali


def rightpad(str1, n=nr):
    """
    Returns a list of rod codes of length `n`
    padding ``str1`` to the right

    :param str1: String of codes to pad to the right
    :type str1: str
    :param n: Number of rods: default nr
    :type n: int
    :returns: List of codes
    :rtype: list

    .. note::
           This implementation only works with `n = 13`.
           Don't change the default!

    :example:

        >>> rightpad('0 0 23 12 5 34 22 12 2 1')
        [0, 0, 0, 0, 0, 23, 12, 5, 34, 22, 12, 2, 1]
        >>> rightpad('0 0 23 12 5 34 22 12 2 1 0 0 0 0 0 0 0 0 0 0 0')
        [2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    """

    ali = [int(i) for i in str1.split()]
    l0 = len(ali)
    if l0 <= n:
        ali = [0 for i in range(nr - l0)] + ali
    else:
        ali = ali[-nr:]
    return ali


def tenchi_split(list1):
    """
    Splits list of codes

    Splits list of codes in ``str1`` in codes to move
    *Ten* and *Chi* beads in each rod.

    :param str1: string with codes for each rod
    :type str1: str
    :returns: tuple containing lists of codes for *Ten* and
        *Chi* beads in each rod and a string ``name`` with filename for swg.
    :rtype: tuple

    :example:

        >>> a = leftpad('0 0 23 12 5')
        >>> t1, c1, name = tenchi_split(a)
        >>> print(t1)
        [0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        >>> print(c1)
        [0, 0, 3, 2, 5, 0, 0, 0, 0, 0, 0, 0, 0]
        >>> print(name)
        00002312050000000000000000.svg

    """

    ten = []
    chi = []
    name = ''
    for i in range(len(list1)):
        t = list1[i] // 10
        c = list1[i] - 10 * t
        ten.append(t)
        chi.append(c)
        name = name + repr(t) + repr(c)
    name = name + '.svg'
    return ten, chi, name



def sw_print(str1, left=True, atype='2:5'):
    """
    Draws the abacus as ascii art

    This is the main function of this module

    :param str1: list of raw codes
    :type str1: str
    :param left: ``True`` if leftpad is required, ``False`` for rightpad
    :type left: bool
    :param atype: '1:4', '1:5', '2:5', '3:5'
    :type atype: str
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

    """

    l1 = '   A  B  C  D  E  F  G  H  I  J  K  L  M  '
    l0 = '║ ●'
    le1 = '╔═════════════════════════════════════════╗'
    le2 = '╠═════════════════════════════════════════╣'
    le3 = '╚═════════════════════════════════════════╝'

    if atype == '1:4':
        tcod = ['○│', '│●']
        ccod = ['│○○○○', '●│○○○', '●●│○○', '●●●│○', '●●●●│']
        nur = 2
        nlr = 5
    elif atype == '3:5' :
        tcod = ['○○○│', '○○│●', '○│●●', '│●●●']
        ccod = ['││○○○○○', '●││○○○○', '●●││○○○', '●●●││○○', '●●●●││○', '●●●●●││']
        nur = 4
        nlr = 7
    elif atype == '1:5' :
        tcod = ['○│', '│●']
        ccod = ['│○○○○○', '●│○○○○', '●●│○○○', '●●●│○○', '●●●●│○', '●●●●●│']
        nur = 2
        nlr = 6
   
    else :
        tcod = ['○○││', '○││●', '││●●', '│●│●']
        ccod = ['││○○○○○', '●││○○○○', '●●││○○○', '●●●││○○', '●●●●││○', '●●●●●││']
        nur = 4
        nlr = 7
    if left:
        ten, chi, name = tenchi_split(leftpad(str1))
    else:
        ten, chi, name = tenchi_split(rightpad(str1))

    values = ' '
    for i in range(nr):
        values = values + '{:3d}'.format(5 * ten[i] + chi[i])
    print(values)
    print(le1)
    for i in range(nur):
        line = l0[0:2] + ' '
        for j in range(nr):
            line = line + tcod[ten[j]][i] + '  '
        line = line + l0[0]
        print(line)
    print(le2)
    for i in range(nlr):
        line = l0[0:2] + ' '
        for j in range(nr):
            line = line + ccod[chi[j]][i] + '  '
        line = line + l0[0]
        print(line)
    print(le3)
    print(l1)


if __name__ == "__main__":
    """
    Tests
    """

    sw_print('0 1 2 3 4 5 10 11 12 13 14 15 20')
    sw_print('21 22 23 24 25 30 31 32 33 34 35')
    sw_print('21 22 23 24 25 30 31 32 33 34 35', atype = '3:5')
    sw_print('1 2 3', False)
    sw_print('0 1 2 3 4 10 11 12 13 14 ', atype = '1:4')
    sw_print('0 1 2 3 4 5 10 11 12 13 14 15', atype = '1:5')

