# Write a generator function that generates the first 10 even numbers. 


def fun(max):
    count = 0
    while count <= max:
        yield count
        count += 2


ctr=fun(10)
print(next(ctr))
print(next(ctr))
print(next(ctr))
print(next(ctr))
print(next(ctr))
print(next(ctr))
