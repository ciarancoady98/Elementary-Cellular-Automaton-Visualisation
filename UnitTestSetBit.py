def setBit(number, index):
    mask = 1 << index
    number |= mask
    return number

while True:
    testNumber = 0
    testIndex = int(input("Please enter a bit index to set : "))
    testNumber = setBit(testNumber, testIndex)
    print(testNumber)
