#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#

# @lc code=start
class Solution:
    def __init__(self):
        self.tmp = []
        self.rslt = 0
    
    def reversePairs(self, nums: List[int]) -> int:
        self.tmp = [_ for _ in nums]
        self.splitSort(nums, 0, len(nums)-1)
        return self.rslt
    
    def splitSort(self, nums, left, right):
        if left == right:
            return
        else:
            mid = int((right - left) / 2 + left)
            self.splitSort(nums, left, mid)
            self.splitSort(nums, mid+1, right)
            self.mergeSort(nums, left, mid, right)

    def mergeSort(self, nums, left, mid, right):
        self.tmp[left:right+1] = nums[left:right+1]
        
        for i in range(left, mid+1):
            j = mid+1
            while j <= right and self.tmp[i] > 2*self.tmp[j]:
                j += 1
            self.rslt += j-mid-1

        i = left
        j = mid + 1
        p = left

        # print(tmp, left, right, mid)
        while (p <= right):
            if i == mid + 1:
                nums[p] = self.tmp[j]
                j += 1
            elif j == right + 1:
                nums[p] = self.tmp[i]
                i+=1
            elif self.tmp[i] < self.tmp[j]:
                nums[p] = self.tmp[i]
                i+=1
            elif self.tmp[i] >= self.tmp[j]:
                nums[p] = self.tmp[j]
                j+=1
            p += 1
        # print(rslt)
# @lc code=end

