patterns = ['  #\n  #\n  #\n  #\n  #', '###\n  #\n###\n#\n###']
userInput = input('Enter a string of numbers: ')
toPrint = []
representations= {
    '0': ('###', '# #', '# #', '# #', '###'),
    '1': ('  #', '  #', '  #', '  #', '  #'),
    '2': ('###', '  #', '###', '#  ', '###'),
    '3': ('###', '  #', '###', '  #', '###'),
    '4': ('# #', '# #', '###', '  #', '  #'),
    '5': ('###', '#  ', '###', '  #', '###'),
    '6': ('###', '#  ', '###', '# #', '###'),
    '7': ('###', '  #', '  #', '  #', '  #'),
    '8': ('###', '# #', '###', '# #', '###'),
    '9': ('###', '# #', '###', '  #', '###'),
    '.': ('   ', '   ', '   ', '   ', '  #'),
}
digits = [representations[digit] for digit in userInput]
print(digits)
# now digits is a list of 5-tuples, each representing a digit in the given number
# We'll print the first lines of each digit, the second lines of each digit, etc.
for i in range(5):
    print("  ".join(segment[i] for segment in digits))