class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0 or len(nums) == 1: return False
        dup = {}

        for i in nums:
            if i in dup:
                return True
            else:
                dup[i] = 1
        return False
        