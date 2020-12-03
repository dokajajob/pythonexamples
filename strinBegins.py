def st(s):
    if s.startswith('Is'):
        return s
    else:
        return 'Is' + s

print(st('test'))
print(st('Israel'))
