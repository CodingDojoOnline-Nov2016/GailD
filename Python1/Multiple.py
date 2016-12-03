# This assignment creates a function that reads each value in the list and
# returns a list where each item is  multipled by 5
my_list = [2, 4, 10, 16]
def multiply(a, b): #multiply function with two parameters
    new_list = [] #this is my new list
    for element in a: #start looping thru list
        new_list.append(b * element) #append each new element into new_list
    return new_list
result = multiply(my_list, 5) #Invoking multiply function with two arguments carried in
print result
