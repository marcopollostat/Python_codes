def fizzbuzz(a):
    div3 = a%3
    div5 = a%5
    if (div3 == 0) and ( not(div5 == 0) ):
        return "Fizz"
    elif (div5 == 0) and ( not(div3 == 0) ):
        return "Buzz"
    elif div3 == 0 and div5 == 0:
        return "FizzBuzz"
    elif ( not(div3 == 0) ) and ( not(div5 == 0) ):
        return a
