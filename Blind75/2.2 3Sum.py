


""" https://leetcode.com/problems/3sum/ """

class Solution:

   def threeSum(self, nums: list[int]) -> list[list[int]]:
       result=[]  
       nums.sort()
       for i in range(len(nums)-2):
         if i > 0 and nums[i]==nums[i-1]:
            continue 

         target= -1 * nums[i] 
         pairs=self.twoSum(nums,target,i+1)

         for pair in pairs:
           result.append([nums[i],pair[0],pair[1]])

       return result

   def twoSum(self,nums:list[int], target:int, index:int)-> list[list[int]]:
      hashmap ={}
      pairs=[]
      for j in range(index,len(nums)):
         remaining=target-nums[j]
         if remaining in hashmap:
            pairs.append([nums[j],remaining])
         hashmap[nums[j]]=j

      return pairs



      




      
        
