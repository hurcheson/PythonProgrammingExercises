# I/O of file

# Writes content to a file
def writeToFile(fileName, fileContent):
    with open(fileName, 'w') as fileObj:
        fileObj.write(fileContent)

# appending an input to the file specified
def appendToFile(fileName, appendInput):
    with open(fileName, 'a') as fileObj:
        fileObj.write(appendInput)

# reading from the specified file
def readFromFile(fileName):
    with open(fileName, 'r') as fileObj:
        return fileObj.read()


writeToFile('greet.txt', 'Hello!\n')
appendToFile('greet.txt', 'Goodbye!\n')
assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'

