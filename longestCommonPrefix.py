class Solution:
    
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        answer = ""
        
        for i in range(len(strs[0])):
            for k in strs:
                if i == len(k) or k[i] != strs[0][i]:
                    return answer
            answer += strs[0][i]
            
        return answer

sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))