
def is_prime_number(num):
    is_prime = ""
    if num > 1:
        for iPrime in range(2, round(num // 2)):
            if (num % iPrime) == 0:
                is_prime = ""
                break
        else:
            is_prime = "Prime"
    return is_prime


def fizz_buzz(num):
    if num % 15 == 0:
        return "FizzBuzz"
    elif num % 5 == 0:
        return "Fizz"
    elif num % 3 == 0:
        return "Buzz"
    else:
        return str(num)