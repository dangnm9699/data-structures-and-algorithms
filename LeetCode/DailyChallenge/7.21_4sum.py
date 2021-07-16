from typing import List

"""
Link: https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/610/week-3-july-15th-july-21st/3816/
"""


class Solution:
    def __init__(self):
        self.type = "Daily Challenge"
        self.date = "Week 3: July 15th - July 21st"
        self.year = "2021"
        self.name = "4Sum"

    def four_sum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        | 1 <= nums.length <= 200
        | -10^9 <= nums[i] <= 10^9
        | -10^9 <= target <= 10^9
        """
        d = dict()
        n = len(nums)
        res = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                key = nums[i] + nums[j]
                if key in d.keys():
                    d[key].append((i, j))
                else:
                    d[key] = [(i, j)]
        for first_key in d.keys():
            second_key = target - first_key
            if second_key in d.keys():
                first_pairs = d[first_key]
                second_pairs = d[second_key]
                for (i, j) in first_pairs:
                    for (k, l) in second_pairs:
                        quad_idx = [i, j, k, l]
                        if len(set(quad_idx)) != len(quad_idx):
                            continue
                        quad = [nums[i], nums[j], nums[k], nums[l]]
                        quad.sort()
                        if quad not in res:
                            res.append(quad)
        res.sort()
        return res


if __name__ == '__main__':
    # read input
    nums = list(map(int, input().split()))
    target = int(input())
    # get solution
    solution = Solution()
    result = solution.four_sum(nums, target)
    # print solution
    print(result)
