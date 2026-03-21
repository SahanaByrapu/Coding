"""https://leetcode.com/problems/majority-element/description/"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

     count=0
     for i in range(0,len(nums)):
     #Boyer-Moore Voting Algorithm
        if(count==0):
            candidate=nums[i]
            count+=1
        else:
          count+= 1 if(candidate==nums[i]) else -1

     return candidate
      


#Space Complexity:O(1)
#Time Complexity:O(n)
