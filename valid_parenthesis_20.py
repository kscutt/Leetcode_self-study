class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0 : return False             # it must be even to be matching
        
        dict = { '(' : ')' ,'{' : '}', '[' : ']' }    # create a dictionary with all pairs of parentheses 
        
        stack = []                                    # create an empty stack 
        
        for i in s:                                   # for each element in s
            if i in dict.keys():                      # if it's a right opening parenthesis {[(, it needs 
                stack.append(i)                       # a mate so add to the search stack
            else:    
                if stack == []: return False          # if the stack is empty return false
                a = stack.pop()                       # pop the value from the stack
                if i not in dict[a]: return False     # if it's not in the dictionary it can't be valid
            
        return stack == []                            # return the status if the stack is empty or not
                                                      # an empty stack means it's a match because all have 
                                                      # been popped for comparison :)
        
