#This assignment creates a function that takes a list of numbers and prints out '*'
x = [4, 6, 1, 3, 5, 7, 25]
string = '*'
def draw_stars(x, string):
    for element in x:
        asterisk = element * string
        print asterisk
draw_stars(x, string)


# string1 = '&'
# more = string1 * 4
# print more
