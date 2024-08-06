class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        charS = set()
        maxlen = 0
        left = 0
        for right in range(len(s)):
            if s[right] not in charS:
                charS.add(s[right])
                maxlen = max(maxlen, right - left +1)

            else:
                while s[right] in charS:
                    charS.remove(s[left])
                    left+=1
                charS.add(s[right])
        return maxlen

def test_solution():
    solution = Solution()
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    assert solution.lengthOfLongestSubstring("bbbbb") == 1
    assert solution.lengthOfLongestSubstring("pwwkew") == 3
    assert solution.lengthOfLongestSubstring("") == 0
    assert solution.lengthOfLongestSubstring(" ") == 1
    assert solution.lengthOfLongestSubstring("au") == 2
    assert solution.lengthOfLongestSubstring("dvdf") == 3
    assert solution.lengthOfLongestSubstring("anviaj") == 5
    print("All test cases pass")

test_solution()
