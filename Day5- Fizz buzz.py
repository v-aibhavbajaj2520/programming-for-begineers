for work in range (1,101,1):
    if work%3 ==0 and work%5 ==0:
        print("FizzBuzz")
    elif work%5 ==0:
        print("Buzz")
    elif work%3 ==0:
        print("Fizz")
    else:
        print(work)
