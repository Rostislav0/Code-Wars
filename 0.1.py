def spin_words(sentence):
    c = ''
    for i in sentence.split():
        if len(i) >= 5:
            c += i[::-1]
        else:
            c += i
        c += ' '
    return c[:-1]

print(spin_words('This is another test'))
