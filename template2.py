from pylatex.position import VerticalSpace
import quantities as pq
from sympy import *
from pylatex.base_classes import Environment
from pylatex.package import Package
from pylatex import Document, Section, Subsection, MultiColumn, Tabular, LongTabu, LongTable, Command, Math, Quantity, PageStyle, Head, MiniPage, Foot, LargeText, \
    MediumText, LineBreak, simple_page_number, Enumerate, Center
from pylatex.utils import bold, NoEscape
import os
from topicsVariable import *


def no_of(spaces):
    x = r'\\'
    for i in range(spaces-1):
        x += r' \\'

    return x


''' details = [['Polynomial',
            'Adding and Subtracting Polynomial',
            'Perform the given operations and give the simpliest form.',
            3,
            [
                ['(2*x**3 + 2*x**2 - 4*x)+(8*x**4 + 4*x**3 - 12*x**2 - 4*x + 4)', ['Simpliest Form:   ', 'Leading Term:   ', 'Degree:  ', 'Leading Coefficient:   ', 'Constant Term:   '],
                 ['Simpliest Form:   8*x**4 + 6*x**3 - 10*x**2 - 8*x + 4', 'Leading Term:   8*x**4', 'Degree:  4', 'Leading Coefficient:   8', 'Constant Term:   4']],
                ['(-2*x**3 + 5*x**2 - 4*x + 1)-(-2*x**3 - 7*x**2 - 8*x - 3)', ['Simpliest Form:   ', 'Leading Term:   ', 'Degree:  ', 'Leading Coefficient:   ',
                                                                               'Constant Term:   '], ['Simpliest Form:   12*x**2 + 4*x + 4', 'Leading Term:   12*x**2', 'Degree:  2', 'Leading Coefficient:   12', 'Constant Term:   4']],
                ['(-2*x**3 + 6*x**2 + 2*x - 6)-(2*x**3 + 3*x**2 - 2*x - 3)', ['Simpliest Form:   ', 'Leading Term:   ', 'Degree:  ', 'Leading Coefficient:   ', 'Constant Term:   '],
                 ['Simpliest Form:   -4*x**3 + 3*x**2 + 4*x - 3', 'Leading Term:   -4*x**3', 'Degree:  3', 'Leading Coefficient:   -4', 'Constant Term:   -3']]
            ]
            ]
           ]
'''


def worksheet(details, filename):
    # Loop for worksheet and answer key
    for i in range(2):
        print(i)
        geometry_options = {
            "head": "0.5pt",
            "margin": "0.4in",
            "bottom": "1in",
            "top": "0.5in"
        }

        doc = Document(geometry_options=geometry_options)

        doc.preamble.append(Command('renewcommand', arguments=[
                            NoEscape('\\thesection'), NoEscape('\Alph{section}')]))
        doc.preamble.append(Command('renewcommand', arguments=[NoEscape(
            '\\thesubsection'), NoEscape('\\Alph{subsection}.')]))

        with doc.create(MiniPage(align='l')):

            doc.append(MediumText(
                'Name ___________________  Student No.___ G__/___ Date: ________Score: ____ '))
            doc.append(NoEscape(r'\\'))
            doc.append(MediumText(
                'Nickname: ___________________   Worksheet No.: _____ '))
            doc.append(NoEscape(r' \\'))

        doc.packages.append(Package('ragged2e'))
        doc.packages.append(Package('multicol'))
        # doc.packages.append(Package('xspace'))
        doc.packages.append(Package('amsmath'))

        # doc.preamble.append(Command('newcolumntype', arguments=[
        #                     NoEscape('L'), NoEscape('>{$}l<{$}')]))

        filename = filename+'anskey' if i == 1 else filename
        subTopicIndex = 0
        
        for each in details:
            '''details =[
            ['Polynomial','Identifying Polynomial',
                'instruction',5,[[givQues],[givAns]] ],
            ['Polynomial','Multiplying Polynomial','instruction',5,[[givQuesAns],]]
            ]
            '''
                
            mainTopic, subTopic, instruction, items, givQuesAns = each
            # Diplay Centered Topic
            doc.append(VerticalSpace('0.1in'))
            # doc.append(NoEscape(r'\\'))
            doc.append(NoEscape(r'\begin{Center}'))
            doc.append(LargeText(bold(subTopic)))
            doc.append(NoEscape(r'\end{Center}'))

            with doc.create(Subsection(NoEscape(instruction))):

                with doc.create(Enumerate(enumeration_symbol=r"\arabic*)",
                                          options={'start': 1})) as enum:
                    doc.append(NoEscape(r'\enlargethispage{\baselineskip}'))

                    doc.append(NoEscape(r'\begin{multicols}{2}'))
                    for indx, item in enumerate(givQuesAns[i]):

                        enum.add_item(NoEscape(item[0]))
                        space = 13 if indx < 6 else 15
                        doc.append(
                            # spacesSubTopics[subTopicIndex])))
                            # spacesSubTopics[subTopicIndex])))
                            NoEscape(no_of(Spaces[subTopic])))
                        for k in item[1]:
                            doc.append(NoEscape(k))
                            doc.append(NoEscape(r' \\'))
                        
                        # if indx+1 % 3 == 0 and indx != 3:
                        #     doc.append(NoEscape(r' \\'))
                        # if indx+1 % 2 == 0 :
                        #     doc.append(NoEscape(r'\newpage'))

                    doc.append(NoEscape(r'\end{multicols}'))
                    # doc.append(NoEscape(r'\newpage'))
                    # doc.append(NoEscape(r'\newpage'))


            # Page breaks at third sub topic
            subTopicIndex += 1
            if subTopicIndex == 3:  # 3:
                doc.append(NoEscape(r'\newpage'))

        doc.generate_pdf(filename, clean_tex=True)
        print('end')



def main(details):
    
    files = os.listdir('output/')
    i = 1
    temp = 'polynomial - #'
    while temp+'.pdf' in files:
        temp = 'polynomial - #'
        temp += str(i)
        i += 1
    filename = 'output/' + temp
    worksheet(details, filename)
    
