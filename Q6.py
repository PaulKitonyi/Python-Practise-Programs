# A program to search through a list and print out the smallest number.

li = [3,4,2,56,44,32,7,5]
smallest = None
for i in li:
    if smallest is None:
        smallest = i
    elif i < smallest:
        smallest = i

print(smallest)
