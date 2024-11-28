class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 0
        idx = 0
        seen = []
        for num in nums:
            if num not in seen:
                cnt += 1
                nums[idx] = num
                idx += 1
                seen.append(num)
        return cnt