""" https://leetcode.com/problems/top-k-frequent-elements/description/ """"

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        pqheap=[]
        freqmap={}

        for num in nums:
          freqmap[num]=freqmap.get(num,0)+1

        for num in freqmap.keys():
          heapq.heappush(pqheap,[freqmap[num],num,])
          if len(pqheap)>k:
            heapq.heappop(pqheap)


        return [ num for count, num in pqheap ] 
