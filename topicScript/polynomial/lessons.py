import numpy
import numpy as np
import scipy as sy
import math
import random
from .latexUtils import *
from .polynomialsUtils import *
# from numpy.core.numeric import Infinity
from sympy import *
from sympy.abc import x, y, a, b, c, d, e, f, g, h
from sympy import divisors #, divisor_count
from fractions import Fraction
from topicsVariable import *
from random import randint

from .wordProblem import *

from .goleztheorem import polynomial as  pol


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
    anskeys = [x + latex(properties[x], mode='inline',
                         fold_short_frac=False) for x in props]

    return (polEq, props, anskeys)


def evaluatePoly(topic, level):
    
    polynomial = genPoly(randint(2, 5))
    divisor = genPoly(1, True)
    rem = polys.polytools.div(polynomial, divisor)
    value = genExc(-7, 7)
    if level == 'easy':
        evaluatedValue = polynomial.subs({x: value})
        divisor = x - value  
    else:
        evaluatedValue = rem[1]

    
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
        if isFactor:
            while rem[1] != 0:
                divisor = genPoly(1, True)
                rem = polys.polytools.div(polynomial, divisor)
        else:
            while rem[1] == 0:
                divisor = genPoly(1, True)
                rem = polys.polytools.div(polynomial, divisor)
        answer = 'Factor' if isFactor else r'Not a Factor'
        properties = {  'Remainder: ': rem[1],
                        'Answer: ': answer,
                     }
        polEq = '('+latex(polynomial, mode='inline')+')' + ' $\div$ ' + \
            '('+latex(divisor, mode='inline', fold_short_frac=False)+')'
    props = list(properties.keys())
    anskeys = propsLatex(properties)


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



def unique_combi(p,q):
    # Returns the unique combi of set p / set q
    # Used for rational root theorem
    unique_combinations = []
    
    for i in range(len(p)):
        for j in range(len(q)):
            unique_combinations.append(Rational(p[i]/q[j]))
    unique_combinations = set(unique_combinations)
    # print(unique_combinations)

    return unique_combinations



def RRTandGraphing(level, subTopic):

    roots = [gen(3, 4), 0] if level == 'easy' else [gen(3, 3), gen(1, 2)]

    # factored_form, gen_form, rationalRoots, degree = gen_polynomial()
    factored_form, gen_form, rationalRoots, degree = generatePolynomial(
        roots[0], roots[1])
    rationalRoots = [str(i) if rationalRoots.count(i) == 1 else str(i) + ' mul. ' + str(rationalRoots.count(i))
                     for i in rationalRoots]
    rationalRoots = list(dict.fromkeys(rationalRoots))
    rationalRoots = ', '.join(rationalRoots)
    
    lead_coef = polys.polytools.LC(gen_form)
    constant_term = gen_form.subs({x: 0})
    p = divisors(constant_term)
    q = divisors(lead_coef)
    combi = unique_combi(p,q)

    properties = {'FTA:  ': 'Atmost ' + str(degree),
                  'Possible Roots:   ±':combi,
                  'Factored form:   ': factored_form,
                  'Actual roots:   ': rationalRoots

                  }

    if subTopic == Graphing_Polynomial:
        
        endbehavior = polEndBehavior(degree, lead_coef)

        properties[r'End Behavior:\\ \\ \\ '] = endbehavior
        properties[r'Graph:' + spaces(13)] = ''

    polEq = '$f(x) =$'+' '+latex(gen_form, mode='inline')
    # polEq = latex(gen_form, mode='inline', fold_short_frac=False)
    props = list(properties.keys())
    anskeys = propsLatex(properties)

    return (polEq, props, anskeys)



def BoundTest(coefficients, bound):
    if bound == "lower":
        signList = []
        for i in range((len(coefficients))):
            coef_sign = numpy.sign(coefficients[i])
            signList.append(coef_sign)
        
        lowerBoundTest = numpy.all(numpy.abs(numpy.diff(numpy.sign(coefficients))) == 2)
        # [True  if (signList[each+1]+ signList[each])==0 or\
        #                     (signList[each+1]+ signList[each])==1 else False for each in range(len(signList)-1)]
        bound = False if False in signList else True
    elif bound == 'upper':

        bound = all(i >= 0 for i in coefficients) == False and all(i < 0 for i in coefficients) == False





    return bound


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

        bound = 'upper'
        print(bound)
        k = maximum + 2
        quotient, rem = polys.polytools.div(gen_form, x - k)
        coefficients = Poly(quotient).all_coeffs()
        coefficients.append(rem)
        upperBound = BoundTest(coefficients,bound)
        print(coefficients,'#######',k)
        while upperBound:
            k += 1
            quotient, rem = polys.polytools.div(gen_form, x - k)
            coefficients = Poly(quotient).all_coeffs()
            coefficients.append(rem)
            upperBound = BoundTest(coefficients,bound)
            print(coefficients,'#######',k)
           
    elif bound_random == 2:

        bound = 'lower'
        print(bound)
        k = minimum - 1
        quotient, rem = polys.polytools.div(gen_form, x - k)
        coefficients = Poly(quotient).all_coeffs()
        coefficients.append(rem)
        lowerBound = BoundTest(coefficients,bound)
        print(coefficients,'#######',k)
     
        while lowerBound == False:
            k -= 1
            # print(k)
            quotient, rem = polys.polytools.div(gen_form, x - k)
            coefficients = Poly(quotient).all_coeffs()
            coefficients.append(rem)
            lowerBound = BoundTest(coefficients,bound)

            # print('new', temp)
            # print(rationalRoots)
            print(k, coefficients)
            # print('temp', temp)
            
        # print(coefficients)
        # print(coefficients)

    elif bound_random == 3:

        bound = 'Neither'
        print(bound)

        k = randint(minimum,maximum)
        quotient, rem = polys.polytools.div(gen_form, x + k)
        coefficients = Poly(quotient).all_coeffs()
        coefficients.append(rem)
        lowerBound = BoundTest(coefficients, 'lower') 
        upperBound = BoundTest(coefficients,'upper')
        print(coefficients,'#######', k)
        while not upperBound and  not lowerBound:
            k = randint(minimum,maximum)
            quotient, rem = polys.polytools.div(gen_form, x + k)
            coefficients = Poly(quotient).all_coeffs()
            coefficients.append(rem)
            lowerBound = BoundTest(coefficients,'lower') 
            upperBound = BoundTest(coefficients,'upper')
           
            print(coefficients,'#######', k)
            


    properties = {'Bound:  ': bound,
                  r'Coefficients:\\ ': coefficients

                  }
    polEq = '$f(x)$'+' = ' + latex(gen_form, mode='inline') + '    $k =$ ' + \
            latex(k, mode='inline', fold_short_frac=False)
    # polEq = 'y = '+latex(gen_form, mode='inline')
    # polEq = latex(gen_form, mode='inline', fold_short_frac=False)
    props = list(properties.keys())
    anskeys = propsLatex(properties)

    return (polEq, props, anskeys)


def golezTheorem(level):
    deg, = [gen(1,3) if level == 'easy' else gen(3,4)]
    starting_sign = gen(2,3)
    coefficients = [(-1)**(i + starting_sign)*gen(1,5) for i in range(deg+1) ]
    polynom = Poly(coefficients,x).as_expr()
    terms = deg + starting_sign
    sequence =  [str(polynom.subs({x:i+1})) for i in range(terms)]
    sequence = ', '.join(sequence)
    given = latex(sequence, mode='inline')
    properties = {r'Polynomial in General Form:  \\': polynom} 
    props = list(properties.keys())
    anskeys = propsLatex(properties)
    
    return (given, props, anskeys)


def golezTheorem3(level):
    deg, = [2 if level == 'easy' else gen(3,4)]
    polynom = genPolSequence(deg)
    sequence = []
    terms = deg+gen(2,3)
    print('terms', terms)
    for i in range(terms):
        print(i)
        term = str(polynom.subs({x: i+1}))
        sequence.append(term)
    sequence = ', '.join(sequence)
    given = latex(sequence, mode='inline')
    properties = {r'Polynomial in General Form:  \\': polynom}
    props = list(properties.keys())
    anskeys = propsLatex(properties)
    
    return (given, props, anskeys)


def golezTheorem2(level):
    deg, = [gen(2,3) if level == 'easy' else 4]
    sequence = [gen(-5,6) for i in range(deg+1) ]
    poly_coefficients = pol(sequence)
    poly_coefficients = [sympify(each) for each in poly_coefficients]
    poly_equation = Poly(poly_coefficients,x).as_expr()
    nth_term = poly_equation.subs({x: deg+2,})
    sequence.append(nth_term)
    sequence = [str(each) for each in sequence]
    sequence = ', '.join(sequence)
    given = latex(sequence, mode='inline')
    properties = {r'Polynomial in General Form:  \\': r'f(x)= '+str(poly_equation)}
    anskeys = propsLatex(properties)
    
    return (given, props, anskeys)


def problemSolving(items):

    numOfEasyQuestions = items//2
    hard = items - numOfEasyQuestions
    easyQuestions = random.sample(easy, numOfEasyQuestions)
    hardQuestions = random.sample(hard, hard)

    # for i in range(items):
    #     level = 'easy' if i <= items//2 else 'hard'
    #     if level == 'easy':


    




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