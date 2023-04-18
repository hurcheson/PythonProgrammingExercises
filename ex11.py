# Hours, Minutes, Seconds
def getHoursMinutesSeconds(totalSeconds):
    # If totalSeconds is 0, just return '0s'
    if totalSeconds == 0:
        return '0s'
    
    # Set hours to 0, then add an hour for every 3600 seconds removed
    # totalSeconds until totalSeconds is less than 3600:
    hours = 0

    while totalSeconds >= 3600:
        hours += 1
        totalSeconds -= 3600
    

    # Setting minutes 0
    minutes = 0
    while totalSeconds >= 60:
        minutes += 1
        totalSeconds -= 60
    
    # Setting seconds to 0
    seconds = totalSeconds

    # A list to contain the string hour/minute/second
    hms = []

    # Appending hours to the list
    if hours > 0:
        hms.append(str(hours) + 'h')
    
    if minutes > 0:
        hms.append(str(minutes) + 'm')

    if seconds > 0:
        hms.append(str(seconds) + 's')
    
    return ' '.join(hms)


assert getHoursMinutesSeconds(30) == '30s'
assert getHoursMinutesSeconds(60) == '1m'
assert getHoursMinutesSeconds(90) == '1m 30s'
assert getHoursMinutesSeconds(3600) == '1h'
assert getHoursMinutesSeconds(3601) == '1h 1s'
assert getHoursMinutesSeconds(3661) == '1h 1m 1s'
assert getHoursMinutesSeconds(90042) == '25h 42s'
assert getHoursMinutesSeconds(0) == '0s'
