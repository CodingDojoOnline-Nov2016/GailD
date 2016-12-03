# This assignment prints all the multiples of 5 from 5 to 1,000,000
count = 5
while count <= 1000000:
    if(count % 5 == 0):
        print count
    count = count + 1
    #or as a For loop
    # for i in range (5, 101):
        #if(i % 5 == 0):
        #print i
