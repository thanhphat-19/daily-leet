class Solution:
    def maximum69Number (self, num: int) -> int:
        # find left most 6
        # store left6 postion - multiple with lef6 position
        # multiple 3 three with position
        # plus wiht num 
        temp_num=num
        left6 = -1 
        pos = 1 
        while temp_num > 0:
            digit = temp_num % 10
            if digit == 6:
                left6=pos
            temp_num //=10
            pos *=10
        if left6 != -1:
            num += 3*left6
        return num
        
