
def reverse(string):
    reversedString = ""
    index = len(string)
    while index > 0:
        reversedString += string[index - 1]
        index = index - 1
    return reversedString

word = input("Enter a word")
print(reverse(word))