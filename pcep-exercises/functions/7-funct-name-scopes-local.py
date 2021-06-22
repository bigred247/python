def show_truth():
    mysterious_var = 'New Surprise!' # LOCAL VAR
    print(mysterious_var)

mysterious_var = 'Surprise!' # GLOBAL VAR
print(mysterious_var)   # First Output (GLOBAL)
show_truth()            # Second Output (LOCAL)
print(mysterious_var)   # Third Output (GLOBAL)