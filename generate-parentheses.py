from typing import List
from functools import lru_cache

class Solution:
    def generateParenthesis0(self, n: int) -> List[str]:
        # 暴力法：生成所有可能的序列(递归法)，判断是否有效
        res = []

        def generateSeq(s):
            if len(s) == 2 * n:
                if is_valid(s):
                    res.append(s)
                return
            s += '('
            generateSeq(s)
            s = s[:-1]
            s += ')'
            generateSeq(s)

        def is_valid(s):
            cnt = 0
            for c in s:
                if c == '(':
                    cnt += 1
                else:
                    cnt -= 1
                if cnt < 0:  # 每个时刻左括号都比右括号的数量多
                    return False
            return cnt == 0

        generateSeq('')
        # print(len(res))
        return res

    def generateParenthesis1(self, n: int) -> List[str]:
        # 暴力法会生成很多无效解
        # 有效括号条件：字符串的每一个位置，左括号的个数都大于等于右括号，因此生成字符串时，
        # 左括号可以无限放，而只有剩余左括号小于右括号时可以放置右括号。

        def generateBrackets(left, right, s):
            if left == 0 and right == 0:
                res.append(s)
                return
            if left > 0:
                s += '('
                generateBrackets(left - 1, right, s)
                s = s[:-1]
            if left < right:
                s += ')'
                generateBrackets(left, right - 1, s)

        res = []
        generateBrackets(n, n, '')
        return res

    def generateParenthesis2(self, n: int) -> List[str]:
        # 递归 (a)b
        dic = {0: ['']}
        res = []
        def generateBrackets(n):
            res = []
            for i in range(n):
                if i not in dic:
                    dic[i] = dic.get(i, []) + generateBrackets(i)
                if (n - 1 - i) not in dic:
                    dic[n - 1 - i] = dic.get(n - 1 - i, []) + generateBrackets(n - 1 - i)
                for left in dic[i]:
                    for right in dic[n - 1 - i]:
                        # dic[n] += f'({left}){right}'
                        dic[n] = dic.get(n, []) + [f'({left}){right}']
                        res.append(f'({left}){right}')
            return res

        return generateBrackets(n)

    @lru_cache(None)
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        if n == 0:
            return ['']
        for i in range(n):
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n - 1 - i):
                    res.append(f'({left}){right}')
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.generateParenthesis(3))
