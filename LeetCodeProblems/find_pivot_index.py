from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftIndex = 0
        rightIndex = len(nums) - 1
        leftSum = 0
        rightSum = 0
        while (rightIndex != leftIndex):
            if leftSum < rightSum:
                leftSum += nums[leftIndex]
                print("left sum", str(rightSum))
                leftIndex += 1
            else:
                rightSum += nums[rightIndex]
                print("right sum", str(rightSum))
                rightIndex -= 1

        if leftSum == rightSum:
            return leftIndex

        return -1

    def findPivotRecursion(self, nums: List[int], rightIndex: int,  leftIndex: int = 0, leftSum: int = 0, rightSum: int = 0) -> int:
        if leftSum == rightSum and rightIndex != 0 and leftIndex != 0:
            return leftIndex

        if rightIndex == leftIndex:
            return -1

        if leftSum < rightSum:
            leftSum += nums[leftIndex]
            print("left sum", str(rightSum))
            leftIndex += 1
        else:
            rightSum += nums[rightIndex]
            print("right sum", str(rightSum))
            rightIndex -= 1

        self.findPivotRecursion(nums, leftSum, rightSum, leftIndex, rightIndex)

    def pivotIndexOptimized(self, nums: List[int]) -> int:
        self.findPivotRecursion(nums, len(nums))


if __name__ == "__main__":
    nums = [1, 1, 2, 1, 1]
    solution = Solution()

    # leftIndex = solution.pivotIndex(nums)
    # print(leftIndex)

    leftIndex = solution.pivotIndexOptimized(nums)
    print(leftIndex)
