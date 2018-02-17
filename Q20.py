'''A function to give digitalsum of a given string(ie 2017=2+0+1+7)'''
def digitalsum(n):
    total=0
    count=0
    while count<len(str(n)):
        total +=int(str(n)[count])
        count += 1
    return total
