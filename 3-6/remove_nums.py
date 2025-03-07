## 移除元素
# 重点使用双指针 -> 不需要额外的数据空间，使用O(1)
# 块指针用于遍历，慢指针用于标记合理的长度
## 不要考虑那么多！！！！ -> 写一个通用的而不是专门的算法
## 字符串是不能修改的，可以转换为list，并且可以使用 ...join(list)转换会到字符串的格式
## 初始化一个长度为num的列表：[0]*num
## num*num -> num**2


## 27 移除元素
## 给定 nums = [3,2,2,3], val = 3, 移除等于3的元素，函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。 
## 你不需要考虑数组中超出新长度后面的元素。
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # 双指针
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            if nums[-1] == val:
                return 0
            else:
                return 1
        length = len(nums)-1
        slow = 0
        fast = 0
        while fast <= length:
            if nums[slow] != val:
                if slow != fast and nums[fast]!= val:
                    nums[slow] = nums[fast]
                    slow +=1
                    fast +=1
                elif nums[fast] == val:
                    fast +=1
                else:
                    slow +=1
                    fast +=1
            elif nums[slow] == val:
                if nums[fast] == val:
                    fast +=1
                else:
                    nums[slow] = nums[fast]
                    slow +=1
                    fast +=1
        return slow
## 26删除有序数组中的重复项
给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，
##返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0 or len(nums) == 1:
            length = len(nums)
            return length
        slow = 0
        fast = 1
        while fast <= len(nums)-1 and slow<fast:
            if nums[slow] == nums[fast]:
                fast +=1
            elif nums[slow] != nums[fast]:
                slow +=1
                nums[slow] = nums[fast]
                fast+=1
        return slow+1

## 283 移动0
## 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
## 先进行了将0后移的操作，然后经无用的改为0
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 :
            return 0
        if len(nums) == 1:
            if len(nums) == 0:
                return 0
            else:
                return 1
        slow = 0
        fast = 0
        while fast <= len(nums)-1:
            if fast == slow:
                if nums[slow] == 0:
                    fast +=1
                else:
                    fast +=1
                    slow +=1
            else:
                if nums[fast] != 0:
                    nums[slow] = nums[fast]
                    slow +=1
                    fast+=1
                else:
                    fast +=1
        for i in range(slow,len(nums)):
            nums[i] = 0
        return slow-1
##844 比较含推格的字符串
##给定 s 和 t 两个字符串，当它们分别被输入到空白的文本编辑器后，如果两者相等，返回 true 。# 代表退格字符。
class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #字符串不能直接修改
        def delet_block(s):
            fast = 0
            slow = 0
            length = len(s)-1
            list_s = list(s)
            while fast <= length:
                if fast == slow:
                    if list_s[fast] == '#':
                        if slow!=0:
                            slow -=1
                        fast +=1
                    else:
                        slow+=1
                        fast+=1
                else:
                    if list_s[fast] != '#':
                        list_s[slow] = list_s[fast]
                        slow +=1
                        fast +=1
                    elif list_s[fast] == '#':
                        if slow != 0:
                            slow -=1
                        fast+=1
            return ''.join(list_s[:slow])
        new_s = delet_block(s)
        new_t = delet_block(t)
        if new_s == new_t:
            return True
        else:
            return False

##977有序数组的平方
##给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 使用双指针
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums[0]*nums[0]]
        right = len(nums)-1
        left = 0
        new_s = [0] * len(nums)
        index = len(nums)-1
        while left <=right and index >=0:
            if nums[left]*nums[left] <= nums[right]*nums[right]:
                new_s[index] = nums[right]*nums[right]
                right -=1
                index -=1
            else:
                new_s[index] = nums[left]*nums[left]
                index -=1
                left +=1
        return new_s
