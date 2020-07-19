import fbTDD


# check if Prime
def test_if_prime_number():
    assert fbTDD.is_prime_number(5) == "Prime"


# check if not prime
def test_not_prime_number():
    assert fbTDD.is_prime_number(6) == ""


# check if return Number
def test_return_num():
    assert fbTDD.fizz_buzz(11) == "11"


# check DIv15
def test_check15():
    assert fbTDD.fizz_buzz(30) == "FizzBuzz"


# check DIv5
def test_check5():
    assert fbTDD.fizz_buzz(10) == "Fizz"


# check DIv3
def test_check3():
    assert fbTDD.fizz_buzz(3) == "Buzz"


