class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use hashmap - contains key, value
        hashNums = {} # using dict
        # use set: seen=set()

        # loop through list of nums, 
        # add to dict, check if value of key > 1
        for num in nums:
            if num in hashNums: 
            #for set: if num in seen
                return True 
            hashNums[num] = 1
            #for set: seen.add(num)
        return False



        