def sumoddeven(n):
    if type(n) != list:
        return 'Please pass a list'
    total = 0
    for index in range(len(n)):
        if n[index]%2==0:
            i = n[index]//2
            total += i
        else:
            j = n[index]*2
            total += j
    return total
