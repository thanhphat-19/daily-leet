
from typing import List
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # App 1: two pointer
        # if right == 0, continue
        # if right != 0, take len of the sub_arr
        # number of zero = lengh * (lenght +1) // 2 and move left pointer right after right pointer
        sum_zero = 0
        left= 0
        right= 0
        length_sub_arr = 0
        for right in (range(len(nums))):
            if nums[right] == 0:
                continue
            else: 
                length_sub_arr = right - left
                sum_zero += length_sub_arr * (length_sub_arr + 1) // 2
                left = right + 1
        # if last index is zero, 
        if nums[-1] == 0:
            length_sub_arr = len(nums) - left
            sum_zero += length_sub_arr * (length_sub_arr + 1) // 2
            

            
        return sum_zero





if __name__ == "__main__":
    sol = Solution()
    nums = [1,3,0,0,2,0,0,4]
    result = sol.zeroFilledSubarray(nums)
    print(result)