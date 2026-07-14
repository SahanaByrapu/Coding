""" https://leetcode.com/problems/contains-duplicate/description/ """

### java

class Solution {
    public boolean containsDuplicate(int[] nums) {
        
        Set<Integer> freqset =new HashSet<>();

        for(int num:nums)
        {
            if(freqset.contains(num))
             return true;
            
            freqset.add(num);
        }

        return false;
    }
}


### Python

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
       visited=set()

       for num in nums:
         if num in visited:
             return True
         visited.add(num)

       return False
