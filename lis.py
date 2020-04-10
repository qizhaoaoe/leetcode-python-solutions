# -*- coding: UTF-8 -*-
def longest_subseq(nums):
    n = len(nums)
    f = [[] for _ in range(n)]
    f[0]=[nums[0]]
    
    for i in range(1, n):
        l = 1
        t = i
        # print(i)
        f[i]=[nums[i]]
        for j in range(i-1, -1, -1):
            if nums[j] < nums[i]:
                if (len(f[j])+1) >= l:
                    l = len(f[j])+1
                    t = j
        if t != i:
            f[i] = f[t]+f[i]
	    # print(i, t, f[i])
    return f[-1]
# nums = [2,1 ,5, 3, 6, 4, 8, 9, 7]
nums = [0, -2,1 ,5, 3]
print(longest_subseq(nums))


def longest_subseq1(nums):
    n = len(nums)
    f = [1 for _ in range(n)]
    f[0] = 1
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                f[i] = max(f[i], f[j]+1)

    l = max(f)
    res = []
    nums_dic = {}
    for i in range(n):
        if f[i] == l:
            max_idx = i
        if f[i] not in nums_dic:
            nums_dic[f[i]] = [nums[i]]
        else:
            nums_dic[f[i]].append(nums[i])


    print(nums_dic)
    for i in range(1, l+1):
        res.append(min(nums_dic[i]))
        
    return res
                
# nums = [2,1 ,5, 3, 6, 4, 8, 9, 7]
nums = [0, -2,1 ,5, 3]
print(longest_subseq1(nums))











