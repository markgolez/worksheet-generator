import userInput
import generateQuestions
import template2 as generateWorksheet
# import docTemplate as docTemp


class Worksheets:
    def __init__(self, details):
        self.details = details
        
    def generate(self):
        self.generatedQuestions = generateQuestions.main(self.details)
        generateWorksheet.main(self.generatedQuestions)


def main():
    
    setNumber = input(
            'Please type 0 for single worksheet and 1 for multiple set: ')
    if setNumber == '0':
        '''details =[
                        ['Polynomial','Identifying Polynomial','instruction',5], 
                        ['Polynomial','Multiplying Polynomial','instruction',5], 
                        ['Polynomial','Dividing Polynomial','instruction',5], 
                        ['Conic','Properties of Circle','instruction',5],
                        ['Conic','Properties of Ellipse','instruction',5]
                    ]
        '''
        # Ask user input
        details = userInput.main()
        worksheet = Worksheets(details)
        worksheet.generate()
        

    elif setNumber == '1':
        numberOfSet = int(input(
            'Please type the number of Sets: '))
        details = userInput.main()
        worksheets = {}

        for i in range(numberOfSet):
            worksheets[i] = Worksheets(details)
            worksheets[i].generate()
            for j in range(len(details)):
                details[j].pop()

            

main()
    
