
def next_period_generator():
    yield 4
    print('qweqwe')
    yield 5
    yield 10
    for i in range(10000):
        yield i

[4, 5, 10]



g = next_period_generator()
print(next(g))
print(next(g))
print(next(g))
print(next(g, None))

for i in range(5):
    print(i)

print(range(5))
