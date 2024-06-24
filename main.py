from queue import *
from _thread import *
from time import *
import threading

import userInput
import generateQuestions
import template2 as generateWorksheet
# import docTemplate as docTemp

q = Queue()


class Start:
    def __init__(self, details):
        self.details = details
        
    def generate(self):
        self.generatedQuestions = generateQuestions.main(self.details)
        generateWorksheet.main(self.generatedQuestions)


# def start(details):
    
#     # generate equations
#     generatedQuestions = generateQuestions.main(details)
    
#     # a, = details
#     # b, c, d, e, f = a
#     # print(f)
#     '''details =[
#     ['Polynomial','Identifying Polynomial','instruction',5,[[givQuesAns],] ], 
#     ['Polynomial','Multiplying Polynomial','instruction', [[givQuesAns],] ], 
#     ['Polynomial','Diiding Polynomial','instruction', [[givQuesAns],] ], 
#     ['Conic','Properties of Circle','instruction', [[givQuesAns],] ],
#     ['Conic','Properties of Ellipse','instruction', [[givQuesAns],] ]
#     ]
#     '''

#     # generate worksheets
#     generateWorksheet.main(generatedQuestions)
#     # docTemp.main(details)
#     print('okay')




######################################





import queue 
import threading 
import time 
  
thread_exit_Flag = 0
  
class sample_Thread (threading.Thread): 
   def __init__(self, name, q): 
      threading.Thread.__init__(self)  
      self.name = name 
      self.q = q 
   def run(self): 
      print ("initializing " + self.name) 
      process_data(self.name, self.q) 
      print ("Exiting " + self.name) 
  
# helper function to process data         
def process_data(threadName, q): 
   while not thread_exit_Flag: 
      queueLock.acquire() 
      if not workQueue.empty(): 
         data = q.get() 
         queueLock.release() 
         print ("% s processing % s" % (threadName, data)) 
      else: 
         queueLock.release() 
         time.sleep(1) 
  


######################################






def createThreads(x):
    threadsList = []
    for i in range (x):
        temp = 'thread' + str(i)
        threadsList.append(temp)
  
    return threadsList



queueLock = threading.Lock() 
workQueue = queue.Queue(10) 


def main():
    
    setNumber = input(
            'Please type 0 for single worksheet and 1 for multiple set')
    if setNumber == '0':
        # Ask user input
        '''details =[
        ['Polynomial','Identifying Polynomial','instruction',5], 
        ['Polynomial','Multiplying Polynomial','instruction',5], 
        ['Polynomial','Dividing Polynomial','instruction',5], 
        ['Conic','Properties of Circle','instruction',5],
        ['Conic','Properties of Ellipse','instruction',5]]
        '''
        details = userInput.main()
        worksheet = Start(details)
        worksheet.generate()
        
        # start(details)
    elif setNumber == '1':
        numberOfSet = int(input(
            'Please type the number of Sets'))
        details = userInput.main()
        # threads = createThreads(numberOfSet)
        for i in range(numberOfSet):
            
            worksheet = Start(details)
            worksheet.generate()

    
        
        # # Create new threads 
        # for thread_name in threads: 
        #     thread = sample_Thread(thread_name, workQueue) 
        #     thread.start() 
        #     threads.append(thread) 
        
        
        # # Fill the queue 
        # queueLock.acquire() 
        # for i in range(numberOfSet): 
        #     workQueue.put((start, details))    
        
        
        # queueLock.release() 
        

        # # Wait for the queue to empty 
        # while not workQueue.empty(): 
        #     pass
        
        # # Notify threads it's time to exit 
        # thread_exit_Flag = 1
        
        # # Wait for all threads to complete 
        # for t in threads: 
        #     t.join() 
        # print ("Exit Main Thread") 




main()
    


# def spaces(no_of_spaces):
#     x = r'\\'
#     for i in range(no_of_spaces-1):
#         x += r' \\'d

#     return x


# def main():
#     filename = 'polynomial'

#     worksheet = {'Filename': filename,
#                  }

#     Topics = tis.main()


# # print(Topics)
#     topics = []
#     ans_Keys = []

#     # loop through main topics
#     for main_topic_key in Topics:
#         # loop through subtopics
#         if main_topic_key == 'polynomial':
#             for each_sub_topics_key in Topics[main_topic_key]:
#                 equations, ans_key = equation_generator(
#                     each_sub_topics_key, Topics[main_topic_key][each_sub_topics_key], 'polynomial')
#                 topics.append(
#                     (equations, tis.instructions['conics'][each_sub_topics_key]))
#                 ans_Keys.append(
#                     (ans_key, tis.instructions['conics'][each_sub_topics_key]))
#         elif main_topic_key == 'conics':
#             for each_sub_topics_key in Topics[main_topic_key]:
#                 equations, ans_key = equation_generator(
#                     each_sub_topics_key, Topics[main_topic_key][each_sub_topics_key], 'conics')
#                 topics.append(
#                     (equations, tis.instructions['conics'][each_sub_topics_key]))
#                 ans_Keys.append(
#                     (ans_key, tis.instructions['conics'][each_sub_topics_key]))

#     # checks if the same filename exists in the directory
#     files = os.listdir()
#     i = 1
#     temp = filename
#     while temp+'.pdf' in files:
#         temp = filename
#         temp += str(i)
#         i += 1
#     filename = temp

# # print(topics)
#     template.main(topics, filename, spaces(9))
#     template.main(ans_Keys, filename+'_anskey', spaces(7))


# main()
