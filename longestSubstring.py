class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        currCount = 0
        maxCount = 0
        subStrDict = {}
        l = len(s)
        if l == 1:
            return 1
        x=0
        while x < l-1:
            subStrDict[s[x]]= 1
            currCount+=1
            j = x+1
            while j< l:
                if s[j] not in subStrDict:
                    subStrDict[s[j]]=1
                    currCount+=1
                else:
                    x=j
                    break
                j+=1

            if currCount > maxCount:
                maxCount = currCount
            subStrDict.clear()
            currCount=0
            if j == l:
                break
        return maxCount

print(Solution().lengthOfLongestSubstring("dvdh"))