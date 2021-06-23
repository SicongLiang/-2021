class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 从后往前遍历是否等于9，如果不等于9，则此位置+=1并跳出，其他的设为0
        for index in range(len(digits)-1, -1, -1):
            if digits[index] != 9:
                digits[index] += 1
                break
            else:
                digits[index] = 0
        # 如果第一位需要进位，则第一位设置为1，同时末尾添加0
        if digits[0] == 0:
            digits[0] = 1
            digits.append(0)

        return digits
