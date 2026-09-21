class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sub = {0:1}
        total = 0
        count = 0
        for n in nums:
            total += n
            if total - k in sub:
                count += sub[total-k]
            
            sub[total] = 1 + sub.get(total, 0)
        return count