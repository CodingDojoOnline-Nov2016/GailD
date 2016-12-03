# This assignment creates a function that counts from 1 to 2000 and indicates
# whether each number is odd or even
def odd_even():
    count = 1
    while count <= 2000:
        if (count % 2 == 0):
            print 'Number is', count,'. This is an even number.'
            count = count + 1 #Don't forget to increment count or else infinite loop!!
        else:
            print 'Number is', count,'. This is an odd number.'
            count = count + 1 #Don't forget to increment count or else infinite loop!!
odd_even() # Invoke my odd_even function
