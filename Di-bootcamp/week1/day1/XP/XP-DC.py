#1
phrase = input('Enter a phrase exactly 10 characters long')
#2
if len(phrase) > 10:
    print('Phrase is too long')
elif len(phrase) < 10:
    print("Phrase is too short")
else:
    print('Perfect string')
#3
print(phrase[0])
print(phrase[-1])
#4
result = ''
for char in phrase:
    result = result + char
    print(result)