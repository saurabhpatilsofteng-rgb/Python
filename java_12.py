#advance python
from email import iterators

num = [10,20,30]

iterators = iter(num)

print(next(iterators))
print(next(iterators))

#Generator produce values lazily insted of creating the entire resuult at once


def count_numbers(limit):
    number = 1

    while number <= limit:
        yield number
        number += 1

for value in count_numbers(3):
    print(value)