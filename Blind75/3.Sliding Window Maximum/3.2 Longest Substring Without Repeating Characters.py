
""" https://leetcode.com/problems/longest-substring-without-repeating-characters/description/ """


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength=0
        """ numset=set()
        j=1
        for i in range(0,len(s),j):
            while i<len(s) and s[i] not in numset  :
                numset.add(s[i])
                i+=1

            maxlength=max(maxlength, len(numset))
            numset=set()
            j=i+1 """

        maxlength=0
        hashmap={}
        j=0
        for i in range(0,len(s)):
            if s[i] in hashmap  :
                j= max(j,hashmap[s[i]])
              
            maxlength=max(maxlength, i-j+1)
            hashmap[s[i]]=i+1
           
        return maxlength
