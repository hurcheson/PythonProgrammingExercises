# Ordinal Suffix
def ordinalSuffix(number):
    numberStr = str(number)
    # if(numberStr[-2:-1] in ['11', '12' , '13']):
    #     print(numberStr + 'th')
    if numberStr[-2:] == '11' or numberStr[-2:] == '12' or numberStr[-2:] == '13':
        return numberStr + 'th'
    elif(numberStr[-1] == '1'):
        return numberStr + 'st'
    elif(numberStr[-1] == '2'):
        return numberStr + 'nd'
    elif(numberStr[-1] == '3'):
        return numberStr + 'rd'
    else:
        return numberStr + 'th'



assert ordinalSuffix(0) == '0th'
assert ordinalSuffix(1) == '1st'
assert ordinalSuffix(2) == '2nd'
assert ordinalSuffix(3) == '3rd'
assert ordinalSuffix(4) == '4th'
assert ordinalSuffix(10) == '10th'
assert ordinalSuffix(11) == '11th'
assert ordinalSuffix(12) == '12th'
assert ordinalSuffix(13) == '13th'
assert ordinalSuffix(14) == '14th'
assert ordinalSuffix(101) == '101st'
