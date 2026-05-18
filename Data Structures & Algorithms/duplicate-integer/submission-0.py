class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums: # [1,2,3,2]
            if n in hashset:
                return True
            hashset.add(n)
        return False