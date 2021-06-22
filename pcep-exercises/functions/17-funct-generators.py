def get_number():
    for i in range(1, 4):
        yield i
print(get_number())
generator = get_number()
print(next(generator))
print(next(generator))
print(next(generator))

'''
<generator object get_number at 0x7f3b5e1e9190>
1
2
3
'''