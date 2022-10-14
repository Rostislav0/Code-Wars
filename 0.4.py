import re


def to_camel_case(text):
    x = re.split('-|_', text)
    d = [x[0]]
    for i in x[1:]:
        d.append(i.title())
    return ''.join(d)

print(to_camel_case('the-stealth-warrior'))