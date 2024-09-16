def puissance(a,b):
   if not type(a) is int or not type(b) is int:
      raise TypeError("Only integers are allowed")
   elif a==0:
      if b > 0:
          return 1
      else:
         return False
   elif b != 0:
      result=1
      for i in range(abs(b)):
         result *= a
      if a < 0 and b < 0:
         return 1/result
      else:
         return result
   else:
      return 1
