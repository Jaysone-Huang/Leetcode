class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        result = ''
        strs.sort()
        first, last = strs[0], strs[-1]
        for index in range(min(len(first),len(last))):
            if first[index] != last[index]: return result
            result += first[index]
        return result

def run_tests():
    # Example 1
    strs = ["flower", "flow", "flight"]
    expected = "fl"
    result = longestCommonPrefix(strs)
    print(f"Input: strs = {strs}")
    print(f"Output: \"{result}\"")
    assert result == expected, f"Test failed: expected \"{expected}\", got \"{result}\""
    # Example 2
    strs = ["dog", "racecar", "car"]
    expected = ""
    result = longestCommonPrefix(strs)
    print(f"Input: strs = {strs}")
    print(f"Output: \"{result}\"")
    assert result == expected, f"Test failed: expected \"{expected}\", got \"{result}\""
    print("All tests passed.")

run_tests()