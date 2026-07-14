"""https://leetcode.com/problems/group-anagrams/description/"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap={}

        for str in strs: 
          freqcount=[0]*26       
          for char in str:
            freqcount[ord(char)-97]+=1

          key =tuple(freqcount)
          if key not in hashmap:
                hashmap[key]=[]

          hashmap[key].append(str)

        result=list(hashmap.values())

        return result

               

            
            
        
        



            
            


            


        
