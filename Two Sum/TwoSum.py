class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = dict()
        for index, val in enumerate(nums):
            complement = target - val
            if complement in table:
                return [index, table[complement]]
            else:
                table[val] = index
        return []

def test_two_sum():
    solution = Solution()
    
    # Test case 1: Simple case
    assert solution.twoSum([2, 7, 11, 15], 9) == [1, 0], "Error: Test case 1 failed"
    
    # Test case 2: Negative numbers
    assert solution.twoSum([-1, -2, -3, -4, -5], -8) == [4, 2], "Error: Test case 2 failed"
    
    # Test case 3: Multiple pairs summing to target
    assert solution.twoSum([3, 2, 4], 6) == [2, 1], "Error: Test case 3 failed"
    
    # Test case 4: Single element repeated
    assert solution.twoSum([3, 3], 6) == [1, 0], "Error: Test case 4 failed"
    
    # Test case 5: No valid pairs
    assert solution.twoSum([1, 2, 3, 4], 10) == [], "Error: Test case 5 failed"
    
    # Test case 6: Pair with zero
    assert solution.twoSum([0, 4, 3, 0], 0) == [3, 0], "Error: Test case 6 failed"
    
    # Test case 7: Empty list
    assert solution.twoSum([], 0) == [], "Error: Test case 7 failed"
    
    # Test case 8: Pair with the same element twice
    assert solution.twoSum([5, 75, 25], 100) == [2, 1], "Error: Test case 8 failed"

    print("All test cases passed")

# Call the test function
test_two_sum()