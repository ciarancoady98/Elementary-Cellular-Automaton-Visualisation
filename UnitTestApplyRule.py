def setBit(number, index):
    mask = 1 << index
    number |= mask
    return number

def applyRule(ruleSet, left, middle, right):
    print(left, " " , middle, " ", right)
    print(type(left))
    ruleToApply = 0
    if right == 1:
        ruleToApply = setBit(ruleToApply, 0)
    if middle == 1:
        ruleToApply = setBit(ruleToApply, 1)
    if left == 1:
        ruleToApply = setBit(ruleToApply, 2)
    return ruleToApply

while True:
    testRuleSet = [0,1,1,1,1,1,1,0]
    testInput = list(input("Please enter test 3 bit binary values : "))
    print(applyRule(testRuleSet, int(testInput[0]), int(testInput[1]), int(testInput[2])))
