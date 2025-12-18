def check_divisibility(num, divisor):
  if not isinstance(num,(int,float)):
    print ('number is not numeric' num)
  
  if not isinstance(divisor,(int,float)):
      print ('number is not numeric' num)

  if isinstance(num,(int,float)) and isinstance(divisor,(int,float)):
    result = num // divisor
    if (result == 0):
      print('TRUE')
    else:
      print ('FALSE')

    return result

div1 = check_divisibility(10,2)
div2 = check_divisibility(7,3)
