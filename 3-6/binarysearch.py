## 一些注意点
## 1. 一定要注意极端情况，例如长度等
## 2. 二分查找时要使用 >>1 ，防止溢出

##704 二分查找
###在数组 [1,2,3,4,9,10]中查找元素2
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 左闭右闭
        start = 0
        end = len(nums)-1
        # 考虑一些极端情况，例如长度为0
        if len == 0:
            return -1
        while start <= end:
            mid = start + ((end-start)>>1) # 使用这种，防止溢出
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = end-1
            elif nums[mid] < target:
                start = start+1
        return -1
##35 搜索插入位置
### 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
### 时间复杂度O(logn)
# nums = [1,3,5,6], target = 5
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = start + ((end-start)>>1)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid-1
            elif nums[mid] < target:
                start = mid+1
        if nums[mid] > target:
            return mid
        else:
            return mid+1
## 34 在排序数组中查找元素的第一个和最后一个位置
### 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
###如果数组中不存在目标值 target，返回 [-1, -1]。
###你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
##nums = [5,7,7,8,8,10], target = 8
##输出[-1,-1]
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findleft(nums,target):
            # 用于寻找左侧边界
            # 对整个数组进行遍历，
            start = 0
            end = len(nums)-1
            left = -1
            while start <= end:
                mid = start + ((end-start)>>1)
                if nums[mid] == target:
                    left = mid
                    end = mid-1 # 因为找左侧，所有往左走走
                elif nums[mid] > target:
                    end = mid-1
                else:
                    start = mid+1
            return left
        def findright(nums,target):
            # 用于寻找右侧边界
            # 对整个数组进行遍历，
            start = 0
            end = len(nums)-1
            right = -1
            while start <= end:
                mid = start + ((end-start)>>1)
                if nums[mid] == target:
                    right = mid
                    start = mid+1 # 因为找的右边界，所以往右走走
                elif nums[mid] > target:
                    end = mid-1
                else:
                    start = mid+1
            return right
        left = -1
        right = -1
        left = findleft(nums,target)
        right = findright(nums,target)

        if left != -1 or right !=-1:
            return [left,right]
        return [left,right]

## 69 x的平方根
#给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
#由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
# 输入： x = 8  输出：2
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 由于找的是整数部分，因此是较小的那部分
        # 关于1
        """
        一旦大于1说明已经到了下一个数字
        例如：2和3
        可以发现2是正确答案
        9 -> 8+1
        4
        """
        start = 0
        end = x
        mid = -1
        while start <= end:
            mid = start + ((end-start)>>1)
            if mid * mid == x:
                return mid
            elif mid*mid  <x :
                start = mid+1
            elif (mid*mid) > x:
                if (mid*mid) < (x+1):
                    break
                end = mid-1
        if (mid*mid) - x >=1:
            return mid-1
        return mid
## 367 有效的完全平方数
# 给你一个正整数 num 。如果 num 是一个完全平方数，则返回 true ，否则返回 false 
# 输入：num=14 输出：false
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        start = 0
        end = num
        while start <= end:
            mid = start + ((end-start)>>1)
            result =mid *mid
            if result == num:
                return True
            elif result > num:
                end = mid-1
            elif result < num:
                start = mid+1
            else :
                return False
        return False
