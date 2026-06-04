class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = {}
        n = len(nums)

        for i in range(n):
            c = target - nums[i]
            if c in hMap:
                return [hMap[c], i]
            hMap[nums[i]] = i
        
        return []
        