for number in range(100,1000):
   if number%11==0:
      digits = [int(i) for i in str(number)]
      sum_of_digit_square = 0
      for digit in digits:
         sum_of_digit_square += digit*digit
      if number/11==sum_of_digit_square:
         print("The answer to the problem is ",number)
