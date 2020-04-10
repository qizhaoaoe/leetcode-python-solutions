### 题目描述
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof

### 解题思路
- 枚举+暴力: O(target \sqrt(target))
- 枚举+数学优化: O(target)
- 双指针: O(target)

### 代码
```python
class Solution:
    # 暴力+枚举
    def findContinuousSequence1(self, target: int) -> List[List[int]]:
        res = []
        n = target // 2
        ss = 0
        for i in range(1, n+1):
            ss = i
            j = i+1
            while j < target:
                if ss > target:
                    break
                if ss == target:
                    res.append([x for x in range(i, j)])
                ss += j
                j += 1
                 
        return res
    # 双指针
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = []
        l = 1
        r = 2
        while l < r:
            ss = (l+r)*(r-l+1)/2
            if ss == target:
                res.append([x for x in range(l, r+1)])
                l += 1
            if ss > target:
                l += 1
            else:
                r += 1
        return res
```
