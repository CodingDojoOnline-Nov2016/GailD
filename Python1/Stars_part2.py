# this is a modification of Stars part I - Allow a list containing integers and strings to be
# passed to the draw_stars() function. When a string is passed, instead of  displaying *,
# display the first letter of the string
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
string = '*'
def draw_stars(x, string):
    for element in x:
        if type(element) == int:
            asterisk = element * string
            print asterisk
        elif type(element) == str:
            first_char = element[0][0]
            name = first_char.lower()
            numchars = name * len(element)
            print numchars
draw_stars(x, string)
