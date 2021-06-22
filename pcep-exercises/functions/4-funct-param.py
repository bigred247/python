def print_letter_count(text, letter):
    counter = 0
    for char in text:
        if char == letter:
            counter += 1
    print('Number of', letter, 'is', counter)
#print_letter_count('supercalifragilisticexpialidocious', 'e') #explicily define text and letter values
#print_letter_count(text='supercalifragilisticexpialidocious', letter='e') #define text and letter paramaters
print_letter_count(letter='e', text='supercalifragilisticexpialidocious') #define text and letter paramaters in reverse order and still works

# note there are 2 print statements needed to make this work (one is indented)