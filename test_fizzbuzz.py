import fbTDD
#check if Prime
def test_IfPrimeNumber():
    assert fbTDD.isPrimeNumber(5) == "Prime"
#chaeck if not prime
def test_notPrimeNumber():
    assert fbTDD.isPrimeNumber(6) == ""
# check if return Number
def test_returnNum():
    assert fbTDD.fizzbuzz(11) == "11"
# check DIv15
def test_Check15():
    assert fbTDD.fizzbuzz(30) == "FizzBuzz"
# check DIv5
def test_Check5():
    assert fbTDD.fizzbuzz(10) == "Fizz"
# check DIv3
def test_Check3():
    assert fbTDD.fizzbuzz(3) == "Buzz"


