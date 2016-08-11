def factorial(n):
    if n >= 1:
        numbers = list(range(1,n+1))
        answer = 1
        for number in numbers:
            answer *= number
        return answer
    else:
        return None
