from itertools import islice

genexpr = (x for x in range(10) if x % 2 == 0)
print(type(genexpr))
print(next(genexpr), next(genexpr), next(genexpr))
for i in genexpr:
    print(i)


class LoopOverEven:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __next__(self):
        if self.current >= self.n:
            raise StopIteration
        while True:
            self.current += 1
            if self.current % 2 == 0:
                return self.current

    def __iter__(self):
        return self


for x in LoopOverEven(10):
    print(x)


import string

def abc(word):
    """Generate letters from a word in alphabetical order"""
    for x in string.ascii_lowercase:
        if x in word:
            yield x

for x in abc("banana"):
    print(x)


def multiabc(sentence):
    for word in sentence.split():
        yield from abc(word)
        yield '----'

for x in multiabc("banana racecar"):
    print(x)



def countdown(n):
    while n > 0:
        yield n
        n -=1
    print("Blastoff!")

for x in countdown(10):
    print(x)


def flatten(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


mylist = [[1, 2], [3], [4, [5, [6]]]]
print(list(flatten(mylist)))  # Should return [1, 2, 3, 4, 5, 6]



def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacci(10)))

def my_range(start, stop, step):
    while start < stop:
        yield start
        start += step



for x in list(my_range(0, 1, 0.1)):  # Should work with floats
    print(x)

def sliding_window(seq, n):
    """Yields successive overlapping subsequences of fixed length"""
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


for y in list(sliding_window([1, 2, 3, 4, 5], 3)):
    print(y)