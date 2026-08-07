class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use hashmap - contains key, value
        hashNums = {}
        # loop through list of nums, 
        # add to hash, check if value of key > 1
        for i in nums:
            if i in hashNums:
                return True 
            else: 
                hashNums[i] = 1
        return False



        