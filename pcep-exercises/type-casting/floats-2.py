average_rating = input('Please provide your avg rating: '))
print(average_rating * 3)
# Note that there's no casting -- input() returns a string, which is then multiplied by 3. 
# Returning a string by an integer results in repeating the string as many times as the integer says.
# this returns 5.05.05.0 - basically three "5.0" joined together 


average_rating = float(input('Please provide your avg rating: '))
print(average_rating * 3)
# this returns 15.0 due to the float being added