# 给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在众数。 
#
# 示例 1: 
#
# 输入: [3,2,3]
# 输出: 3
#
# 示例 2: 
#
# 输入: [2,2,1,1,1,2,2]
# 输出: 2
# 
# Related Topics 位运算 数组 分治算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def majorityElement(self, nums: [int]) -> int:
        return self.boyerMooreMethod(nums)

    # 哈希表
    @staticmethod
    def hashMapMethod(nums) -> int:
        import collections
        counts = collections.Counter(nums)
        print(counts)
        return max(counts.keys(), key=counts.get)

    # BM投票法
    @staticmethod
    def boyerMooreMethod(nums) -> int:
        count = 0
        candi = None
        for num in nums:
            if count == 0:
                candi = num
            count += 1 if num == candi else -1
        return candi
# leetcode submit region end(Prohibit modification and deletion)
