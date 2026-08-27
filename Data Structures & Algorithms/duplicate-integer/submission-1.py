class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num = {}
        for n in nums:
            if n in num:
                return True
            else:
                num[n] = 1
        return False
         