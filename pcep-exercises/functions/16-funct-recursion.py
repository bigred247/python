def unique(input_list=[]):
  to_return = []
  for el in input_list:
    if el not in to_return:
      to_return.append(el)
  return to_return
print(unique([1, 4, 1, 5, 1, 2, 1]))


# removes duplicates and returns below
# [1, 4, 5, 2]