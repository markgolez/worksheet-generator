import Topics


def check_validity(values):
    msg = 'valid'
    while msg == 'valid':
        try:
            for each in values:
                isInteger = int(each)
            msg = 'valid'
            break
        except ValueError:
            msg = 'invalid'
    
    return msg

    # isValid = [int(each) for each in list(values.split(','))]
    # while False in isValid:
    #     isValid =[int(each) for each in list(chosenSubTopics.split(','))]
    
    #     print('Please input valid integer only.')
    #     chosenSubTopics = input(
    #     'Please type the numbers of the chosen topic separated by a comma. ')



def main():

    '''
    return
    
    details =[
                        ['Polynomial','Identifying Polynomial','instruction',5], 
                        ['Polynomial','Multiplying Polynomial','instruction',5], 
                        ['Polynomial','Dividing Polynomial','instruction',5], 
                        ['Conic','Properties of Circle','instruction',5],
                        ['Conic','Properties of Ellipse','instruction',5]
                    ]
    '''

    topics = Topics.mainTopics
    listTopics = {}
    # print all main topic
    for idx, each in enumerate(topics.keys()):
        print(idx+1, ': ', each)
        listTopics[idx+1] = each\
        
    chosenTopics = input(
        'Plese type the number(s) of the chosen topic separated by a comma. ')
    
    # msg = check_validity(chosenTopics)
    # while msg == 'invalid':
    #     print('Please type valid integer.')
    #     chosenTopics = input(
    #     'Plese type the number(s) of the chosen topic separated by a comma. ')
    #     msg = check_validity(chosenTopics)
    
    chosenTopics = [listTopics[int(x)] for x in list(chosenTopics.split(','))]

    data = []
    # print all subtopic
    for each in chosenTopics:
        listSubTopics = {}
        for index, every in enumerate(topics[each]):
            print(index+1, ': ', every)
            listSubTopics[index+1] = every
        chosenSubTopics = input(
            'Please type the numbers of the chosen topic separated by a comma. ')
        # List of all sub topic for each main topic ['Identifying...', 'Simplifying...',...]
        # msg = check_validity(chosenSubTopics)
        # while msg == 'invalid':
        #     print('Please input valid integer only.')
        #     chosenSubTopics = input(
        #     'Please type the numbers of the chosen topic separated by a comma. ')
        #     msg = check_validity(chosenSubTopics)
        
        chosenSubTopics = [[each, listSubTopics[int(x)], topics[each][listSubTopics[int(
            x)]]] for x in list(chosenSubTopics.split(','))]
        for each in chosenSubTopics:
            data.append(each)
 
    # Ask for the number of items per topic
    for idx, each in enumerate(data):
        print('Please type the number of items for the topic ',  each[1], ': ')
        items = int(input())
        while not int(items):
            print('Please type an integer number only')
            items = int(input())
        each.append(items)


    
    return data

