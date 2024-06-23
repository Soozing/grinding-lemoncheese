class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # have two loops, trying all possibile variations (n * n)time complexity worst case,at the end (1) space

        # have a map, iterate over the list one time (n) time complexity and (n) space complexitiy

        dictionary = {}
        for i in range(len(nums)):
            indexOfPair = dictionary.get(nums[i])
            if indexOfPair != None:
                return [indexOfPair, i]
            numberToLookFor = target - nums[i]

            dictionary[numberToLookFor] = i
        
        return [0, 0]

