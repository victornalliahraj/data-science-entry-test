def find_and_replace(val, find_val, replace_val):
  for i in range(len(val)):
    if val[i] == find_val:
      val[i] = replace_val
    return val


val1 = find_and_replace([1,2,3,4,2,2],2,5)
val2 = find_and_replace(['apple','banana','apple'],'apple','orange')
