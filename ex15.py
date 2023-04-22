# A function for finding the mediann of a given set of numbers
def median(numbers):
    # Exception Check: checking if the value passed to the parameter is valid or empty
    if len(numbers) == 0:
        return None
    
    middle_index = len(numbers) // 2
    sorted_numbers = sorted(numbers)

    # Odd and Even number of elements detection
    if len(numbers) % 2 == 1:
        for i, num in enumerate(sorted_numbers):
            if i == middle_index:
                return num

    
    # Finds median of even numbers
    if len(numbers) % 2 == 0:
        middle_numbers =[]
        for i, num in enumerate(sorted_numbers):
            if i == middle_index -1 or i== middle_index:
                middle_numbers.append(num)
        
        return sum(middle_numbers) / 2

assert median([]) == None
assert median([1, 2, 3]) == 2
assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5
assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6
import random
random.seed(42)
testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]
for i in range(1000):
 random.shuffle(testData)
 assert median(testData) == 6
