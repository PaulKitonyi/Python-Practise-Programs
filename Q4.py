#A program to search through a list and print out the largest number.

li = [3,4,2,56,44,32,7,5]
largest = None
for i in li:
    if largest is None:
        largest = i
    elif i > largest:
        largest = i

print (largest)
