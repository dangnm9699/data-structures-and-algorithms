from typing import List

"""
Link: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/610/week-3-july-15th-july-21st/3815/
"""


class Solution:
    def __init__(self):
        self.type = "Daily Challenge"
        self.date = "Week 3: July 15th - July 21st"
        self.year = "2021"
        self.name = "Valid Triangle Number"

    def find_c(self, nums: List[int], left: int, right: int, val: int) -> int:
        while right >= left:
            mid = (left + right) // 2
            if nums[mid] >= val:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def triangle_number(self, nums: List[int]) -> int:
        """
        | 1 <= nums.length <= 1000
        | 0 <= nums[i] <= 1000
        """
        nums.sort()
        n = len(nums)
        res = 0
        for a in range(n-2):
            if nums[a] != 0:
                c = a + 2
                for b in range(a+1, n-1):
                    c = self.find_c(nums, c, n-1, nums[a] + nums[b])
                    res += c - b - 1
        return res


if __name__ == '__main__':
    # read input
    nums = list(map(int, input().split()))
    # get solution
    solution = Solution()
    result = solution.triangle_number(nums)
    # print solution
    print(result)
