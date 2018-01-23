def largestnum(n):
    if type(n) != list:
        return 'kindly insert a list'
    largest = None
    for large in range(len(n)):
        if largest is None:
            largest = n[large]
        elif n[large] > largest:
            largest = n[large]
    return(largest)
    
