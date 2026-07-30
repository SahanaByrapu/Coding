""" https://leetcode.com/problems/container-with-most-water/description/ """" 

class Solution:
    def maxArea(self, height: List[int]) -> int:
       
            maxvolume=0
            left=0
            right=len(height)-1
            while left<right:
                minheight=min(height[left],height[right])
                volume= (right-left)* minheight
                maxvolume=max(maxvolume,volume)
                if( height[left] < height[right]):
                    left+=1
                else:
                    right-=1


            return maxvolume
