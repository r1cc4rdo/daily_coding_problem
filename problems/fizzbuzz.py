"""
FizzBuzz is a very simple programming task, used in software developer job
interviews, to determine whether the job candidate can actually write code.
It was invented by Imran Ghory, and popularized by Jeff Atwood [2].
It states [1]:

	Write a program that prints the numbers from 1 to 100.
	But for multiples of three print “Fizz” instead of the
	number and for the multiples of five print “Buzz”.
	For numbers which are multiples of both three and
	five print “FizzBuzz”.

Sources:
[1] https://wiki.c2.com/?FizzBuzzTest
[2] https://www.tomdalling.com/blog/software-design/fizzbuzz-in-too-much-detail
"""


def fizzbuzz():
  """
  A DRY (Don't Repeat Yourself) implementation.
  Readable and easy to understand / modify.
  """
  for number in range(1, 101):
    div3, div5 = ((number % div) == 0 for div in (3, 5))
    if div3 ^ div5:  # one of them True
      print('Fizz' if div3 else 'Buzz')
    else:  # both equal, either T or F
      print('FizzBuzz' if div3 else number)


def fizzbuzz_not_dry():
  """
  Don't be this guy. It makes my eyes bleed.
  Highly nested, hard to follow, prone to copy/paste bugs.
  """
  for i in range(100):
    n = i + 1
    if (n % 3 == 0) or (n % 5 == 0):
      if (n % 3 == 0) and (n % 5 == 0):
        print('FizzBuzz')
      elif n % 3 == 0:
        print('Fizz')
      elif n % 5 == 0:
        print('Buzz')
      else:
      	print('Error!')
    else:
      print(n)


def fizzbuzz_compact():
  """
  Don't be this guy either.
  Readability is the most importantest thing.
  """
  for number in range(1, 101):
    fizz, buzz = ('' if number % d else s for s, d in (('Fizz', 3), ('Buzz', 5)))
    print((fizz + buzz) if fizz or buzz else number)


def fizzbuzz_overengineered():
  """
  Eager dev: 'With this implementation, you can add more words at will!'.
  Not what you were asked to do. Refactoring can happen later, IF needed.
  """
  words_and_dividers = ('Fizz', 3), ('Buzz', 5)  # ('Pop', 7)
  for number in range(1, 101):
    line = ''.join('' if number % div else word for word, div in words_and_dividers)
    print(line if line else number)


if __name__ == '__main__':
  fizzbuzz()
