class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums) - 1
        low = 0

        mid = (low + high) // 2
        
        while low < high:
            if target == nums[mid]: 
                return mid
            elif target < nums[mid]: 
                high = mid - 1
                mid = (low + high) // 2
            elif target > nums[mid]:
                low = mid + 1
                mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        else:
            return -1