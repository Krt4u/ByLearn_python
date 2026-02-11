
def a():
    yield 1
    yield 2
    yield 3

funa = a()

aa = next(funa)
bb = next(funa)
cc = next(funa)
print(aa,bb,cc)