def show_truth():
    global mysterious_var
    mysterious_var = 'New Surprise!' # LOCAL VAR
    print(mysterious_var) # this is printed only when "show_truth()" below is called

mysterious_var = 'Surprise!' # = GLOBAL VAR
print(mysterious_var)   # First Output (GLOBAL)
show_truth()            # Second Output (LOCAL)
print(mysterious_var)   # Third Output (LOCAL) 