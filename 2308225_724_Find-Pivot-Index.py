class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # # O(n^2) solution - time out
        # def cal_sum_left(index: int, nums: List[int]):
        #     sum_left = 0
        #     for i in range(index):
        #         sum_left += nums[i]
            
        #     return sum_left

        # def cal_sum_right(index: int, nums: List[int]):
        #     sum_right = 0
        #     for i in range(index + 1, len(nums)):
        #         sum_right += nums[i]
                
        #     return sum_right
    
        # for i in range(len(nums)):
        #     if cal_sum_left(i, nums) == cal_sum_right(i,nums):
        #         return i
        # return -1
        # O(n) solution
        left_sum = 0 
        right_sum = sum(nums)
        for index, value in enumerate(nums):
            right_sum -= value
            if left_sum == right_sum:
                return index
            left_sum += value
        return -1
