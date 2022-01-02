class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 : return False     # all negatives are false
        
        divider = 1                 # initialize divider 
        
        while x >= 10 * divider:    # while x is equal to or greater than 10*divider   
            divider *= 10           # multiply divider by 10 so that we can get rid of 
                                    # the left digit 
        while x:
            right_digit = x % 10    # get the number in the ones place
            left_digit = x//divider # get the number in the xths place
            
            if left_digit != right_digit: return False # if they're not == it cant be a palindrome
            
            x = (x % divider) // 10 # chop off left digit with mod, chop off right with //
            divider = divider // 100  # update the divider for our chopped x number 
        return True 
