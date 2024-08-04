class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for n in nums:
            if n in set():
                return False
            else:
                s.add(n)

        return True