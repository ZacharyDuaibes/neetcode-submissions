class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        findDup = {}
        count = 1
        for i in range(len(nums)):
            if nums[i] not in findDup:
                count = 1
                findDup[nums[i]] = (count)
            else:
                count += 1
                findDup[nums[i]] = (count)
                return True
        return False


            

         