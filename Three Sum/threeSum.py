class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length, result = len(nums), list()
        nums.sort()
        for i, val in enumerate(nums):
            if i > 0 and val == nums[i-1]: continue
            l, r = i+1, length-1
            while l < r:
                summ = val + nums[l] + nums[r]
                if summ > 0: r -= 1
                elif summ < 0: l += 1
                else:
                    result.append([val, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return result

# Test cases
solution = Solution()

# Example 1
nums1 = [-1, 0, 1, 2, -1, -4]
output1 = [[-1, -1, 2], [-1, 0, 1]]
result1 = solution.threeSum(nums1)
print(f"Input: {nums1}\nOutput: {result1}\nExpected: {output1}\n")

# Example 2
nums2 = [0, 1, 1]
output2 = []
result2 = solution.threeSum(nums2)
print(f"Input: {nums2}\nOutput: {result2}\nExpected: {output2}\n")

# Example 3
nums3 = [0, 0, 0]
output3 = [[0, 0, 0]]
result3 = solution.threeSum(nums3)
print(f"Input: {nums3}\nOutput: {result3}\nExpected: {output3}\n")