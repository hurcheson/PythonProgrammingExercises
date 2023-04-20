# A function to return the largest number in a list
def getBiggest(numbers):
    if len(numbers) == 0:
        return None
    biggest = numbers[0]

    for i in numbers:
        if  i > biggest:
            biggest = i
    
    return biggest

assert getBiggest([1, 2, 3]) == 3
assert getBiggest([3, 2, 1]) == 3
assert getBiggest([28, 25, 42, 2, 28]) == 42
assert getBiggest([1]) == 1
assert getBiggest([]) == None