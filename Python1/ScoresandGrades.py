# This assignment prompts the user 10 times for a test score between 60 and 100
# and displays the score and corresponding grade
def apples():
    print 'Scores and Grades'
    for element in range(0, 10):
        score = int(raw_input('Please enter a score: '))
        if (score >= 60 and score <= 69):
            print 'Score:', score, 'Your grade is D'
        elif (score >= 70 and score <= 79):
            print 'Score:', score, 'Your grade is C'
        elif (score >= 80 and score <= 89):
            print 'Score:', score, 'Your grade is B'
        elif (score >= 90 and score <= 99):
            print 'Score:', score, 'Your grade is A'
        else:
            print 'Please enter a score between 60 and 100'
    print 'End of program. Bye'
apples()
