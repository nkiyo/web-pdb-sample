
def fizzbuzz(i):
    if i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 15 == 0:
        print('FizzBuzz')
    else:
        print(i)

import web_pdb; web_pdb.set_trace()
for i in range(1, 21):
    fizzbuzz(i)
