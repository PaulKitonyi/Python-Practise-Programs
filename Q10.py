lst = []
words=input('Enter words:')
s=words.split(' ')
for word in s:
    if word not in lst:
        lst.append(word)
print(' '.join(sorted(lst)))
