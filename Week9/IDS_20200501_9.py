i =1
while i <= 100: # stop
    if i % 15 == 0:
        print('Fizz Buzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0 :
        print('Buzz')
    else:
        print(i) 
    i += 1 # step