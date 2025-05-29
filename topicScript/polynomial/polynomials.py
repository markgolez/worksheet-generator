from .lessons import *
from topicsVariable import *
def main(subTopic, items):
    equations = []
    ans_key = []
    given_question_ans = []



    if subTopic == Problem_Solving:
        given, question, ans = problemSolving(items)
        item = [given, question, ans]
        given_question_ans.append(item)

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
            level = 'easy' if i <= items//2 else 'hard'
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

        elif subTopic == Golez_Theorem:
            level = 'easy' if i <= items//2 else 'hard'
            given, question, ans = golezTheorem(level)
            item = [given, question, ans]
            given_question_ans.append(item)

        

       
        equations.append((given, question))
        ans_key.append((given, ans))

   

    return (equations, ans_key)
