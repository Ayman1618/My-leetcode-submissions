class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * len(text1)
        lcs = 0

        for i in text2:
            l = 0
            for j, val in enumerate(dp):
                if l < val:
                    l = val
                elif i == text1[j]:
                    dp[j] = l + 1
                    lcs = max(lcs, l + 1)
        
        return lcs

        