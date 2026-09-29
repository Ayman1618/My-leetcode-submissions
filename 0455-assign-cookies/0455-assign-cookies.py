class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()                      
        s.sort()                      
        send = len(s) - 1             
        gend = len(g) - 1             
        res = 0

        while send >= 0 and gend >= 0:
            if g[gend] <= s[send]:    
                res += 1
                gend -= 1             
                send -= 1             
            else:
                gend -= 1             

        return res