# test

class CRC:
    def CRC_code(self, s, x):
        if s == x:
            raise ValueError("the polynomial is the same as input, which might cause problems")
        add_zero = [0 for _ in range(len(x) - 1)]
        s = s + add_zero
        tmp = self.binary_division(s, x)

        if len(tmp) == 0:
            raise ValueError("the entered data may be incorrect")
        if len(tmp) < len(x) - 1:
            tmp = [0 for _ in range(len(x) - len(tmp) - 1)] + tmp
        s[-len(tmp):] = tmp
        return s

    def binary_division(self, s1, x):
        flag = 0  # flag指向最后一位
        tmp = s1[:len(x)]
        res = [0 for _ in range(len(x))]
        while flag <= len(s1) - len(x):
            if len(tmp) < len(x):
                break
            res = [0 for _ in range(len(x))]
            for i in range(len(x)):
                res[i] = tmp[i] ^ x[i]
            if sum(res) == 0:
                if flag + len(x) >= len(s1):
                    return 0
                flag += len(x)
                tmp = s1[flag:flag + len(x)]
                if len(tmp) < len(x):
                    return tmp
            else:
                zero = 0  # 结果前导0的位数
                for i in res:
                    if i == 1:
                        break
                    elif i == 0:
                        zero += 1
                res = res[zero:]
                if flag + len(x) + zero > len(s1):
                    return res + s1[flag+len(x):]
                start, end = len(x) + flag, len(x) + flag + len(x) - len(res)
                flag += len(x) - len(res)
                tmp = res + s1[start:end]

        return res

crc = CRC()
# s = [1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1]
# x = [1, 1, 0, 1, 1]
# print(crc.binary_division(s, x))

