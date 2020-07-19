
def isPrimeNumber(num):
    isPrime = ""
    if num > 1:
        for iPrime in range(2, round(num // 2)):
            if (num % iPrime) == 0:
                isPrime = ""
                break
        else:
            isPrime = "Prime"
    return isPrime

def fizzbuzz(num):
    if num % 15 == 0:
        return ("FizzBuzz")
    elif num % 5 == 0:
        return("Fizz")
    elif num % 3 == 0:
        return("Buzz")
    else:
        return(str(num))