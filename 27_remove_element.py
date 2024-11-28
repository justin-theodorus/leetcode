class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        ans = 0
        for num in nums:
            if num != val:
                nums[idx] = num
                idx += 1
                ans += 1
        return ans