minRange = 1
maxRange = 100

for number in range(minRange, maxRange + 1):
    outputPhrase = ""
    if number % 3 == 0:
        outputPhrase += "Fizz"
    if number % 5 == 0:
        outputPhrase += "Buzz"

    if outputPhrase == "":
        outputPhrase = number

    print(outputPhrase)
