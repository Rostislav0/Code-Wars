def duplicate_count(text):
    text = text.lower()
    a = set(text)
    c = 0
    for i in a:
        if text.count(i) > 1:
            c += 1
    return c


print(duplicate_count('ABBA'))
