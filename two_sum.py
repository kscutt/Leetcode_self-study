class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #find the compliment
        d = {} # make an empty dictionary 
        
        for index,value in enumerate(nums): # for all values in the empty dict we just made 
            complement = target - value # define the number we are looking for
            if(complement in d):        # if that number is in the dict:
                return(d[complement],index) #  we're done return the indicies
            else:
                d[value] = index        # else add it to the dictionary and keep looking
