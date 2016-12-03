# This assignment prints the average of the values in the list
sum = 0
a = [1, 2, 5, 10, 255, 3]
for element in a:
    sum = sum + element
avg = sum / len(a)
print avg
