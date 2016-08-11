def fizzbuzz(n):
    output = []
    for i in range(1,n):
        if (i % 3 == 0) and (i % 5 == 0):
            output.append("FizzBuzz")
        elif (i % 3 == 0):
            output.append("Fizz")
        elif (i % 5 == 0):
            output.append("Buzz")
        else:
            output.append(i)
    return output
