class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ts = {}
        for i in range(len(nums)):
            if target - nums[i] in ts:
                return [ts[target - nums[i]],i]
            else:
                ts[nums[i]] = i
        return False