# 1-masala
class SimpleIterator:
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        if self.num <= 10:
            current = self.num
            self.num += 1
            return current
        else:
            raise StopIteration

iterator = SimpleIterator()
for i in iterator:
    print(i)
# ------------------------------------------------------------
# 2-masala
my_list = [1, 2, 3, 4, 5]
list_iterator = iter(my_list)
for item in list_iterator:
    print(item)

# ------------------------------------------------------------
# 3-masala
class ReverseIterable:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = len(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > 0:
            self.index -= 1
            return self.iterable[self.index]
        else:
            raise StopIteration

reverse_iter = ReverseIterable([1, 2, 3, 4, 5])
for item in reverse_iter:
    print(item)

# ------------------------------------------------------------
# 4-masala
string = "Python"
string_iter = iter(string)
for char in string_iter:
    print(char)
# -------------------------------------------------------------
# 5-masala
class EvenIterator:
    def __init__(self, nums):
        self.nums = nums
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.nums):
            current = self.nums[self.index]
            self.index += 1
            if current % 2 == 0:
                return current
        raise StopIteration

evens = EvenIterator([1, 2, 3, 4, 5, 6, 7, 8])
for even in evens:
    print(even)
# -------------------------------------------------------------
# 6-masala
numbers = iter([1, 2, 3, 4, 5])
print("Sum:", sum(numbers))
# -------------------------------------------------------------
# 7-maasala
my_list = [1, 2, 3, 4, 5]
iterator = iter(my_list)
found = 3 in iterator
print("Element mavjudmi:", found)
# -------------------------------------------------------------

# Generator misollari:

# 1-masala
def simple_range(start, end):
    current = start
    while current < end:
        yield current
        current += 1

for num in simple_range(1, 10):
    print(num)
# ------------------------------------------------------------
# 2-masala
def word_lengths(text):
    for word in text.split():
        yield len(word)

for length in word_lengths("Hello world Python generators"):
    print(length)
# - ------------------------------------------------------------

# 3-masala
def odd_numbers():
    num = 1
    while True:
        yield num
        num += 2

odd_gen = odd_numbers()
for _ in range(10):
    print(next(odd_gen))

# -------------------------------------------------------------
# 4-masala
def even_numbers():
    num = 2
    while True:
        yield num
        num += 2

even_gen = even_numbers()
for _ in range(10):
    print(next(even_gen))
# -------------------------------------------------------------
# 5-masala
def infinite_numbers():
    num = 1
    while True:
        yield num
        num += 1

inf_gen = infinite_numbers()
for _ in range(10):
    print(next(inf_gen))

# -------------------------------------------------------------
# 6-masala
def square_numbers(nums):
    for num in nums:
        yield num ** 2

for square in square_numbers(range(1, 11)):
    print(square)
# -------------------------------------------------------------
# 7-masala
def sum_generator(nums):
    yield sum(nums)

print(next(sum_generator([1, 2, 3, 4, 5])))
# - -----------------------------------------------------------

# 8-masala
def positive_numbers(nums):
    for num in nums:
        if num > 0:
            yield num

for positive in positive_numbers([-3, 1, -1, 4, -5, 6]):
    print(positive)
# - -----------------------------------------------------------

# 9-masala
import random

def random_numbers(count):
    for _ in range(count):
        yield random.randint(1, 100)

for rnd in random_numbers(5):
    print(rnd)
# - -----------------------------------------------------------

# 10-masala
def prime_numbers(limit):
    count = 0
    num = 2
    while count < limit:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num
            count += 1
        num += 1

for prime in prime_numbers(10):
    print(prime)
# - -----------------------------------------------------------

# 11-masala
def reverse_string(s):
    for char in reversed(s):
        yield char

for char in reverse_string("Python"):
    print(char)
# - -----------------------------------------------------------

# 12-masala
def product_of_numbers(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
        yield product

for prod in product_of_numbers(5):
    print(prod)
# - -----------------------------------------------------------