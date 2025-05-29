import numpy
from sympy import *
from sympy.abc import x, y, a, b, c, d, e, f, g, h

from random import randint

r1 = symbols('r1')
pl = Symbol('+')
pm = Symbol('±', real=True)

def genExc(p, q, r=0, *args):
    # Generate any number except zero and *args
    x = randint(p, q)
    while x == r or x in args:
        x = randint(p, q)
    return x


def gen(p, q):
    x = randint(p, q)
    return x


def genPolSequence(deg):
    polynom = a*x+b
    polynom = polynom.subs({a: 3, b: (-1)*genExc(1, 3)})
    for i in range(deg-1):
        polynom *= (a*x+b)
        polynom = polynom.subs({a: genExc(1,2), b: (-1)**i*genExc(1, 3)})
    
    polynom = expand(polynom)

    return polynom


def generatePolynomial(int_root, rat_root):
    # Generates a polynomial with int and rational roots.
    degree = int_root+rat_root
    polynom = a*x+b
    if rat_root == 0:
        r = genExc(-1, 1,)
    elif int_root == 0:
        r = genExc(-2, 2,)
    else:
        r = genExc(-1, 1,)
    polynom = polynom.subs({a: r, b: genExc(-1, 2)})
    for i in range(int_root-1):
        polynom *= (a*x+b)
        polynom = polynom.subs({a: 1, b: genExc(-1, 3)})

    for j in range(rat_root):
        polynom *= (a*x+b)
        polynom = polynom.subs({a: genExc(-1, 2), b: genExc(-1, 3)})

    polynom = expand(polynom)
    factoredForm = factor(polynom)
    rationalRoots = Poly(polynom).all_roots(multiple=True)
    return (factoredForm, polynom, rationalRoots, degree)


# print(generatePolynomial(0, 2))

# possible for fractional roots


def genPoly(no_fact, frac_roots=False):
    if frac_roots == False:
        p = genExc(-1, 2)
        q = genExc(-2, 1)
    else:
        p = genExc(-3, 2, 0, 1)
        q = genExc(-3, 2, 0, 1)
    polynom = a*x+b
    polynom = polynom.subs({a: p, b: q})
    for i in range(no_fact-1):
        polynom *= (a*x+b)
        polynom = polynom.subs({a: genExc(-1, 2), b: genExc(-1, 3)})
        polynom = expand(polynom)
    return polynom

# integer roots only


def gen_polynomial():

    degree = gen(3, 5)
    rationalRoots = [gen(-3, 5) for i in range(degree)]
    factoredForm = (x-r1)
    factoredForm = factoredForm.subs({r1: rationalRoots[0]})
    for i in range(degree-1):
        factoredForm *= (x-r1)
        factoredForm = factoredForm.subs({r1: rationalRoots[i+1]})

    gen_form = expand(factoredForm)

    return (factoredForm, gen_form, rationalRoots, degree)


def gen_deg(operation, level):
    if operation == 'multiply':
        deg = [2, gen(1, 2)]
    elif operation == 'add' or operation == 'minus':
        deg = [gen(2, 3), gen(2, 3)]
    else:
        if level == 'easy':
            deg = [gen(3, 4), 1]
        elif level == 'hard':
            deg = [gen(3, 5), 2]
    return deg
