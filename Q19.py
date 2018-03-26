# A function to return the smallest number in a given list.

def smallest(l):
    if type(l) != list:
        raise TypeError('Pass a list')
    count=0
    smallest_no=None
    while count<len(l):
        if smallest_no==None:
            smallest_no=l[count]
        elif l[count]<smallest_no:
            smallest_no=l[count]
        count +=1
    return smallest_no
