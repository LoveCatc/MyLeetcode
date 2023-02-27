#
# @lc app=leetcode.cn id=315 lang=python3
#
# [315] 计算右侧小于当前元素的个数
#

# @lc code=start
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        rslt = [0 for _ in nums]
        tmp = [0 for _ in nums]
        def splitSort(nums, left, right):   # [left, right]
            # print(left, right)
            if right - left == 0:
                return 
            else:
                mid = int((right - left) / 2 + left)
                splitSort(nums, left, mid)
                splitSort(nums, mid+1, right)
                mergeSplit(nums, left, mid, right)
            
        def mergeSplit(nums, left, mid, right):
            nonlocal rslt, tmp

            for i in range(left, right+1):
                tmp[i] = nums[i]
            
            p = left
            q = mid + 1
            i = left
            print(left,mid,right,tmp)
            while i <= right:
                if p > mid:
                    nums[i] = tmp[q]
                    q += 1
                elif q > right:
                    rslt[p] += q-mid-1
                    nums[i] = tmp[p]
                    p += 1
                elif tmp[p] <= tmp[q]:
                    rslt[p] += q-mid-1
                    nums[i] = tmp[p]
                    p += 1
                elif tmp[p] > tmp[q]:
                    nums[i] = tmp[q]
                    q += 1
                i += 1
            print(nums)
        splitSort(nums, 0, len(nums)-1)
        return rslt




# @lc code=end

