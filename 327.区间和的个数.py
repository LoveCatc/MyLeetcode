#
# @lc app=leetcode.cn id=327 lang=python3
#
# [327] 区间和的个数
#

# @lc code=start
class Solution:
    def __init__(self):
        self.rslt = 0
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        self.lower = lower
        self.upper = upper
        self.nums = nums
        self.tmp = [_ for _ in nums] 
        self.splitSort(self.nums, 0, len(self.nums)-1)
        return self.rslt
    def splitSort(self, nums, left, right):
        if left == right: 
            return 
        mid = int((right - left) / 2 + left)
        self.splitSort(nums, left, mid)
        self.splitSort(nums, mid+1, right)
        self.mergeSort(nums, left, mid, right)
    def mergeSort(self, nums, left, mid, right):
        self.tmp[left:right+1] = nums[left:right+1]
        i = left
        j = mid + 1
        p = left
        while p <= right:
            if j == right+1:
                nums[p] = self.tmp[i]
                i += 1
            elif i == mid+1:
                nums[p] = self.tmp[j]
                j += 1
            elif self.tmp[i] < self.tmp[j]:
                nums[p] = self.tmp[i]
                i += 1
            elif self.tmp[i] >= self.tmp[j]:
                nums[p] = self.tmp[j]
                j += 1
            p += 1
        i = left
        j = right
        while i <= mid and j >= mid+1:
            if self.checkValid(i, j) == 0:
                self.rslt += 1
            elif self.checkValid(i, j) == 1:
                
    def checkValid(self, left, right):
        intvSum = sum(self.nums[left:right+1])
        if intvSum > self.upper:
            return 1
        elif intvSum < self.lower:
            return -1
        else:
            return 0
# @lc code=end

