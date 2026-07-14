"""https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/"""

#Dictionary Approach

 class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        sum_dict={}

        for i in range(0,len(numbers)):
               remaining=target-numbers[i]
               if remaining in sum_dict:
                    return [sum_dict[remaining]+1,i+1]

               sum_dict[numbers[i]]=i


#Time Complexity  O(n)
#Space Complexity O(n)


#Two Pointer Approach
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1

        while(left<right):
        
           sum=numbers[left]+numbers[right]

           if sum == target:
               return [left+1,right+1]
           elif sum < target:
              left+=1
           else:
                right-=1


#Time complexity: O(n)
#Space complexity:O(1)
 
