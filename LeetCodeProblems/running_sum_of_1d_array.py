from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSumList = []
        for i in range(len(nums)):
            runningSumList.append(sum(nums[:i + 1]))
        return runningSumList

    def runningSumOptimized(self, nums: List[int]) -> List[int]:
        for (i, num) in enumerate(nums):
            if (i != 0):
                nums[i] = num + nums[i-1]
        return nums


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    solution = Solution()

    runningSumList = solution.runningSum(nums)
    print(runningSumList)

    runningSumList = solution.runningSumOptimized(nums)
    print(runningSumList)
