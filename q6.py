def find_first_negative(lst):
  i = 0
  j = len(lst)
  while i < j:
    if lst(i) < 0:
      return lst[i]
    i += 1
    
    Print ('No Negatives')

neg1 = find_first_negative ([3, 5, -1, 7, -2, 8])
neg2 = find_first_negative ([2, 10, 7, 0])
