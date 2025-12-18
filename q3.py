def update_dictionary(dct, key, value):
  if key in dct:
    print('Key exists' {key} 'with value in dictionary as' {dct[key]})
    
  dct[key] = value
return dct

upd1 = udpate_dictionary({},'name','alice)
upd2 = update_dictionary({'age': 25}, 'age', 26)
