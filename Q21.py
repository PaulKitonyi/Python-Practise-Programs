def digitalsum(s):
    if s < 10:
        return s
    return s%10 + digitalsum(s//10)
        
