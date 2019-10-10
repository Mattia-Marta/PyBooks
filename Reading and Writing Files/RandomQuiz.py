'''
Say you’re a geography teacher with 35 students in your class and you want to give a pop quiz on US state capitals. 
Alas, your class has a few bad eggs in it, and you can’t trust the students not to cheat. 
You’d like to randomize the order of questions so that each quiz is unique, making it impossible for any-one 
to crib answers from anyone else. Of course, doing this by hand would be a lengthy and boring affair. 
Fortunately, you know some Python.Here is what the program does:
• Creates 35 different quizzes.
• Creates 50 multiple-choice questions for each quiz, in random order.
• Provides the correct answer and three random wrong answers for each question, in random order.
• Writes the quizzes to 35 text files.
• Writes the answer keys to 35 text files.

This means the code will need to do the following:
#? Store the states and their capitals in a dictionary.
#? Call open(), write(), and close() for the quiz and answer key text files.
#? Use random.shuffle() to randomize the order of the questions and multiple-choice options
'''
#! python3

import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 
'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 
'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 
'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 
'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 
'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 
'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 
'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 
'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 
'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 
'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 
'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range(2):
    #* TODO: Create the quiz and answer key files.
    quizFile = open('capitals%s.txt' % (quizNum+1), 'w')
    answerFile = open('capitals_solutions_%s.txt' % (quizNum+1), 'w')

    #* TODO: Write out the header for the quiz. 
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')    
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))    
    quizFile.write('\n\n')
    
    #* TODO: Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)
        
    #* TODO: Loop through all 50 states, making a question for each
    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswer = list(capitals.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrongAnswer = random.sample(wrongAnswer, 3)
        answerOptions = wrongAnswer + [correctAnswer]
        random.shuffle(answerOptions)
    
        #* TODO: Write the question and answer options to the quiz file.
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write('\t%s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')    

        #* TODO: Write the answer key to a file.
        answerFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerFile.close()


        

