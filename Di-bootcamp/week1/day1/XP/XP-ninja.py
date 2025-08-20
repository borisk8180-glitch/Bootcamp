phrase = input('Enter a phrase exactly 10 characters long')
if len(phrase) > 10:
    print('Phrase is too long')
elif len(phrase) < 10:
    print("Phrase is too short")
else:
    print('Perfect string')