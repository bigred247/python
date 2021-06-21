dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}

while True:
    english = input('Enter a word in English or EXIT: ')
    if english == 'EXIT':
        break
    if english in dict:
        print('Translation:', dict[english]) #this only looks at the 'key' item
    else:
        print('No match!')
print('Bye!')
