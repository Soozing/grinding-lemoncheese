class Solution:
    def isAnagram(s: str, t: str) -> bool:
        letterCountDict = {}

        # Can do simple edege cases for better performance times ie. string length comparisons

        for i in range(len(s)):
            if s[i] not in letterCountDict:
                letterCountDict[s[i]] = 1
            else:
                letterCountDict[s[i]] = letterCountDict[s[i]] + 1

        for i in range(len(t)):
            if t[i] not in letterCountDict:
                letterCountDict[t[i]] = -1
            else:
                letterCountDict[t[i]] = letterCountDict[t[i]] - 1

        for value in letterCountDict.values():
            if value != 0:
                return False
            
        return True

# Test Examples
testArguements = [
    [['anagram', 'nagaram'], True],
    [['rat', 'car'], False],
]

for (args, expectedResult) in testArguements:
    (s1, s2) = args
    assert Solution.isAnagram(s1, s2) == expectedResult

