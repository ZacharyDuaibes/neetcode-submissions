class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use hashmap - contains key, value
        hashNums = {} # using dict
        # use set: seen=set()

        # loop through list of nums, 
        # add to dict, check if value of key > 1
        for num in nums:
            if num in hashNums: #in seen for set
                return True 
            hashNums[num] = 1
        return False



        