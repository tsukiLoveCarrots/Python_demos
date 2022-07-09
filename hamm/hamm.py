class hamming():
    def code(self, code):
        r = 0
        k = len(code)
        while pow(2, r) < k + r + 1:
            r += 1
        positions = []
        for i in range(r):
            positions.append(pow(2, i) - 1)
        for pos in positions:
            code = self.insert(code, '0', pos)
        ham_code = self.list_str_transform(code, 'str2list')
        for pos in positions:
            pos_num = ham_code[pos]
            for i in range(len(ham_code)):
                if pos + 1 & i + 1 != 0:
                    pos_num = '{}'.format(int(pos_num) ^ int(ham_code[i]))
            ham_code[pos] = pos_num
        ham_code = self.list_str_transform(ham_code, 'list2str')
        return ham_code

    def check(self, code):
        check_list = []
        if 1 <= len(code) <= 4:
            check_list = [0 for _ in range(3)]
        if 4 < len(code) <= 11:
            check_list = [0 for _ in range(4)]
        for i in range(len(check_list)):
            num = 0
            for j in range(len(code)):
                if j + 1 & pow(2, i) != 0:
                    num = num ^ int(code[j])
            check_list[i] = num
        check_list.reverse()
        if sum(check_list) == 0:
            return True
        else:
            return self.calc(check_list)

    def calc(self, check_list):
        return int(''.join(str(i) for i in check_list), 2)

    def insert(self, code, num, pos):
        return code[:pos] + num + code[pos:]

    def list_str_transform(self, code, switch):
        if switch == 'str2list':
            return list(code)

        elif switch == 'list2str':
            return "".join(i for i in code)

        else:
            raise ValueError(
                "invalid switch type. Expecting 'str2list' or 'list2str', got {} instead".format("'" + switch + "'"))


ham = hamming()
