import fbTDD

for i in range(1,101):
    isPrime = fbTDD.is_prime_number(i)
    is_fizz_buzz = fbTDD.fizz_buzz(i)
    print(is_fizz_buzz + " " + isPrime)

print("BOOM")
