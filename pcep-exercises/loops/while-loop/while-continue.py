for i in range(1, 21):
    if i % 5 == 0:
        continue
    print(i)
# this will remove any number that is divisble by 5 from the loop.
# so 5, 10, 15 and 20 are skipped but the while continue loop still loops through numbers 1 - 20 
# remember the end of range number "21" is excluded from the loop but 1 is included 