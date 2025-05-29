from topicsVariable import *
from topicScript import linear
from topicScript import quadratic
from topicScript.polynomial import polynomials as pol
from topicScript import expLog
from topicScript import conics
from topicScript import trigo

'''details =[
['Polynomial','Identifying Polynomial','instruction',5], 
['Polynomial','Multiplying Polynomial','instruction',5], 
['Polynomial','Dividing Polynomial','instruction',5], 
['Conic','Properties of Circle','instruction',5],
['Conic','Properties of Ellipse','instruction',5]]
'''


def main(details):
    # print(details)
    print('from genQ','cardinality', len(details[0]))
    for each in details:
        # print(each)
        if each[0] == Linear:
            questions, anskey = linear.main(each[1], each[3])
        elif each[0] == Quadratic:
            questions, anskey = quadratic.main(each[1], each[3])
        elif each[0] == Polynomial:
            questions, anskey = pol.main(each[1], each[3])
        elif each[0] == Exponential:
            questions, anskey = expLog.main(each[1], each[3])
        elif each[0] == Conic:
            questions, anskey = conics.main(each[1], each[3])
        elif each[0] == Trigonometry:
            questions, anskey = trigo.main(each[1], each[3])

        each.append([questions, anskey])

    # print(details)
    print('after genQ','cardinality', len(details[0]))

    return details
