import numpy
# from numpy.core.numeric import Infinity
from sympy import *
# from sympy.abc import x, y, a, b, c, d, e, f, g, h
# from sympy import divisors #, divisor_count

# import numpy as np
# import scipy as sy
# from random import randint


# r1 = symbols('r1')
# pl = Symbol('+')
# pm = Symbol('±', real=True)


def spaces(no_of_spaces):
    x = r'\\'
    for i in range(no_of_spaces-1):
        x += r' \\'

    return x


def to_latex_wrapper(exprs, no_newline):
    newline = ''
    for i in range(no_newline):
        newline += '\\ '
    expr = latex(exprs)
    expr = '\('+expr+newline+'\)'

    return expr


def inline_wrapper(exprs):
    expr = latex(exprs)
    expr = '$\\left('+expr+'\\right)$'

    return expr


def propsLatex(properties):
    props = list(properties.keys())
    anskey = []
    for x in props:
        if type(properties[x]) == str:
            ans = x + properties[x]
        else:
            ans = x + latex(properties[x],
                            mode='inline', fold_short_frac=False)
        anskey.append(ans)

    return anskey


def pm(p, q):
    x = str(p)
    y = str(q)
    temp = x+'\pm '+y
    return temp



def spaces(no_of_spaces):
    x = r'\\'
    for i in range(no_of_spaces-1):
        x += r' \\'

    return x


def to_latex_wrapper(exprs, no_newline):
    newline = ''
    for i in range(no_newline):
        newline += '\\ '
    expr = latex(exprs)
    expr = '\('+expr+newline+'\)'

    return expr


def inline_wrapper(exprs):
    expr = latex(exprs)
    expr = '$\\left('+expr+'\\right)$'

    return expr


def propsLatex(properties):
    props = list(properties.keys())
    anskey = []
    for x in props:
        if type(properties[x]) == str:
            ans = x + properties[x]
        else:
            ans = x + latex(properties[x],
                            mode='inline', fold_short_frac=False)
        anskey.append(ans)

    return anskey


def pm(p, q):
    x = str(p)
    y = str(q)
    temp = x+'\pm '+y
    return temp

# from random import choices
# population = [1, 2, 3, 4, 5, 6]
# weights = [0.1, 0.05, 0.05, 0.2, 0.4, 0.2]
# choices(population, weights)
