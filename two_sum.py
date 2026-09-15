# Time Complexity : O(N)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No


# Your code here along with comments explaining your approach
#I have checked if the complement that is target - nums[i] is in HashMap if it is return the index with the current index.
#Then I have used HashMap for storing elements with corresponding to to their index as values.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

#Time - O(N2)
#Space - O(1)

class Solution:
    def twoSum(self, nums:List[int], target: int) -> List[int]:
        if not nums:
            return []
        dict = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in dict:
                return [i, dict[comp]]
            dict[nums[i]] = i
            
