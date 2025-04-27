class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numMap = {} # dictionary to store the numbers and their indices
        n = len(nums)

        # Build the hash table
        for i in range(n):
            numMap[nums[i]] = i # nums[0]=2 -> numMap[2]=0, nums[1]=7 -> numMap[7]=1

        # Find the complement
        for i in range(n):
            complement = target - nums[i]
            # 檢查 complement 這個數字有沒有在字典 numMap 的「key」裡 (雜湊方法)
            # 把字典的 key 和 value 反過來存（即 key 為索引、value 為數字）不可行
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]


sol1 = Solution().twoSum([2, 7, 11, 15], 9)
print(f"[2, 7, 11, 15], 9 => {sol1}")
sol2 = Solution().twoSum([3, 2, 4], 6)
print(f"[3, 2, 4], 6 => {sol2}")
sol3 = Solution().twoSum([3, 3], 6)
print(f"[3, 3], 6 => {sol3}")