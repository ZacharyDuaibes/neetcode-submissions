class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use hashmap - contains key, value
        hashNums = {} # can also just do seen=set()
        # loop through list of nums, 
        # add to hash, check if value of key > 1
        for num in nums:
            if num in hashNums:
                return True 
            else: 
                hashNums[num] = 1
        return False



        