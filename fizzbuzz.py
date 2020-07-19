import fbTDD

for i in range(1,101):
    isPrime = fbTDD.isPrimeNumber(i)
    isfissbuzz = fbTDD.fizzbuzz(i)
    print(isfissbuzz + " " + isPrime)


