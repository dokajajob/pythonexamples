def st(s):
    if s.startswith('Is'):
        return s
    else:
        return 'Is' + s

print(st('test', one, two))
print(st('Israel'))
