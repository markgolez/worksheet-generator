# from numpy.core.numeric import Infinity
from sympy import *
from topicsVariable import *
import numpy as np
import scipy as sy
import random
import math
import time

x, y, a, b, h, k, r, s, t = symbols('x y a b h k r s t')
# PM = Symbol('±', real=True)


# def to_latex_wrapper(exprs, no_newline):
#     newline = ''
#     for i in range(no_newline):
#         newline += '\\ '
#     expr = latex(exprs)
#     expr = '\('+expr+newline+'\)'

#     return expr


# def inline_wrapper(exprs):
#     expr = latex(exprs)
#     expr = '$\\left('+expr+'\\right)$'

#     return expr


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


# def pm(p, q):
#     x = str(p)
#     y = str(q)
#     temp = x+PM+y
#     return temp


def generate():
    x = random.randint(-9, 12)
    while x == 0:
        x = random.randint(-5, 6)
    return x


def gen_circle(level):
    genEq = UnevaluatedExpr((x-h)**2)+UnevaluatedExpr((y-k)**2)
    center = (random.randint(-10, 10), random.randint(-10, 10))
    radius = random.randint(1, 15)
    parExp = genEq.subs({h: center[0], k: center[1]})
    parEq = Eq(parExp, radius**2)
    standard_equation = simplify(expand(parExp - radius**2))
    if level == 'easy':
        given = parEq
    elif level == 'hard':
        given = Eq(standard_equation, 0)
    conEq = latex(given, mode='inline')

    properties = {'radius:   ': radius, 'center:   ': center}
    # prop_keys = properties.keys()
    # for each in prop_keys:
    #     properties[each] = to_latex_wrapper(properties[each], 4)
    # props = [x + str(properties[x]) for x in prop_keys]

    props = list(properties.keys())
    anskeys = propsLatex(properties)

    return (conEq, props, anskeys)


def pm(a, b):
    x = str(a)
    y = str(b)
    temp = x+'\pm '+y
    return temp


def gen_hyper_ellipse(conic, level):
    form = 'standard' if level == 'easy' else 'general'
    ##    genEq = s*UnevaluatedExpr(((x-h)**2)/(a**2))+t*UnevaluatedExpr(((y-k)**2)/(b**2))
    genEq = s*((x-h)**2)/(a**2)+t*((y-k)**2)/(b**2)
    center = (random.randint(-5, 7), random.randint(-5, 7))
    p = random.randint(1, 6)
    q = random.randint(1, 6)
    while p == q:
        q = random.randint(1, 6)
    axisLength = (p, q)
# print(axisLength)
    if conic == 'hyperbola':
        u = random.choice((-1, 1))
        v = -1*u
        c = simplify(sqrt(axisLength[0]**2 + axisLength[1]**2))
        if u < 0:
            orientation = 'Vertical'
            asymptote = pm(center[1], UnevaluatedExpr(
                frac(Rational(axisLength[1], axisLength[0])))*UnevaluatedExpr(x-center[0]))
        else:
            orientation = 'Horizontal'
            asymptote = pm(center[1], UnevaluatedExpr(
                frac(Rational(axisLength[0], axisLength[1])))*UnevaluatedExpr(x-center[0]))
        asymptote = '$y = ' + asymptote + '$'
        c = latex(c)
    elif conic == 'ellipse':
        u = v = 1

        if axisLength[0] > axisLength[1]:
            orientation = 'Horizontal'
            c = simplify(sqrt(axisLength[0]**2 - axisLength[1]**2))
            eccentricity = c/axisLength[0]
        else:
            orientation = 'Vertical'
            c = simplify(sqrt(axisLength[1]**2 - axisLength[0]**2))
            eccentricity = c/axisLength[1]
        c = latex(c)

    parExp = genEq.subs(
        {h: center[0], k: center[1], a: axisLength[0], b: axisLength[1], s: u, t: v})

    if form == 'standard':
        parEq = Eq(parExp, 1)
    elif form == 'general':
        product_of_axis_squared = (axisLength[0]**2)*(axisLength[1]**2)
        parExp = product_of_axis_squared*parExp
        parEq = Eq(expand(parExp-product_of_axis_squared), 0)

    if orientation == 'Horizontal':
        majorAxis = 'y = ' + str(center[1])
        minorAxis = 'x = ' + str(center[0])
        len_major_axis = axisLength[0]*2
        len_minor_axis = axisLength[1]*2
        focus = '$('+pm(center[0], c)+',' + str(center[1])+')$'

        vertices = '$('+pm(center[0], axisLength[0]
                           )+',' + str(center[1])+')$'
        coVertices = '$('+str(center[0])+',' + \
            pm(center[1], axisLength[1])+')$'

        # focus = str(focus)
        # vertices = str(vertices)
        # coVertices = str(coVertices)
    else:

        majorAxis = 'x = ' + str(center[0])
        minorAxis = 'y = ' + str(center[1])
        len_minor_axis = axisLength[0]*2
        len_major_axis = axisLength[1]*2
        focus = '$('+str(center[0]) + ',' + pm(center[1], c)+')$'
        if conic == 'ellipse':
            vertices = '$('+str(center[0])+',' + \
                pm(center[1], axisLength[0])+')$'
            coVertices = '$('+pm(center[0], axisLength[1]
                                 )+',' + str(center[1])+')$'
        elif conic == 'hyperbola':
            vertices = '$('+str(center[0])+',' + \
                pm(center[1], axisLength[1])+')$'
            coVertices = '$('+pm(center[0], axisLength[0]
                                 )+',' + str(center[1])+')$'
    print(focus, vertices, coVertices)
    properties = {'Orientation: ': orientation,
                  'Center: ': center,
                  'Vertices: ': vertices,
                  'Focus: ': focus,
                  'Co-vertices: ': coVertices
                  }
    if conic == 'hyperbola':
        properties['Transverse axis: '] = majorAxis
        properties['Conjugate axis: '] = minorAxis
        properties['asymptote: '] = asymptote

    elif conic == 'ellipse':
        properties['Major axis: '] = majorAxis
        properties['Minor axis: '] = minorAxis
        properties['Length Major Axis: '] = len_major_axis
        properties['Length Minor Axis: '] = len_minor_axis
        properties['eccentricity: '] = eccentricity
    print(properties)
    conEq = latex(parEq, mode='inline', fold_short_frac=False)
    props = list(properties.keys())
    anskeys = propsLatex(properties)

    return (conEq, props, anskeys)


# def equation_generator(conic):

    # if conic == 'hyperbola':
    #     parEq, properties, props = gen_hyperbola('hyperbola')
    # elif conic == 'ellipse':
    #     parEq, properties, props = gen_hyperbola('ellipse')
    # elif conic == 'circle':
    #     parEq, properties, props = gen_circle()

    # tex = to_latex_wrapper(parEq)

    # return (tex, properties, props)


def main(subTopic, items):
    equations = []
    ans_key = []
    given_question_ans = []
    for i in range(items):
        if subTopic == Identifying_Conic_Sections:
            pass

        elif subTopic == Conversion_from_Standard_to_General_Form:
            operation = 'add' if i <= i//2 else 'minus'
            level = 'easy'
            given, question, ans = operations(operation, level)
            item = [given, question, ans]
            given_question_ans.append(item)

        elif subTopic == Properties_of_Circle:
            level = 'easy' if i < items//2 else 'hard'
            given, question, ans = gen_circle(level)
            item = [given, question, ans]
            given_question_ans.append(item)

        elif subTopic == Finding_Equation_of_Circle:
            level = 'easy' if i <= i//2 else 'hard'
            given, question, ans = operations('divide', level)
            item = [given, question, ans]
            given_question_ans.append(item)

        elif subTopic == Properties_of_Ellipse or Properties_of_Hyperbola:
            level = 'easy' if i < items//2 else 'hard'
            conic_section = 'ellipse' if subTopic == Properties_of_Ellipse else 'hyperbola'
            given, question, ans = gen_hyper_ellipse(conic_section, level)
            item = [given, question, ans]
            given_question_ans.append(item)

        equations.append((given, question))
        ans_key.append((given, ans))

    # print(equations)
    # print(ans_key)

    return (equations, ans_key)


# def gen_ellipse():
##    genEq = UnevaluatedExpr(((x-h)**2)/(a**2))+UnevaluatedExpr(((y-k)**2)/(b**2))
##    center = (random.randint(-10, 10),random.randint(-10, 10))
##    p = random.randint(1, 15)
##    q = random.randint(1, 15)
# while p==q:
##        q = random.randint(1, 15)
##    axisLength = (p,q)
##    parExp = genEq.subs({h:center[0] , k: center[1], a:axisLength[0], b: axisLength[1]})
##    parEq = Eq(parExp, 1)
# if axisLength[0]>axisLength[1]:
##        orientation = 'Horizontal'
##        majorAxis = 'y = '+ str(center[1])
##        minorAxis = 'x = '+ str(center[0])
##        len_minor_axis = axisLength[1]*2
##        len_major_axis = axisLength[0]*2
##        c = simplify(sqrt(axisLength[0]**2 - axisLength[1]**2))
##        eccentricity = c/axisLength[0]
##        c = latex(c)
##        focus = (pm(center[0], c), center[1])
##        vertices = (pm(center[0],axisLength[0]), center[1])
##        coVertices = (center[0], pm(center[1], axisLength[1]))
##
# asymptote =
# else :
##        orientation = 'Vertical'
##        majorAxis = 'x = '+ str(center[0])
##        minorAxis = 'y = '+ str(center[1])
##        len_minor_axis = axisLength[0]*2
##        len_major_axis = axisLength[1]*2
##        c = simplify(sqrt(axisLength[1]**2 - axisLength[0]**2))
##        eccentricity = c/axisLength[0]
##        c = latex(c)
##        focus = (center[0], pm(center[1],c))
##        vertices = (center[0], pm(center[1],axisLength[0]))
##        coVertices = (pm(center[0],axisLength[1]), center[1])
##
##
##
# properties = {'orientation: ': orientation,
# 'center: ': center,
# 'focus: ': focus,
# 'vertices: ':vertices,
# 'co-vertices: ': coVertices,
# 'major axis: ': majorAxis,
# 'minor axis: ': minorAxis,
# 'length of major axis: ': len_major_axis,
# 'length of minor axis: ': len_minor_axis,
# 'eccentricity: ': eccentricity
# }
##
##    prop_keys = properties.keys()
##    pm_group = ['focus: ','vertices: ','co-vertices: ']
##
# for each in prop_keys:
##        properties[each] = to_latex_wrapper(properties[each])
# props = [x + str(properties[x]) for x in prop_keys]#to_latex_wrapper(circle[1]) #[to_latex_wrapper(x+':'+str(circle[1][x])) for x in circle[1].keys()]
##
##
##
# return (parEq, properties, props)
