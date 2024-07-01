import Topics

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
        chosenSubTopics = [[each, listSubTopics[int(x)], topics[each][listSubTopics[int(
            x)]]] for x in list(chosenSubTopics.split(','))]
        for each in chosenSubTopics:
            data.append(each)
 
    # Ask for the number of items per topic
    for idx, each in enumerate(data):
        print('Please type the number of items for the topic ',  each[1], ': ')
        items = int(input())
        each.append(items)


    
    return data

