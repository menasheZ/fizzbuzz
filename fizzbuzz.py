
for i in range(1,101):
    isPrime = ""
    if i > 1:
        for iPrime in range(2, round(i//2)):
            if(i % iPrime) == 0:
                isPrime= ""
                break
        else: isPrime = "Prime"
    if i % 15 == 0:
        print("FizzBuzz"+" "+isPrime)
    elif i % 5 == 0:
        print("Fizz"+" "+isPrime)
    elif i % 3 == 0:
        print("Buzz"+" "+isPrime)
    else:
        print(str(i)+" "+isPrime)


