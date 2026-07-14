"""https://leetcode.com/problems/valid-anagram/description/"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False

        freqcount=[0]*26

        for s_char in s:
            freqcount[ord(s_char)-97]+=1
        for t_char in t:
            freqcount[ord(t_char)-97]-=1

        for freq_char in freqcount:
            if freq_char>0:
              return False

        return True

        