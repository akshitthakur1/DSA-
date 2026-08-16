class Solution:
    def reverse(self, x: int) -> int:
        y = str(x)
       
        if y[0] == "-":
            reversed_str = "-" + y[1:][::-1]
        else:
            reversed_str = y[::-1] 
            
       
        rev = int(reversed_str)
       
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        
        return rev