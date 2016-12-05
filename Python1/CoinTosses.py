#This assignment simulates tossing a coin 5,000 times.
import random
possibilities = {'heads': 0, 'tails': 0}
sides = possibilities.keys()
for x in range(1, 5001):
    possibilities[random.choice(sides)] += 1
    print 'Attempt', x, 'Throwing a coin...', 'Got', possibilities['heads'], 'Head(s) so far.', 'Got', possibilities['tails'], 'Tail(s) so far.'
print 'Ending the program, thank you!'
