import numpy
# from numpy.core.numeric import Infinity
from sympy import *
from sympy.abc import x, y, a, b, c, d, e, f, g, h
from topicsVariable import *
import numpy as np
import scipy as sy
from random import randint
import math
import time


r1 = symbols('r1')
pl = Symbol('+')
pm = Symbol('±', real=True)


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


def genExc(p, q, r=0, *args):
    x = randint(p, q)
    while x == r or x in args:
        x = randint(p, q)
    return x


def gen(p, q):
    x = randint(p, q)
    return x


def generatePolynomial(int_root, rat_root):
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


def operations(operation, level):

    op = {'add': '$+$',
          'minus': '$-$',
          'multiply': '$*$',
          'divide': '$\div$'
          }
    expr = []
    deg = gen_deg(operation, level)

    for each in deg:
        expr.append(genPoly(each))

    polEq = inline_wrapper(
        expr[0])+op[operation]+inline_wrapper(expr[1])
    # polEq = '('+str(prod[0])+')'+op[operation]+'('+str(prod[1])+')'
    if operation == 'divide':
        quo, rem = polys.polytools.div(expr[0], expr[1])
        # expanded = quo_rem[0] + (quo_rem[1]/expr[1])
        constant_term = quo.subs({x: 0})
        deg_ans = degree(quo, gen=0)
        lead_coef = polys.polytools.LC(quo)
        leading_term = polys.polytools.LT(quo)
        # expanded = str(quo_rem[0]) + remainder
        properties = {'Quotient:   ': quo,
                      'Leading Term:   ': leading_term,
                      'Degree:  ': deg_ans,
                      'Leading Coefficient:   ': lead_coef,
                      'Constant Term:   ': constant_term,
                      'Remainder: ': rem
                      }

    else:
        if operation == 'multiply':
            expanded = expand(expr[0]*expr[1])
        elif operation == 'add':
            expanded = expand(expr[0]+expr[1])
        elif operation == 'minus':
            expanded = expand(expr[0]-expr[1])
        # print(expanded)
        constant_term = expanded.subs({x: 0})
        deg_ans = degree(expanded, gen=0)
        lead_coef = polys.polytools.LC(expanded)
        leading_term = polys.polytools.LT(expanded)
        # expanded = latex(expanded, mode='inline')

        properties = {'Simpliest Form:   ': expanded,
                      'Leading Term:   ': leading_term,
                      'Degree:  ': deg_ans,
                      'Leading Coefficient:   ': lead_coef,
                      'Constant Term:   ': constant_term

                      }
    props = list(properties.keys())

    anskeys = [x + latex(properties[x], mode='inline',
                         fold_short_frac=False) for x in props]

    return (polEq, props, anskeys)


# a, b, c = operations('add', 'easy')


def diffSquare(level):
    r = 1 if level == 'easy' else y
    p = genExc(-3, 1)*x
    q = genExc(-1, 2)
    p *= p
    q *= q
    return (p, -q)


def sumDiffCubes(level):
    r = 1 if level == 'easy' else y
    p = genExc(-3, 1)*x
    q = genExc(-1, 3)
    p *= p*p
    q *= q*q

    return (p, q)


def by_grouping(level):
    if level == 'easy':
        p = genExc(-1, 1)
        q = genExc(-1, 1)

    elif level == 'hard':
        p = genExc(-3, 3)
        q = genExc(-3, 4)

    factors = (a*x+b)*(c*x+d)
    factors = factors.subs(
        {a: p, b: genExc(-9, 4), c: q, d: genExc(-2, 9)})
    polEq = expand(factors)
    factored_form = factor(factors)
    return (polEq, factored_form)


def factoring(typeIs, level):

    if typeIs == Factoring_By_Grouping:
        polEq, factored_form = by_grouping(level)
        properties = {'Factored Form: ': factored_form}
    elif typeIs == Factoring_using_Mixed_Methods:
        combination = randint(1, 6)
        if combination == 1:
            p, q = diffSquare(level)
            r, s = diffSquare(level)
            polEq = expand((p+q)*(r+s))
        elif combination == 2:
            p, q = sumDiffCubes(level)
            r, s = sumDiffCubes(level)
            polEq = expand((p+q)*(r+s))
        elif combination == 3:
            p, q = sumDiffCubes(level)
            r, s = sumDiffCubes(level)
            polEq = expand((p-q)*(r-s))
        elif combination == 4:
            p, q = sumDiffCubes(level)
            r, s = sumDiffCubes(level)
            polEq = expand((p-q)*(r+s))
        elif combination == 5:
            p, q = diffSquare(level)
            r, s = sumDiffCubes(level)
            polEq = expand((p+q)*(r+s))
        elif combination == 6:
            p, q = diffSquare(level)
            r, s = sumDiffCubes(level)
            polEq = expand((p+q)*(r-s))
        factored_form = factor(polEq)
        properties = {r'Factored Form: \\': factored_form}
    polEq = latex(polEq, mode='inline')

    props = list(properties.keys())
    # anskeys = ''
    anskeys = [x + latex(properties[x], mode='inline',
                         fold_short_frac=False) for x in props]

    return (polEq, props, anskeys)


def evaluatePoly(topic, level):
    # expr1 = genPoly(randint(3,6))
    # expr2 = genPoly(1) if level == 'easy' else genPoly(2)
    # quo_rem = polys.polytools.div(expr1, expr2)

    # remainder = '' if (quo_rem[1]/expr[1]
    #                     ) == 0 else '+'+str(quo_rem[1]/expr[1])
    # expanded = str(quo_rem[0]) + remainder
    # properties = {'Quotient:   ': quo_rem[0],
    #                 'Leading Term:   ': leading_term,
    #                 'Degree:  ': deg_ans,
    #                 'Leading Coefficient:   ': lead_coef,
    #                 'Constant Term:   ': constant_term,
    #                 'Remainder: ': quo_rem[1]
    #                 }

    polynomial = genPoly(
        randint(2, 5))

    factor1 = genPoly(1, True)

    divisor = genPoly(1, True)
    r, = solve(divisor, x)
    value = genExc(-7, 7) if level == 'easy' else r
    evaluatedValue = polynomial.subs({x: value})
    if topic == Evaluating_Polynomial:
        properties = {'Evaluated Value: ': evaluatedValue}
        polEq = latex(polynomial, mode='inline') + '   at $x=$ ' + \
            latex(value, mode='inline', fold_short_frac=False)
    elif topic == Remainder_Theorem:
        properties = {'Remainder: ': evaluatedValue}
        polEq = '('+latex(polynomial, mode='inline')+')' + ' $\div$ ' + \
            '('+latex(divisor, mode='inline', fold_short_frac=False)+')'

    elif topic == Factor_Theorem:
        isFactor = bool(randint(0, 1))
        rem = polys.polytools.div(polynomial, divisor)
        if isFactor:
            while rem[1] != 0:
                divisor = genPoly(1, True)
                rem = polys.polytools.div(polynomial, divisor)
        else:
            while rem[1] == 0:
                divisor = genPoly(1, True)
                rem = polys.polytools.div(polynomial, divisor)
        answer = 'Factor' if isFactor else r'Not a Factor'
        properties = {'Answer: ': answer}
        polEq = '('+latex(polynomial, mode='inline')+')' + ' $\div$ ' + \
            '('+latex(divisor, mode='inline', fold_short_frac=False)+')'
    props = list(properties.keys())
    anskeys = propsLatex(properties)

    # polynomial = genPoly(
    #     randint(2, 5))

    # p = genExc(-2, 3)
    # q = genExc(-5, 5)
    # r = a/b
    # r = r.subs({a: p, b: q})
    # value = genExc(-7, 7) if level == 'easy' else genPoly(1)
    # print(value)
    # evaluatedValue = polynomial.subs({x: value})
    # properties = {'Evaluated Value: ': evaluatedValue}
    # polEq = latex(polynomial, mode='inline') + '   at $x=$ ' + \
    #     latex(value, mode='inline', fold_short_frac=False)

    return (polEq, props, anskeys)


def fta_drs_rrt():

    factored_form, gen_form, rationalRoots, degree = gen_polynomial()

    properties = {'Fundamental Theorem of Algebra:  ': 'Atmost ' + str(degree),
                  "Descartes' Rule of Sign:   ": '',
                  'Rational Root Theorem:   ': '',
                  'Actual Roots:     ': rationalRoots
                  }

    prop_keys = properties.keys()

    for each in prop_keys:
        properties[each] = to_latex_wrapper(properties[each], 4)

    props = [x + str(properties[x]) for x in prop_keys]

    return (gen_form, properties, props)


def polEndBehavior(degree, lead_coef):

    fxGoesTo = r'$f(x) \rightarrow \hspace{0.5em}$'
    infAsXGoestoNegInfFxgoesto = r'$\infty \hspace{0.5em} as \hspace{0.5em} x \rightarrow - \infty \\ f(x) \rightarrow$'
    asXgoestoInf = r'$\infty \hspace{0.5em} as \hspace{0.5em} x \rightarrow \infty \\$'

    if lead_coef > 0 and degree % 2 == 0:
        endBehavior = fxGoesTo + infAsXGoestoNegInfFxgoesto + asXgoestoInf
    elif lead_coef > 0 and degree % 2 == 1:
        endBehavior = fxGoesTo + '$-$' + infAsXGoestoNegInfFxgoesto + asXgoestoInf
    elif lead_coef < 0 and degree % 2 == 0:
        endBehavior = fxGoesTo + '$-$' + infAsXGoestoNegInfFxgoesto + '$-$' + asXgoestoInf
    elif lead_coef < 0 and degree % 2 == 1:
        endBehavior = fxGoesTo + infAsXGoestoNegInfFxgoesto + '$-$' + asXgoestoInf

    return endBehavior


def RRTandGraphing(level, subTopic):

    roots = [gen(3, 4), 0] if level == 'easy' else [gen(3, 3), gen(1, 2)]

    # factored_form, gen_form, rationalRoots, degree = gen_polynomial()
    factored_form, gen_form, rationalRoots, degree = generatePolynomial(
        roots[0], roots[1])
    rationalRoots = [str(i) if rationalRoots.count(i) == 1 else str(i) + ' mul. ' + str(rationalRoots.count(i))
                     for i in rationalRoots]
    rationalRoots = list(dict.fromkeys(rationalRoots))
    rationalRoots = ', '.join(rationalRoots)
    properties = {'FTA:  ': 'Atmost ' + str(degree),
                  'Factored form:   ': factored_form,
                  'Actual roots:   ': rationalRoots

                  }

    if subTopic == Graphing_Polynomial:
        lead_coef = polys.polytools.LC(gen_form)
        endbehavior = polEndBehavior(degree, lead_coef)

        properties[r'End Behavior:\\ \\ \\ '] = endbehavior
        properties[r'Graph:' + spaces(13)] = ''

    polEq = '$f(x) =$'+' '+latex(gen_form, mode='inline')
    # polEq = latex(gen_form, mode='inline', fold_short_frac=False)
    props = list(properties.keys())
    anskeys = propsLatex(properties)

    return (polEq, props, anskeys)


def bounds(level):

    roots = [gen(4, 6), 0] if level == 'easy' else [gen(3, 4), gen(1, 3)]
    # factored_form, gen_form, rationalRoots, degree = gen_polynomial()
    factored_form, gen_form, rationalRoots, degree = generatePolynomial(
        roots[0], roots[1])
    # print(rationalRoots)

    bound_random = randint(1, 3)
    maximum = math.ceil(max(rationalRoots))
    minimum = math.floor(min(rationalRoots))
    # print(gen_form)
    if bound_random == 1:

        bound = 'Upper'
        print(bound)
        k = genExc(maximum + 1, maximum + 1)
        quotient, rem = polys.polytools.div(gen_form, x - k)
        coefficients = Poly(quotient).all_coeffs()
        coefficients.append(rem)
        while all(i >= 0 for i in coefficients) == False and all(i < 0 for i in coefficients) == False:
            k += 1
            quotient, rem = polys.polytools.div(gen_form, x - k)
            coefficients = Poly(quotient).all_coeffs()
            coefficients.append(rem)
            # print(k, quotient)
            # print(rationalRoots)
            # print(coefficients)
            time.sleep(2)
        # print(coefficients)

    elif bound_random == 2:

        bound = 'Lower'
        print(bound)
        k = genExc(minimum - 1, minimum - 1)
        quotient, rem = polys.polytools.div(gen_form, x - k)
        coefficients = Poly(quotient).all_coeffs()
        coefficients.append(rem)
        temp = numpy.all(numpy.abs(numpy.diff(numpy.sign(coefficients))) == 2)

        # print(temp)
        while temp == False:
            k -= 1
            # print(k)
            quotient, rem = polys.polytools.div(gen_form, x - k)
            coefficients = Poly(quotient).all_coeffs()
            coefficients.append(rem)
            temp = numpy.all(
                numpy.abs(numpy.diff(numpy.sign(coefficients))) == 2)

            # print('new', temp)
            # print(rationalRoots)
            # print(k, coefficients)
            time.sleep(2)
        # print(coefficients)
        # print(coefficients)

    elif bound_random == 3:

        bound = 'Neither'
        print(bound)
        rangeOfRoots = maximum - minimum
        while rangeOfRoots <= 1:
            factored_form, gen_form, rationalRoots, degree = generatePolynomial(
                roots[0], roots[1])

        k = genExc(minimum+1, maximum-1)
        quotient, rem = polys.polytools.div(gen_form, x + k)
        coefficients = Poly(quotient).all_coeffs()
        coefficients.append(rem)
        temp = numpy.all(numpy.abs(numpy.diff(numpy.sign(coefficients))) == 2) or all(
            i >= 0 for i in coefficients) or all(i < 0 for i in coefficients)
        while temp:
            k = genExc(minimum+1, maximum-1)

            quotient, rem = polys.polytools.div(gen_form, x + k)
            coefficients = Poly(quotient).all_coeffs()
            coefficients.append(rem)
            temp = numpy.all(numpy.abs(numpy.diff(numpy.sign(coefficients))) == 2) or all(
                i >= 0 for i in coefficients) or all(i < 0 for i in coefficients)
            time.sleep(2)


    properties = {'Bound:  ': bound

                  }
    polEq = '$f(x)$'+' = ' + latex(gen_form, mode='inline') + '    $k =$ ' + \
            latex(k, mode='inline', fold_short_frac=False)
    # polEq = 'y = '+latex(gen_form, mode='inline')
    # polEq = latex(gen_form, mode='inline', fold_short_frac=False)
    props = list(properties.keys())
    anskeys = propsLatex(properties)

    return (polEq, props, anskeys)


def pol_ineq(level):
    roots = [gen(3, 5), 0] if level == 'easy' else [gen(4, 4), gen(1, 3)]

    # factored_form, gen_form, rationalRoots, degree = gen_polynomial()
    factored_form, gen_form, rationalRoots, degree = generatePolynomial(
        roots[0], roots[1])
    # rationalRoots = [str(i) if rationalRoots.count(i) == 1 else str(i) + ' mul. ' + str(rationalRoots.count(i))
    #                  for i in rationalRoots]
    # rationalRoots = list(dict.fromkeys(rationalRoots))
    # rationalRoots = ', '.join(rationalRoots)
    case = gen(1, 4)
    if case == 1:
        solution_set = solveset(gen_form < 0, x, S.Reals)
        relation = '$< 0$'
    elif case == 2:
        solution_set = solveset(gen_form <= 0, x, S.Reals)
        relation = '$\leq 0$'
    elif case == 3:
        solution_set = solveset(gen_form > 0, x, S.Reals)
        relation = '$> 0$'
    elif case == 4:
        solution_set = solveset(gen_form >= 0, x, S.Reals)
        relation = '$\geq 0$'

    properties = {'Solution Set:  ': solution_set
                  }

    equation = factored_form  # #if level == 'hard' else factored_form

    polEq = latex(equation, mode='inline') + " " + relation
    # polEq = latex(gen_form, mode='inline', fold_short_frac=False)
    props = list(properties.keys())
    anskeys = propsLatex(properties)

    return (polEq, props, anskeys)


def simplify_interval_notation(level):
    # level = 2 if level == 'easy' else 3
    if level == 'easy':
        cases = randint(1, 11)
        if cases == 1:
            given = [Interval(gen(-10, -7), gen(5, 8)),
                     Interval(gen(-6, -1), gen(2, 4))]
        elif cases == 2:
            given = [Interval(gen(-10, -1), gen(0, 7)),
                     Interval(gen(-8, -3), gen(-1, 6))]
        elif cases == 3:
            given = [Interval(-oo, gen(3, 7)),
                     Interval.Lopen(gen(-4, 3), gen(9, 12))]
        elif cases == 4:
            given = [Interval(-oo, gen(0, 7)), Interval(gen(-8, -3), oo)]
        elif cases == 5:
            given = [Interval.Ropen(-oo, gen(2, 4)),
                     Interval.Lopen(gen(-3, 7), oo)]
        elif cases == 6:
            given = [Interval.Ropen(gen(-6, -1), gen(2, 4)),
                     Interval(gen(-4, 3), oo)]
        elif cases == 7:
            given = [Interval.Ropen(gen(-10, -1), gen(0, 7)),
                     Interval.Ropen(gen(-8, -3), gen(-1, 6))]
        elif cases == 8:
            given = [Interval.Lopen(gen(-6, -1), gen(2, 4)),
                     Interval.Lopen(gen(-8, -3), gen(-1, 6))]
        elif cases == 9:
            given = [Interval.Ropen(-oo, gen(2, 4)),
                     Interval(gen(-8, -3), gen(-1, 6))]
        elif cases == 10:
            given = [Interval(-oo, gen(0, 7)), Interval.Lopen(gen(-8, -3), oo)]
        elif cases == 11:
            given = [Interval.Ropen(-oo, gen(2, 4)),
                     Interval.Lopen(gen(-5, 7), oo)]

        solution_set = Union(given[0], given[1])
        polEq = latex(given[0], mode='inline') + \
            '$\cup$' + latex(given[1], mode='inline')

    elif level == 'hard':
        cases = randint(1, 2)
        if cases == 1:
            given = [Interval.Ropen(-oo, gen(2, 4)),
                     Interval(gen(1, 7), gen(9, 12)), Interval(gen(5, 7), oo)]
        elif cases == 2:
            given = [Interval(-oo, gen(2, 4)),
                     Interval.Ropen(gen(1, 7), gen(9, 12)), Interval.Lopen(gen(5, 7), oo)]
        elif cases == 2:
            given = [Interval.Ropen(-oo, gen(2, 4)),
                     Interval.Lopen(gen(1, 7), gen(9, 12)), Interval(gen(5, 7), oo)]
        elif cases == 2:
            given = [Interval(-oo, gen(2, 4)),
                     Interval(gen(1, 7), gen(9, 12)), Interval(gen(5, 7), oo)]

        solution_set = Union(given[0], given[1], given[2])

        polEq = latex(given[0], mode='inline') + '$\cup$' + latex(given[1],
                                                                  mode='inline') + '$\cup$' + latex(given[2], mode='inline')

    properties = {'Simpliest Form:  ': solution_set
                  }

    # polEq = latex(gen_form, mode='inline', fold_short_frac=False)
    props = list(properties.keys())
    anskeys = propsLatex(properties)

    return (polEq, props, anskeys)


def main(subTopic, items):
    equations = []
    ans_key = []
    given_question_ans = []
    for i in range(items):
        if subTopic == Identifying_Polynomial:
            pass

        elif subTopic == Adding_and_Subtracting_Polynomial:
            operation = 'add' if i <= i//2 else 'minus'
            level = 'easy'
            given, question, ans = operations(operation, level)
            item = [given, question, ans]
            given_question_ans.append(item)

        elif subTopic == Multiplying_Polynomial:
            level = 'easy'
            given, question, ans = operations('multiply', level)
            item = [given, question, ans]
            given_question_ans.append(item)

        elif subTopic == Dividing_Polynomial:
            level = 'easy' if i <= i//2 else 'hard'
            given, question, ans = operations('divide', level)
            item = [given, question, ans]
            given_question_ans.append(item)

        elif subTopic == Factoring_By_Grouping or subTopic == Factoring_using_Mixed_Methods:
            level = 'easy' if i < items//2 else 'hard'
            given, question, ans = factoring(subTopic, level)
            item = [given, question, ans]
            given_question_ans.append(item)

        elif subTopic == Evaluating_Polynomial or subTopic == Remainder_Theorem or subTopic == Factor_Theorem:
            if subTopic == Evaluating_Polynomial:
                level = 'easy' if i < items - 2 else 'hard'
            else:
                level = 'easy' if i < items//2 else 'hard'
            # print(level)
            given, question, ans = evaluatePoly(subTopic, level)
            item = [given, question, ans]
            given_question_ans.append(item)

        elif subTopic == Rational_Root_Theorem or subTopic == Graphing_Polynomial:
            level = 'easy' if i < items//2 else 'hard'
            given, question, ans = RRTandGraphing(level, subTopic)
            item = [given, question, ans]
            given_question_ans.append(item)

        elif subTopic == Upper_Lower_Bounds:
            level = 'easy' if i < items//2 else 'hard'
            given, question, ans = bounds(level)
            item = [given, question, ans]
            given_question_ans.append(item)

        elif subTopic == Problem_Solving:
            level = 'easy' if i < items//2 else 'hard'
            given, question, ans = bounds(level)
            item = [given, question, ans]
            given_question_ans.append(item)

        elif subTopic == Polynomial_Inequality:
            level = 'easy' if i % 8 != 3 or i % 8 != 7 else 'hard'
            given, question, ans = pol_ineq(level)
            item = [given, question, ans]
            given_question_ans.append(item)

        elif subTopic == Simplifying_Interval_Notation:
            level = 'easy' if i < (2*items)//3 else 'hard'
            given, question, ans = simplify_interval_notation(level)
            item = [given, question, ans]
            given_question_ans.append(item)

        # elif subTopic == Graphing_Polynomial:
        #     level = 'easy' if i < items//2 else 'hard'
        #     given, question, ans = graphing(level)
        #     item = [given, question, ans]
        #     given_question_ans.append(item)
        # print(given,question)
        equations.append((given, question))
        ans_key.append((given, ans))

    # print(equations)
    # print(ans_key)

    return (equations, ans_key)
