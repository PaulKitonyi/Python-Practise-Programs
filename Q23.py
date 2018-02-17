def second_largest(l):
    largest=None
    second_large=None

    for i in range(len(l)):
        if largest==None:
            largest=l[i]
        elif l[i]>largest:
            second_large=largest
            largest=l[i]
        elif l[i]>second_large:
            second_large=l[i]
    return second_large

print(second_largest([2,3,4469,6,565]))
            
