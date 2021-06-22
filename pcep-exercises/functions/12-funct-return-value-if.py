def get_average(input_numbers):
    sum = 0.0
    for number in input_numbers:
        sum += number
    average = sum / len(input_numbers)
    return average
#print('the average is:', get_average([5.0, 3.5, 7.8, 9.9, 10.0])) #function exits after printing

average = get_average([5.0, 3.5, 7.8, 9.9, 10.0])
if average > 5.0:
    print('The average is too high!')